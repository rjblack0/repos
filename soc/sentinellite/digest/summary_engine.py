# digest/summary_engine.py

import json
import os
from datetime import datetime
from core import alert_rules
from utils.config_loader import load_config

# Config and paths
config = load_config()

OTX_IOC_PATH = "feeds/output/otx_iocs.json"
ENRICHED_ALERTS_PATH = "output/enriched_alerts.json"

ALERT_FILES = {
    "syslog": "output/alerts_syslog.json",
    "ufw": "output/alerts_ufw.json",
    "auth": "output/alerts_auth.json"
}

DIGEST_DIR = config.get("digest", {}).get("output_dir", "output/digests")
MAX_IOCS = config.get("digest", {}).get("max_iocs_displayed", 10)
MAX_ALERTS = config.get("digest", {}).get("max_alerts_per_log", 5)

def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

def summarize_iocs(iocs):
    lines = []
    for ioc in iocs[:MAX_IOCS]:
        lines.append(f"- [{ioc['type']}] {ioc['indicator']} ({ioc.get('pulse_name', ioc.get('source', 'unknown'))}) — {ioc.get('description', 'No description')}")
    return "\n".join(lines)

def summarize_alerts(all_alerts):
    output = ""
    total = 0
    for log_name, alerts in all_alerts.items():
        count = len(alerts)
        total += count
        if count > 0:
            output += f"\n### {log_name.upper()} — {count} match(es)\n"
            for alert in alerts[:MAX_ALERTS]:
                output += f"- {alert['matched_indicator']} matched: {alert['log_line']}\n"
    return output if total > 0 else "No matches found in any monitored logs.\n"

def summarize_behavioral_alerts(flags):
    if not flags:
        return "No behavioral detections found.\n"
    output = ""
    for item in flags:
        output += f"- [{item['rule']}] {item['indicator']} — {item['timestamp']}\n"
        if 'log_line' in item:
            output += f"  Log: {item['log_line']}\n"
    return output

def summarize_enriched_alerts(enriched):
    if not enriched:
        return "No geographic or ASN information available for matched indicators.\n"
    output = ""
    for item in enriched:
        if 'error' in item:
            continue
        ip = item.get("indicator")
        geo = item.get("geo", {})
        asn = item.get("asn", "N/A")
        org = item.get("org", "N/A")
        output += f"- {ip} — {geo.get('country', 'Unknown')} ({org}, ASN {asn})\n"
    return output

def generate_digest():
    print("[*] Generating threat digest...")

    iocs = load_json(OTX_IOC_PATH)
    enriched = load_json(ENRICHED_ALERTS_PATH)
    all_alerts = {name: load_json(path) for name, path in ALERT_FILES.items()}
    behavioral_flags = alert_rules.apply_alert_rules(all_alerts)

    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M")
    digest_path = os.path.join(DIGEST_DIR, f"threat_digest_{timestamp}.md")
    os.makedirs(DIGEST_DIR, exist_ok=True)

    with open(digest_path, "w") as f:
        f.write(f"# SentinelLite Threat Digest — {timestamp} UTC\n\n")

        f.write("## Threat Intel Feed Summary (OTX)\n")
        f.write(summarize_iocs(iocs) + "\n\n")

        f.write("## Matched Indicators in Local Logs\n")
        f.write(summarize_alerts(all_alerts) + "\n")

        f.write("\n## Behavior-Based Alerts\n")
        f.write(summarize_behavioral_alerts(behavioral_flags) + "\n")

        f.write("## Enriched Matches (Geo + ASN)\n")
        f.write(summarize_enriched_alerts(enriched))

    print(f"[+] Digest generated at: {digest_path}")


if __name__ == "__main__":
    generate_digest()
