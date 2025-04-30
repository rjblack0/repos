# feeds/shodan_fetcher.py

import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv
from utils.config_loader import load_config

# Load environment and config
load_dotenv()
config = load_config()

API_KEY = os.getenv("SHODAN_API_KEY")
OUTPUT_PATH = "feeds/output/shodan_iocs.json"

SHODAN_SEARCH_URL = "https://api.shodan.io/shodan/host/search"

DEFAULT_QUERY = "port:3389 country:US"  # RDP servers in the US

def fetch_shodan_iocs(query=DEFAULT_QUERY, limit=50):
    print(f"[*] Querying Shodan with: \"{query}\"")

    try:
        response = requests.get(
            SHODAN_SEARCH_URL,
            params={
                "key": API_KEY,
                "query": query
            }
        )
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"[!] Failed to fetch from Shodan: {e}")
        return

    matches = data.get("matches", [])[:limit]
    iocs = []

    for item in matches:
        iocs.append({
            "indicator": item["ip_str"],
            "type": "IPv4",
            "description": item.get("hostnames", ["Exposed service"])[0],
            "port": item.get("port"),
            "org": item.get("org"),
            "created": datetime.utcnow().isoformat(),
            "source": "Shodan"
        })

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(iocs, f, indent=2)

    print(f"[+] Saved {len(iocs)} IOCs to {OUTPUT_PATH}")


if __name__ == "__main__":
    feed_cfg = config.get("feeds", {}).get("shodan", {})
    if feed_cfg.get("enabled", False):
        query = feed_cfg.get("query", DEFAULT_QUERY)
        limit = feed_cfg.get("limit", 50)
        fetch_shodan_iocs(query, limit)
    else:
        print("[*] Shodan feed is disabled in config.yaml.")
