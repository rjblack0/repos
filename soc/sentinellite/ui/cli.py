# ui/cli.py
from sentinellite import pull_feeds, scan_logs
from pathlib import Path

def read_latest_digest():
    dig_dir = Path("output/digests")
    if not dig_dir.exists():
        print("No digest directory found. Run a scan first.")
        return
    files = sorted(dig_dir.glob("threat_digest_*.md"))
    if not files:
        print("No digest found. Run a scan first.")
        return
    latest = files[-1]
    print(f"\n=== {latest.name} ===\n")
    print(latest.read_text())

def menu():
    while True:
        print("\n================ SentinelLite Menu ================")
        print("1) Pull feeds")
        print("2) Scan logs")
        print("3) Read latest digest")
        print("q) Quit")
        choice = input("> ").strip().lower()
        if choice == "1":
            pull_feeds()
        elif choice == "2":
            scan_logs()
        elif choice == "3":
            read_latest_digest()
        elif choice in ("q","quit","exit"):
            print("Bye.")
            break
        else:
            print("Unknown choice.")

if __name__ == "__main__":
    menu()
