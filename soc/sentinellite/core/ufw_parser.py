# core/ufw_parser.py

import json
import os
from datetime import datetime
from utils.config_loader import load_config

config = load_config()

IOC_PATH = "feeds/output/consolidated_iocs.json"
UFW_LOG_PATH = config.get("logs", {}).get("ufw", "/var/log/ufw.log")
ALERT_OUTPUT_PATH = "output/alerts_ufw.json"

def load_iocs():
    if not os.path.exists(IOC_PATH):
        print(f"[!] IOC file not found at {IOC_PATH}")
        return []
    with open(IOC_PATH, "r") as f:
        return json.load(f)

def extract_indicators(iocs, types=("IPv4", "domain")):
    """Extract IPs/domains to scan for."""
    return set(ioc["indicator"] for ioc in iocs if ioc["type"] in types)


def parse_ufw_log_and_match(indicators):
    """Match indicators in UFW firewall log."""
    if not os.path.exists(UFW_LOG_PATH):
        print(f"[!] UFW log not found at {UFW_LOG_PATH}")
        return []

    matches = []

    with open(UFW_LOG_PATH, "r", encoding="utf-8", errors="ignore") as log:
        for line in log:
            for indicator in indicators:
                if indicator in line:
                    matches.append({
                        "timestamp": datetime.utcnow().isoformat(),
                        "log_line": line.strip(),
                        "matched_indicator": indicator
                    })

    return matches


def save_matches(matches):
    """Save match results to JSON file."""
    if matches:
        os.makedirs(os.path.dirname(ALERT_OUTPUT_PATH), exist_ok=True)
        with open(ALERT_OUTPUT_PATH, "w") as f:
            json.dump(matches, f, indent=2)
        print(f"[+] Found {len(matches)} matches. Saved to {ALERT_OUTPUT_PATH}")
    else:
        print("[*] No matches found.")


def main():
    print("[*] Loading IOCs...")
    iocs = load_iocs()
    indicators = extract_indicators(iocs)
    print(f"[*] Loaded {len(indicators)} indicators")

    print("[*] Scanning UFW log...")
    matches = parse_ufw_log_and_match(indicators)
    save_matches(matches)


if __name__ == "__main__":
    main()
