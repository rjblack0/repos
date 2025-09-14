# feeds/consolidate_feeds.py

import json
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime, timezone
now = datetime.now(timezone.utc)
from glob import glob

FEED_OUTPUT_DIR = "feeds/output/"
OUTPUT_PATH = os.path.join(FEED_OUTPUT_DIR, "consolidated_iocs.json")

def load_iocs(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as f:
        return json.load(f)

def consolidate_feeds():
    print("[*] Consolidating threat intel feeds...")

    sources = [
        "otx_iocs.json",
        "abuseipdb_iocs.json",
        "shodan_iocs.json"
    ]

    all_iocs = []

    for filename in sources:
        path = os.path.join(FEED_OUTPUT_DIR, filename)
        iocs = load_iocs(path)
        if iocs:
            print(f"  [+] Loaded {len(iocs)} IOCs from {filename}")
        all_iocs.extend(iocs)

    # De-duplicate by indicator string
    seen = set()
    unique_iocs = []
    for ioc in all_iocs:
        key = ioc.get("indicator")
        if key and key not in seen:
            unique_iocs.append(ioc)
            seen.add(key)

    os.makedirs(FEED_OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(unique_iocs, f, indent=2)

    print(f"[+] Consolidated {len(unique_iocs)} unique IOCs saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    consolidate_feeds()
