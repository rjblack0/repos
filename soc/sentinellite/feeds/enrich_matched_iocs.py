# feeds/enrich_matched_iocs.py

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import requests
from datetime import datetime, timezone
from time import sleep
import ipaddress

# Shodan helper (you already created feeds/enrich_shodan.py)
from feeds.enrich_shodan import shodan_enabled, enrich_ip_with_shodan

NOW = datetime.now(timezone.utc)

ALERT_PATHS = [
    "output/alerts_syslog.json",
    "output/alerts_ufw.json",
    "output/alerts_auth.json",
]

CACHE_PATH = "feeds/output/ip_enrichment_cache.json"
OUTPUT_PATH = "output/enriched_alerts.json"

# ip-api alternative was fine too; sticking with your ipapi.co choice
IP_API_URL = "https://ipapi.co/{}/json/"


def _is_ipv4(s: str) -> bool:
    try:
        ipaddress.ip_address(s)
        # skip IPv6 for now, keep parity with your original behavior
        return ":" not in s
    except Exception:
        return False


def load_json_list(path: str):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []


def load_json_dict(path: str):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def save_json(data, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def extract_matched_indicators():
    indicators = set()
    for path in ALERT_PATHS:
        alerts = load_json_list(path)
        for entry in alerts:
            ioc = entry.get("matched_indicator")
            if ioc and _is_ipv4(ioc):
                indicators.add(ioc)
    return sorted(indicators)


def enrich_ip_ipapi(ip: str, cache: dict) -> dict:
    """
    Enrich with ipapi.co (geo/asn/org). Writes/returns cache[ip] dict.
    """
    cached = cache.get(ip)
    # If we already have at least a basic structure from a previous run, reuse
    if isinstance(cached, dict) and ("geo" in cached or "asn" in cached or "org" in cached):
        return cached

    try:
        resp = requests.get(IP_API_URL.format(ip), timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            cache[ip] = {
                "indicator": ip,
                "geo": {
                    "country": data.get("country_name"),
                    "region": data.get("region"),
                    "city": data.get("city"),
                },
                "asn": data.get("asn"),
                # ipapi sometimes returns "org" under different fields; try a few
                "org": data.get("org") or data.get("org_name") or data.get("company"),
                "last_checked": datetime.utcnow().isoformat(),
            }
        else:
            print(f"[!] ipapi.co failed for {ip}: HTTP {resp.status_code}")
            cache[ip] = {"indicator": ip, "error": f"ipapi HTTP {resp.status_code}"}
    except Exception as e:
        print(f"[!] ipapi.co error for {ip}: {e}")
        cache[ip] = {"indicator": ip, "error": str(e)}

    # be polite to public API
    sleep(0.5)
    return cache[ip]


def maybe_enrich_shodan(ip: str, cache: dict) -> dict:
    """
    If SHODAN_API_KEY is present and we don't have shodan cached yet,
    query Shodan and store under cache[ip]['shodan'].
    """
    if not shodan_enabled():
        # nothing to do; leave as-is
        return cache.get(ip, {"indicator": ip})

    base = cache.get(ip) or {"indicator": ip}
    if isinstance(base, dict) and "shodan" in base and isinstance(base["shodan"], dict):
        # already enriched with shodan
        return base

    try:
        sh = enrich_ip_with_shodan(ip) or {}
        # Normalize a subset of high-value fields
        shodan_view = {
            "org": sh.get("org"),
            "isp": sh.get("isp"),
            "ports": sh.get("ports") or [],
            "tags": sh.get("tags") or [],
            "hostnames": sh.get("hostnames") or [],
            "vulns": sh.get("vulns") or [],
            "last_update": sh.get("last_update"),
            "error": sh.get("error") if isinstance(sh, dict) else None,
        }
        base["shodan"] = shodan_view
        # keep raw for future pivots if you want
        raw = base.get("raw", {})
        raw["shodan"] = sh
        base["raw"] = raw
    except Exception as e:
        # Don't break the pipeline on Shodan failure
        raw = base.get("raw", {})
        raw["shodan"] = {"error": str(e)}
        base["raw"] = raw
        base["shodan"] = {"error": str(e)}

    # be polite to API
    sleep(0.5)
    cache[ip] = base
    return base


def main():
    print("[*] Extracting matched IOCs from alert files...")
    iocs = extract_matched_indicators()
    print(f"[+] Found {len(iocs)} unique IPv4 indicators to enrich.")

    cache = load_json_dict(CACHE_PATH)
    enriched_out = []

    for i, ip in enumerate(iocs, 1):
        print(f"  [{i}/{len(iocs)}] Enriching {ip}...")
        # Step 1: IPAPI enrichment (geo/asn/org)
        base = enrich_ip_ipapi(ip, cache)

        # Step 2: Shodan enrichment (ports/tags/hostnames/vulns)
        base = maybe_enrich_shodan(ip, cache)

        # Provide a consistent top-level view (useful even if APIs fail)
        record = {
            "indicator": ip,
            "geo": base.get("geo") or {},
            "asn": base.get("asn"),
            "org": base.get("org"),
            "shodan": base.get("shodan") or {},
            "raw": base.get("raw") or {},
            "last_checked": base.get("last_checked", datetime.utcnow().isoformat()),
        }
        enriched_out.append(record)

    save_json(enriched_out, OUTPUT_PATH)
    save_json(cache, CACHE_PATH)

    print(f"[+] Enriched alerts saved to {OUTPUT_PATH}")
    print(f"[+] Cache updated with {len(cache)} total entries.")


if __name__ == "__main__":
    main()
