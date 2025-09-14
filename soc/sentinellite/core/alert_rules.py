# core/alert_rules.py
from collections import Counter, defaultdict
from datetime import datetime, timezone
import json, os

from utils.config_loader import load_config

# ---------- Config ----------
CFG = load_config()

def _policy_list(key: str):
    """Safely read a list from config.policy.<key>."""
    return list(((CFG.get("policy", {}) or {}).get(key, [])) or [])

# ---------- Helpers ----------
def _now_iso():
    return datetime.utcnow().isoformat()

def _norm(s: str) -> str:
    return (s or "").strip().lower()

def _in_norm_set(value: str, items) -> bool:
    """Case-insensitive 'contains' matching against a set/list of fragments."""
    v = _norm(value)
    if not v:
        return False
    for it in items or []:
        itn = _norm(it)
        if not itn:
            continue
        if itn in v:
            return True
    return False

# ---------- Loaders ----------
def load_alerts():
    """Load per-log IOC match alerts produced by the parsers."""
    files = [
        ("syslog", "output/alerts_syslog.json"),
        ("ufw",    "output/alerts_ufw.json"),
        ("auth",   "output/alerts_auth.json"),
    ]
    res = {k: [] for k, _ in files}
    for key, fp in files:
        if os.path.exists(fp):
            try:
                res[key] = json.load(open(fp, "r", encoding="utf-8", errors="ignore"))
                if not isinstance(res[key], list):
                    res[key] = []
            except Exception:
                res[key] = []
    return res

def load_enriched_iocs():
    """Load enrichment results (geo/asn/org + shodan)."""
    path = "output/enriched_alerts.json"
    if not os.path.exists(path):
        return []
    try:
        data = json.load(open(path, "r", encoding="utf-8", errors="ignore"))
        return data if isinstance(data, list) else []
    except Exception:
        return []

# ---------- Rules ----------
def rule_repeated_hits(all_alerts, min_hits: int = 5):
    """
    Flag indicators that appear frequently across any logs.
    """
    hits = Counter(a.get("matched_indicator") for a in all_alerts if a.get("matched_indicator"))
    flagged = []
    for ind, cnt in hits.items():
        if cnt >= min_hits:
            flagged.append({
                "rule": f"Repeated indicator seen >= {min_hits} times",
                "indicator": ind,
                "count": cnt,
                "timestamp": _now_iso(),
            })
    return flagged

def rule_failed_ssh_logins(auth_alerts, threshold: int = 3):
    """
    Rough SSH brute detection based on auth log lines.
    """
    per_ind = defaultdict(int)
    for a in auth_alerts:
        line = _norm(a.get("log_line"))
        ind  = a.get("matched_indicator")
        if not ind:
            continue
        if "failed password" in line or "authentication failure" in line:
            per_ind[ind] += 1

    flagged = []
    for ind, cnt in per_ind.items():
        if cnt >= threshold:
            flagged.append({
                "rule": f"Multiple failed SSH logins (>= {threshold})",
                "indicator": ind,
                "count": cnt,
                "timestamp": _now_iso(),
            })
    return flagged

def rule_country_block(enriched):
    """
    Flag indicators whose geo.country is NOT in allowed_countries.
    """
    allowed = set(_policy_list("allowed_countries"))
    if not allowed:
        return []
    flagged = []
    for item in enriched:
        country = ((item.get("geo") or {}).get("country") or "Unknown")
        if country and country not in allowed:
            flagged.append({
                "rule": "Country not allowed",
                "indicator": item.get("indicator"),
                "country": country,
                "org": item.get("org"),
                "timestamp": _now_iso(),
            })
    return flagged

def rule_cloud_provider_block(enriched):
    """
    Flag indicators whose provider/org string matches any fragment in cloud_orgs.
    Matches against both 'org' and 'asn' fields.
    """
    cloud_orgs = _policy_list("cloud_orgs")
    if not cloud_orgs:
        return []
    flagged = []
    for item in enriched:
        org = (item.get("org") or "")
        asn = (item.get("asn") or "")
        if _in_norm_set(org, cloud_orgs) or _in_norm_set(asn, cloud_orgs):
            flagged.append({
                "rule": "Source is cloud provider (policy blocklist)",
                "indicator": item.get("indicator"),
                "org": org,
                "asn": asn,
                "timestamp": _now_iso(),
            })
    return flagged

def rule_suspicious_orgs(enriched):
    """
    Flag indicators whose org string matches any fragment in suspicious_orgs.
    """
    susp = _policy_list("suspicious_orgs")
    if not susp:
        return []
    flagged = []
    for item in enriched:
        org = (item.get("org") or "")
        if _in_norm_set(org, susp):
            flagged.append({
                "rule": "Source ASN/Org known suspicious",
                "indicator": item.get("indicator"),
                "org": org,
                "timestamp": _now_iso(),
            })
    return flagged

# --- Optional Shodan-powered rules (safe if shodan missing) ---
def rule_exposed_risky_services(enriched, risky_ports={23, 2323, 3389, 5900, 7547}):
    """
    Use Shodan ports to flag risky exposure (telnet, rdp, vnc, tr-069, etc.).
    """
    flagged = []
    for item in enriched:
        sh = item.get("shodan") or {}
        ports = set(sh.get("ports") or [])
        risky = sorted(list(ports & set(risky_ports)))
        if risky:
            flagged.append({
                "rule": "Matched indicator has risky open ports",
                "indicator": item.get("indicator"),
                "risky_ports": risky,
                "timestamp": _now_iso(),
            })
    return flagged

def rule_known_vulns_present(enriched):
    """
    Use Shodan 'vulns' (CVE IDs) if present.
    """
    flagged = []
    for item in enriched:
        vulns = (item.get("shodan") or {}).get("vulns") or []
        if vulns:
            flagged.append({
                "rule": "Shodan reports known CVEs",
                "indicator": item.get("indicator"),
                "cves": list(vulns)[:10],
                "timestamp": _now_iso(),
            })
    return flagged

# ---------- Orchestrator ----------
def evaluate(all_alerts_map):
    """
    Run all rules and return a flat list of detections.
    """
    syslog = all_alerts_map.get("syslog", []) or []
    ufw    = all_alerts_map.get("ufw", []) or []
    auth   = all_alerts_map.get("auth", []) or []
    combined = syslog + ufw + auth

    flagged = []
    # Volume/behavior rules on raw matches
    flagged += rule_repeated_hits(combined, min_hits=5)
    flagged += rule_failed_ssh_logins(auth, threshold=3)

    # Enrichment-based rules
    enriched = load_enriched_iocs()
    flagged += rule_country_block(enriched)
    flagged += rule_cloud_provider_block(enriched)
    flagged += rule_suspicious_orgs(enriched)
    flagged += rule_exposed_risky_services(enriched)
    flagged += rule_known_vulns_present(enriched)

    return flagged
