# digest/summary_engine.py

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json, os
from datetime import datetime, timezone
from utils.config_loader import load_config
from core import alert_rules

now = datetime.now(timezone.utc)
config = load_config()

ENRICHED_ALERTS_PATH = "output/enriched_alerts.json"

def _safe_load(path):
    if not os.path.exists(path): return []
    try: return json.load(open(path, "r"))
    except Exception: return []

def summarize_alerts(all_alerts_map, max_per_log=5):
    total = 0
    out = []
    for key in ["syslog","ufw","auth"]:
        alerts = all_alerts_map.get(key, [])
        if not alerts: continue
        out.append(f"### {key} ({len(alerts)} total)\n")
        for alert in alerts[:max_per_log]:
            out.append(f"- {alert['matched_indicator']} — {alert['log_line']}")
        total += len(alerts)
        out.append("")
    return "\n".join(out) if total else "No matches found in any monitored logs.\n"

def summarize_behavioral_alerts(flags):
    if not flags: return "No behavioral detections found.\n"
    out = []
    for item in flags:
        line = f"- [{item['rule']}] {item['indicator']} — {item.get('org','')} {item.get('country','')} (count={item.get('count','')})"
        out.append(line)
    return "\n".join(out)

def summarize_enriched_alerts(enriched):
    if not enriched:
        return "No geographic or ASN information available for matched indicators.\n"
    out = []
    for item in enriched:
        ip = item.get("indicator")
        geo = item.get("geo", {})
        asn = item.get("asn", "N/A")
        org = item.get("org", "N/A")
        sh = item.get("shodan") or {}
        ports = sh.get("ports") or []
        tags = sh.get("tags") or []
        vulns = sh.get("vulns") or []
        out.append(
            f"- {ip} — {geo.get('country','Unknown')} "
            f"({org}, ASN {asn}); ports={ports[:10]} "
            f"tags={tags[:6]} vulns={vulns[:6]}"
        )
    return "\n".join(out)

def generate_digest():
    print("[*] Generating threat digest...")
    all_alerts_map = alert_rules.load_alerts()
    flags = alert_rules.evaluate(all_alerts_map)
    enriched = _safe_load(ENRICHED_ALERTS_PATH)

    out_dir = config.get("digest",{}).get("output_dir","output/digests")
    os.makedirs(out_dir, exist_ok=True)
    digest_path = os.path.join(out_dir, f"threat_digest_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.md")

    with open(digest_path, "w") as f:
        f.write(f"# SentinelLite Threat Digest\nGenerated: {datetime.now(timezone.utc).isoformat()} UTC\n\n")
        f.write("## Matched Indicators in Local Logs\n")
        f.write(summarize_alerts(all_alerts_map, max_per_log=config.get('digest',{}).get('max_alerts_per_log',5)))
        f.write("\n\n## Behavior-Based Alerts\n")
        f.write(summarize_behavioral_alerts(flags))
        f.write("\n\n## Enriched Matches (Geo + ASN)\n")
        f.write(summarize_enriched_alerts(enriched))

    print(f"[+] Digest generated at: {digest_path}")
    return digest_path

if __name__ == "__main__":
    generate_digest()
