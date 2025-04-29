# SentinelLite

### Lightweight Modular SIEM with Integrated Threat Intelligence Digest

---

## Mission Statement

**SentinelLite** aims to democratize cybersecurity visibility by providing a lightweight, modular, and user-friendly SIEM solution that combines internal log analysis with curated external threat intelligence — delivering actionable insights through a plain-English daily digest. Designed with small businesses, home labs, and independent analysts in mind, SentinelLite lowers the barrier to threat detection and response without sacrificing clarity or functionality.

---

## Taglines?

Professional & Polished
SentinelLite – Security insights made simple.

Technical & Clear
SentinelLite – Modular SIEM meets real-time threat intelligence.

Clever & Memorable
SentinelLite – Think small. Detect big.

For Your Target Audience
SentinelLite – Cyber threat awareness for teams without a SOC.



## Project Goal

To build a Python-based, open-source SIEM that:
- Collects and parses logs from common system and application sources
- Integrates real-time threat intelligence feeds (OTX, Shodan, AbuseIPDB, etc.)
- Matches IOCs and anomalies across internal and external data
- Generates human-readable daily/weekly **Threat Intelligence Digests**
- Operates efficiently on resource-limited systems (e.g., Raspberry Pi)
- Requires minimal configuration and no enterprise licenses

---

## Features

- Modular architecture for log collectors and feed integrations
- Local alert engine with customizable rule matching
- IOC enrichment from global threat sources
- NLP-based digest generation for non-technical stakeholders
- Exportable reports in Markdown, PDF, or HTML
- Optional web interface for visualizing logs and alerts

---

## Tech Stack

- **Language:** Python 3.x

## Roadmap

- [ ] Implement core log ingestion (syslog, UFW, web server)
- [ ] Build modular parser system
- [ ] Create lightweight IOC correlation engine
- [ ] Integrate first threat feed (OTX)
- [ ] Develop NLP-based digest generator
- [ ] Add CLI interface
- [ ] Add optional web UI (Flask)