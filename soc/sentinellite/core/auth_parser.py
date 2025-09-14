# core/auth_parser.py
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.config_loader import load_config
import json, os, re
from datetime import datetime, timezone
now = datetime.now(timezone.utc)

IOC_PATH = "feeds/output/consolidated_iocs.json"
ALERT_OUTPUT_PATH = "output/alerts_auth.json"

def load_iocs():
    if not os.path.exists(IOC_PATH):
        print(f"[!] IOC file not found at {IOC_PATH}; did you run pull/consolidate?")
        return []
    try:
        return json.load(open(IOC_PATH, "r"))
    except Exception as e:
        print(f"[!] Failed to parse IOC file: {e}")
        return []

def extract_indicators(iocs, types=("IPv4","IPv6","domain")):
    inds = []
    for i in iocs:
        t = (i.get("type") or "").strip()
        ind = (i.get("indicator") or "").strip()
        if not ind: continue
        if t in types: inds.append(ind)
    return set(inds)

def _scan_file_for_indicators(log_path, indicators, source_label):
    if not os.path.exists(log_path):
        print(f"[!] Log not found at {log_path}")
        return []
    matches = []
    doms = [d for d in indicators if "." in d and not re.match(r"^\d+([.:]\d+)+$", d)]
    ips = [ip for ip in indicators if ip not in doms]
    dom_patterns = [re.compile(rf"(?<![\w.-]){{re.escape(d)}}(?![\w.-])") for d in doms]

    with open(log_path, "r", encoding="utf-8", errors="ignore") as log:
        for line in log:
            line_s = line.strip()
            for ip in ips:
                if ip in line_s:
                    matches.append({
                        "timestamp": datetime.utcnow().isoformat(),
                        "log_line": line_s,
                        "matched_indicator": ip,
                        "source_log": source_label,
                    })
            for pat, dom in zip(dom_patterns, doms):
                if pat.search(line_s):
                    matches.append({
                        "timestamp": datetime.utcnow().isoformat(),
                        "log_line": line_s,
                        "matched_indicator": dom,
                        "source_log": source_label,
                    })
    return matches

def save_matches(matches):
    if matches:
        os.makedirs(os.path.dirname(ALERT_OUTPUT_PATH), exist_ok=True)
        json.dump(matches, open(ALERT_OUTPUT_PATH, "w"), indent=2)
        print(f"[+] Found {len(matches)} matches. Saved to {ALERT_OUTPUT_PATH}")
    else:
        print("[*] No matches found.")

config = load_config()
AUTH_LOG_PATH = config.get("logs", {}).get("auth", "/var/log/auth.log")

def main():
    print("[*] Loading IOCs...")
    iocs = load_iocs()
    indicators = extract_indicators(iocs)
    print(f"[*] Loaded {len(indicators)} indicators")
    print("[*] Scanning auth.log...")
    matches = _scan_file_for_indicators(AUTH_LOG_PATH, indicators, "auth")
    save_matches(matches)

if __name__ == "__main__":
    main()
