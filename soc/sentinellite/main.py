# main.py

import subprocess
from datetime import datetime, timezone
now = datetime.now(timezone.utc)

def print_banner():
    print("=" * 50)
    print("     🛡️  SentinelLite — Modular SIEM Engine")
    print("=" * 50)
    print(f"Started: {datetime.now(timezone.utc).isoformat()}\n")


def run_module(label, command):
    print(f"[*] Running: {label}")
    result = subprocess.run(command, shell=True)
    if result.returncode == 0:
        print(f"[+] {label} completed.\n")
    else:
        print(f"[!] {label} failed.\n")


def main():
    print_banner()

    # Step 1: Threat Feed Collectors
    run_module("OTX Threat Feed Fetcher", "python3 feeds/otx_fetcher.py")
    run_module("AbuseIPDB Feed Fetcher", "python3 feeds/abuseipdb_fetcher.py")
    run_module("Shodan Feed Fetcher", "python3 feeds/shodan_fetcher.py")

    # Step 2: Log Parsers
    run_module("Syslog IOC Matcher", "python3 core/syslog_parser.py")
    run_module("UFW Log Matcher", "python3 core/ufw_parser.py")
    run_module("Auth Log Matcher", "python3 core/auth_parser.py")

    # Step 3: Digest Generation
    run_module("Threat Digest Generator", "python3 digest/summary_engine.py")

    print("SentinelLite scan completed.\n")


if __name__ == "__main__":
    main()
