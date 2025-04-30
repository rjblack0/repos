# feeds/enrich_matched_iocs.py

import os
import json
import requests
from datetime import datetime
from time import sleep

ALERT_PATHS = [
    "output/alerts_syslog.json",
    "output/alerts_ufw.json",
    "output/alerts_auth.json"
]

CACHE_PATH = "feeds/output/ip_enrichment_cache.json"
OUTPUT_PATH = "output/enriched_alerts.json"
IP_API_URL = "https://ipapi.co/{}/json/"

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def extract_matched_indicators():
    indicators = set()
    for path in ALERT_PATHS:
        alerts = load_json(path)
        for entry in alerts:
            ioc = entry.get("matched_indicator")
            if ioc and ":" not in ioc:  # Skip IPv6 for now
                indicators.add(ioc)
    return sorted(indicators)

def enrich_ip(ip, cache):
    if ip in cache:
        return cache[ip]

    try:
        response = requests.get(IP_API_URL.format(ip), timeout=5)
        if response.status_code == 200:
            data = response.json()
            cache[ip] = {
                "indicator": ip,
                "geo": {
                    "country": data.get("country_name"),
                    "region": data.get("region"),
                    "city": data.get("city")
                },
                "asn": data.get("asn"),
                "org": data.get("org"),
                "last_checked": datetime.utcnow().isoformat()
            }
        else:
            print(f"[!] Failed to enrich {ip}: HTTP {response.status_code}")
            cache[ip] = {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        print(f"[!] Error enriching {ip}: {e}")
        cache[ip] = {"error": str(e)}

    sleep(1)  # Respect API limits
    return cache[ip]

def main():
    print("[*] Extracting matched IOCs from alert files...")
    iocs = extract_matched_indicators()
    print(f"[+] Found {len(iocs)} unique matched IOCs to enrich.")

    cache = load_json(CACHE_PATH)
    enriched = []

    for i, ip in enumerate(iocs, 1):
        print(f"  [{i}/{len(iocs)}] Enriching {ip}...")
        info = enrich_ip(ip, cache)
        if isinstance(info, dict):
            enriched.append(info)

    save_json(enriched, OUTPUT_PATH)
    save_json(cache, CACHE_PATH)

    print(f"[+] Enriched alerts saved to {OUTPUT_PATH}")
    print(f"[+] Cache updated with {len(cache)} total entries.")

if __name__ == "__main__":
    main()
