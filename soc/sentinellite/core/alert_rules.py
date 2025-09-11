# core/alert_rules.py

from collections import Counter, defaultdict
from datetime import datetime
from utils.config_loader import load_config
import json
import os

def _norm_str(v):
    """Return a lowercase string, safely handling None."""
    return (v or "").stripe().lower()

def _in_norm_set(value, items):
    """Case/whitespiace-insensitive membership."""
    return _norm_str(value) in {_norm_str(x) for x in items or []}

config = load_config()

IOC_THRESHOLD = config.get("rules", {}).get("repeated_ioc_threshold", 3)
ALLOWED_COUNTRIES = config.get("rules", {}).get("allowed_countries", [])
CLOUD_ORGS = cfg.get("cloud_orgs", [])
if _in_norm_set(org, CLOUD_ORGS) or _in_norm_set(asn_org, CLOUD_ORGS):
    flag.append({"type": "cloud_provider_block", "org": org or asn_org})    
SUSPICIOUS_ORGS = [org.lower() for org in config.get("rules", {}).get("suspicious_orgs", [])]

ENRICHED_IOCS_PATH = "output/enriched_alerts.json"


def group_by_indicator(alerts):
    grouped = defaultdict(list)
    for alert in alerts:
        key = alert.get("matched_indicator")
        grouped[key].append(alert)
    return grouped


def rule_repeated_hits(alerts):
    flagged = []
    counts = Counter(a["matched_indicator"] for a in alerts)
    for indicator, count in counts.items():
        if count >= IOC_THRESHOLD:
            flagged.append({
                "indicator": indicator,
                "count": count,
                "rule": f"Repeated IOC match ({count} hits)",
                "timestamp": datetime.utcnow().isoformat()
            })
    return flagged


def rule_failed_ssh_logins(alerts):
    flagged = []
    for alert in alerts:
        line = alert.get("log_line", "").lower()
        if "sshd" in line and ("failed password" in line or "invalid user" in line):
            flagged.append({
                "indicator": alert["matched_indicator"],
                "log_line": alert["log_line"],
                "rule": "Failed SSH login attempt",
                "timestamp": datetime.utcnow().isoformat()
            })
    return flagged


def rule_country_block(enriched):
    flagged = []
    for ioc in enriched:
        geo = ioc.get("geo", {})
        country = geo.get("country", "Unknown")
        if country not in ALLOWED_COUNTRIES:
            flagged.append({
                "indicator": ioc.get("indicator"),
                "rule": f"Access from disallowed country: {country}",
                "country": country,
                "timestamp": datetime.utcnow().isoformat()
            })
    return flagged


def rule_cloud_provider_block(enriched):
    flagged = []
    for ioc in enriched:
        org     = _norm_str(ioc.get("org"))
        if any(cloud in org for cloud in CLOUD_ORGS):
            flagged.append({
                "indicator": ioc.get("indicator"),
                "rule": f"Known cloud provider: {ioc.get('org')}",
                "timestamp": datetime.utcnow().isoformat()
            })
    return flagged


def rule_suspicious_orgs(enriched):
    flagged = []
    for ioc in enriched:
        org = ioc.get("org", "").lower()
        if any(s in org for s in SUSPICIOUS_ORGS):
            flagged.append({
                "indicator": ioc.get("indicator"),
                "rule": f"Suspicious org detected: {ioc.get('org')}",
                "timestamp": datetime.utcnow().isoformat()
            })
    return flagged


def load_enriched_iocs():
    if not os.path.exists(ENRICHED_IOCS_PATH):
        return []
    with open(ENRICHED_IOCS_PATH, "r") as f:
        return json.load(f)


def apply_alert_rules(all_alerts):
    flagged = []

    # Standard log-based detection
    combined = all_alerts["syslog"] + all_alerts["ufw"] + all_alerts["auth"]
    flagged += rule_repeated_hits(combined)
    flagged += rule_failed_ssh_logins(all_alerts["auth"])

    # Enrichment-based detection
    enriched = load_enriched_iocs()
    flagged += rule_country_block(enriched)
    flagged += rule_cloud_provider_block(enriched)
    flagged += rule_suspicious_orgs(enriched)

    return flagged
