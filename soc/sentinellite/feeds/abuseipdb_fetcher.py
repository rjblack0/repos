# feeds/abuseipdb_fetcher.py

import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv
from utils.config_loader import load_config

# Load config and environment
load_dotenv()
config = load_config()

API_KEY = os.getenv("ABUSEIPDB_API_KEY")
OUTPUT_PATH = "feeds/output/abuseipdb_iocs.json"
ABUSEIPDB_ENDPOINT = "https://api.abuseipdb.com/api/v2/blacklist"

HEADERS = {
    "Key": API_KEY,
    "Accept": "application/json"
}


def fetch_abuseipdb_iocs(limit=50):
    print("[*] Fetching malicious IPs from AbuseIPDB...")

    try:
        response = requests.get(
            ABUSEIPDB_ENDPOINT,
            headers=HEADERS,
            params={"confidenceMinimum": 90}
        )
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"[!] Failed to fetch AbuseIPDB data: {e}")
        return

    iocs = []

    for item in data.get("data", [])[:limit]:
        iocs.append({
            "indicator": item["ipAddress"],
            "type": "IPv4",
            "description": "High-confidence malicious IP (AbuseIPDB)",
            "confidence": item.get("abuseConfidenceScore"),
            "country": item.get("countryCode"),
            "created": datetime.utcnow().isoformat(),
            "source": "AbuseIPDB"
        })

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(iocs, f, indent=2)

    print(f"[+] Saved {len(iocs)} IOCs to {OUTPUT_PATH}")


if __name__ == "__main__":
    feed_cfg = config.get("feeds", {}).get("abuseipdb", {})
    if feed_cfg.get("enabled", False):
        limit = feed_cfg.get("limit", 50)
        fetch_abuseipdb_iocs(limit)
    else:
        print("[*] AbuseIPDB feed is disabled in config.yaml.")
