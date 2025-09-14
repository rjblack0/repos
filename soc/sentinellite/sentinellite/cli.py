# sentinellite/cli.py
import os, sys, re
from pathlib import Path
from datetime import datetime, timezone

# Orchestrators (subprocess-based)
from .orchestrator import pull_feeds, scan_logs

# Direct module calls for enrichment/digest if needed
from feeds import enrich_matched_iocs as enrich_mod
from digest.summary_engine import generate_digest

from dotenv import load_dotenv

BANNER = r"""
   _____            _      _ _
  / ____|          | |    (_) |
 | (___   ___ _ __ | |     _| |_ ___
  \___ \ / _ \ '_ \| |    | | __/ _ \
  ____) |  __/ | | | |____| | ||  __/
 |_____/ \___|_| |_|______|_|\__\___|

                SenLite — Threat Scanner
"""

ABOUT_TEXT = """
SenLite — Lightweight IOC Pull, Scan, Enrich, and Digest

What it does
------------
• Load IOC Feeds: pulls OTX + AbuseIPDB, consolidates to a single IOC list.
• Scan Logs: checks your configured logs for those indicators.
• Enrich: geo/ASN/org (ipapi) + Shodan (ports/tags/CVEs) for matched IPs.
• Digest: Markdown summary under output/digests/.

Default file locations
----------------------
• Consolidated IOCs:       feeds/output/consolidated_iocs.json
• Alerts:                  output/alerts_syslog.json | alerts_ufw.json | alerts_auth.json
• Enriched matches:        output/enriched_alerts.json
• Digests (Markdown):      output/digests/threat_digest_*.md

Config & API keys
-----------------
• Edit logs in config.yaml:
    logs:
      syslog: "/var/log/syslog"
      ufw:    "/var/log/ufw.log"
      auth:   "/var/log/auth.log"

• API keys live in .env (kept out of git):
    OTX_API_KEY=...
    ABUSEIPDB_API_KEY=...
    SHODAN_API_KEY=...

• You can set/update keys via menu: [K] Configure API keys

Typical flows
-------------
• Quicksearch (pull + scan + digest): [Q]
• Pull only: [L]
• Scan (+enrich +digest): [S]
• Enrich-only: [E]
• Read last digest & alert snapshots: [R]

Security notes
--------------
• .env contains secrets. Keep perms 0600 and out of source control.
• Respect rate limits (public APIs will throttle).
"""

MENU = """
[L] Load IOC feeds
[E] Enrich matched indicators
[S] Scan logs (+enrich +digest)
[Q] Quicksearch (Load + Scan)
[R] Read latest digest & alerts
[K] Configure API keys
[A] About / Instructions
[X] Exit
"""

ENV_PATH = Path(".env")

# --------- CLI UTIL ---------
def clear(no_clear: bool):
    if no_clear:
        return
    os.system("clear" if os.name != "nt" else "cls")

def is_tty():
    try:
        return sys.stdin.isatty()
    except Exception:
        return False

def ask(prompt: str) -> str:
    try:
        return input(prompt)
    except EOFError:
        print("\n[!] No interactive input available (stdin not a TTY). Exiting.")
        sys.exit(1)

# --------- ACTIONS ---------
def load_ioc():
    print("\n[*] Pulling and consolidating IOCs...")
    pull_feeds()
    print("[+] IOC load complete.\n")

def enrich():
    print("\n[*] Enriching matched indicators...")
    # Call enrichment directly (does NOT require a full scan)
    enrich_mod.main()
    print("[+] Enrichment complete.\n")

def scan():
    print("\n[*] Scanning logs...")
    # orchestrator.scan_logs() already runs: parsers → enrich → digest
    scan_logs()
    print("[+] Scan (incl. enrich + digest) complete.\n")

def quicksearch():
    print("\n[*] Quicksearch = Load IOC → Scan")
    load_ioc()
    scan()

def read_logs():
    dig_dir = Path("output/digests")
    if dig_dir.exists():
        digests = sorted(dig_dir.glob("threat_digest_*.md"))
        if digests:
            latest = digests[-1]
            print(f"\n=== {latest.name} ===\n")
            try:
                print(latest.read_text())
            except Exception as e:
                print(f"[!] Failed to read digest: {e}")
        else:
            print("[*] No digests yet. Run Scan first.")
    else:
        print("[*] No digest directory yet. Run Scan first.")

    # Quick peek at alert files
    for p in [Path("output/alerts_syslog.json"),
              Path("output/alerts_ufw.json"),
              Path("output/alerts_auth.json")]:
        print(f"\n--- {p} (first ~10 lines) ---")
        if not p.exists():
            print("(no file)")
            continue
        try:
            with p.open("r", encoding="utf-8", errors="ignore") as f:
                for i, line in enumerate(f):
                    if i >= 10: break
                    print(line.rstrip())
        except Exception as e:
            print(f"[!] {e}")

