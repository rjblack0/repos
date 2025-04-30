# sentinellite.py

import argparse
import subprocess
from datetime import datetime, timezone

def run(label, command):
    print(f"\n[*] {label}")
    result = subprocess.run(command, shell=True)
    if result.returncode == 0:
        print(f"[+] {label} completed.")
    else:
        print(f"[!] {label} failed.")

def pull_feeds():
    run("OTX Threat Feed Fetcher", "python3 feeds/otx_fetcher.py")
    run("AbuseIPDB Feed Fetcher", "python3 feeds/abuseipdb_fetcher.py")
    run("Shodan Feed Fetcher", "python3 feeds/shodan_fetcher.py")
    run("Consolidate All IOCs", "python3 feeds/consolidate_feeds.py")

def scan_logs():
    run("Syslog IOC Matcher", "python3 core/syslog_parser.py")
    run("UFW Log Matcher", "python3 core/ufw_parser.py")
    run("Auth Log Matcher", "python3 core/auth_parser.py")
    run("Enrich Matched IOCs", "python3 feeds/enrich_matched_iocs.py")
    run("Threat Digest Generator", "python3 digest/summary_engine.py")

def main():
    parser = argparse.ArgumentParser(description="SentinelLite CLI")
    parser.add_argument("command", choices=["pull", "scan", "pull-and-scan"], help="Choose what to run")

    args = parser.parse_args()

    print("=" * 50)
    print("SentinelLite — Command-Line Interface")
    print("=" * 50)
    print(f"Started: {datetime.now(timezone.utc).isoformat()} UTC")

    if args.command == "pull":
        pull_feeds()
    elif args.command == "scan":
        scan_logs()
    elif args.command == "pull-and-scan":
        pull_feeds()
        scan_logs()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
