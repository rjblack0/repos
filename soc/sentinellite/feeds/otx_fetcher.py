# feeds/otx_fetcher.py

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import json
from dotenv import load_dotenv
from datetime import datetime, timezone
now = datetime.now(timezone.utc)
from utils.config_loader import load_config

# Load env variables and config
load_dotenv()
config = load_config()

OTX_API_KEY = os.getenv("OTX_API_KEY")
HEADERS = {"X-OTX-API-KEY": OTX_API_KEY}
BASE_URL = "https://otx.alienvault.com/api/v1/pulses/subscribed"
OUTPUT_PATH = "feeds/output/otx_iocs.json"


def fetch_otx_iocs(limit):
    print("[*] Fetching threat pulses from OTX...")
    try:
        response = requests.get(BASE_URL, headers=HEADERS, params={"limit": limit})
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"[!] Failed to fetch data from OTX: {e}")
        return

    all_iocs = []

    for pulse in data.get("results", []):
        pulse_name = pulse.get("name", "Unknown")
        created = pulse.get("created", "N/A")
        tags = pulse.get("tags", [])
        indicators = pulse.get("indicators", [])

        for ioc in indicators:
            all_iocs.append({
                "indicator": ioc.get("indicator"),
                "type": ioc.get("type"),
                "description": ioc.get("description"),
                "pulse_name": pulse_name,
                "created": created,
                "tags": tags
            })

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(all_iocs, f, indent=2)

    print(f"[+] Saved {len(all_iocs)} IOCs to {OUTPUT_PATH}")


if __name__ == "__main__":
    feed_settings = config.get("feeds", {}).get("otx", {})
    if feed_settings.get("enabled", False):
        limit = feed_settings.get("limit", 25)
        fetch_otx_iocs(limit)
    else:
        print("[*] OTX feed is disabled in config.yaml")