# --------- ABOUT ---------
def show_about():
    print("\n" + ABOUT_TEXT.strip() + "\n")

# --------- API KEYS ---------
def _mask(val: str) -> str:
    if not val: return ""
    return val if len(val) <= 8 else (val[:4] + "*" * (len(val)-8) + val[-4:])

def _load_env_map() -> dict:
    # Load into process (won't override already-set environment vars)
    load_dotenv(ENV_PATH)
    data = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            if not line or line.strip().startswith("#"): 
                continue
            if "=" in line:
                k, v = line.split("=", 1)
                data[k.strip()] = v.strip()
    return data

def _write_env_map(env_map: dict):
    lines = [
        "# SenLite API keys (.env)",
        "# Keep this file out of source control!",
        f"OTX_API_KEY={env_map.get('OTX_API_KEY','')}",
        f"ABUSEIPDB_API_KEY={env_map.get('ABUSEIPDB_API_KEY','')}",
        f"SHODAN_API_KEY={env_map.get('SHODAN_API_KEY','')}",
    ]
    ENV_PATH.write_text("\n".join(lines) + "\n")
    try:
        os.chmod(ENV_PATH, 0o600)  # WSL/Linux
    except Exception:
        pass

def _looks_like_key(s: str) -> bool:
    return bool(s) and bool(re.match(r"^[A-Za-z0-9_\-\.]{8,}$", s))

def configure_api_keys():
    print("\n[*] Configure API keys (.env)\n")
    env_map = _load_env_map()

    otx    = env_map.get("OTX_API_KEY") or os.getenv("OTX_API_KEY") or ""
    abuse  = env_map.get("ABUSEIPDB_API_KEY") or os.getenv("ABUSEIPDB_API_KEY") or ""
    shodan = env_map.get("SHODAN_API_KEY") or os.getenv("SHODAN_API_KEY") or ""

    print("Press Enter to keep the current value.\n")
    print(f"OTX_API_KEY         current: { _mask(otx) or '(none)' }")
    newv = ask("Enter OTX_API_KEY: ").strip()
    if newv: otx = newv

    print(f"ABUSEIPDB_API_KEY   current: { _mask(abuse) or '(none)' }")
    newv = ask("Enter ABUSEIPDB_API_KEY: ").strip()
    if newv: abuse = newv

    print(f"SHODAN_API_KEY      current: { _mask(shodan) or '(none)' }")
    newv = ask("Enter SHODAN_API_KEY: ").strip()
    if newv: shodan = newv

    # Gentle sanity hints
    for label, val in [("OTX_API_KEY", otx), ("ABUSEIPDB_API_KEY", abuse), ("SHODAN_API_KEY", shodan)]:
        if val and not _looks_like_key(val):
            print(f"[!] {label} looks unusual; saving anyway.")

    env_map["OTX_API_KEY"] = otx
    env_map["ABUSEIPDB_API_KEY"] = abuse
    env_map["SHODAN_API_KEY"] = shodan
    _write_env_map(env_map)

    # Also update this process so user can continue without restarting
    if otx:    os.environ["OTX_API_KEY"] = otx
    if abuse:  os.environ["ABUSEIPDB_API_KEY"] = abuse
    if shodan: os.environ["SHODAN_API_KEY"] = shodan

    print("\n[+] Saved .env and updated current session.")
    print("    • Verify with [L] Load IOC feeds (AbuseIPDB requires its key).\n")

# --------- ENTRYPOINT ---------
def main():
    no_clear = ("--no-clear" in sys.argv)
    debug    = ("--debug"    in sys.argv)

    clear(no_clear)
    print(BANNER)
    print(f"Started: {datetime.now(timezone.utc).isoformat()}\n")

    if debug:
        print(f"[debug] cwd={os.getcwd()}")
        print(f"[debug] isatty(stdin)={is_tty()}")
        print(f"[debug] PYTHONPATH={os.environ.get('PYTHONPATH','')}")

    while True:
        print(MENU)
        choice = ask("> ").strip().lower()
        if   choice == "l": load_ioc()
        elif choice == "e": enrich()
        elif choice == "s": scan()
        elif choice == "q": quicksearch()
        elif choice == "r": read_logs()
        elif choice == "k": configure_api_keys()
        elif choice == "a": show_about()
        elif choice == "x": break
        elif choice in ("", None):
            # empty entry can happen on odd terminals; loop again
            continue
        else:
            print("Unknown option.")

if __name__ == "__main__":
    main()
