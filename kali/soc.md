## SOC WORKFLOW
# Goal: Detect, investigate, and respond to suspicious activity
# Focus: Alerts → Validation → Evidence → Containment → Documentation

## 1. Alert Intake

# Sources:
# SIEM (Splunk / ELK)
# EDR alerts
# IDS/IPS (Snort / Suricata)
# Firewall logs
# User reports

# Key Questions:
# What triggered the alert?
# Which host/user is involved?
# When did it happen?

## 2. Triage (Is this real?)

# Tools:
# SIEM queries
# httpx (check suspicious domains)
# Shodan / Censys (external IP intel)

# Actions:
# Check reputation of IP/domain
# Validate alert context
# Look for false positives

# httpx check
httpx -silent -status-code -title suspicious_domain.txt

## Goal
False positive → close
Suspicious → escalate

## 3. Initial Investigation

# Tools:
# Wireshark
# tcpdump
# SIEM queries
# DNS logs

# Actions:
# Identify communication patterns
# Check DNS requests
# Look for unusual traffic

tcpdump -i eth0 host 192.168.1.10

# Wireshark Filters
ip.addr == x.x.x.x
dns.qry.name contains "suspicious"
tcp.flags.syn == 1

## Goal
Confirm suspicious behavior
Identify scope

## 4. Network Analysis

# Tools:
# Wireshark
# tcpdump
# Nmap (internal validation)

# Actions:
# Analyze traffic flows
# Check lateral movement
# Identify open services

nmap -sS -sV 192.168.1.10

## Goal:
Unexpected ports
Beaconing traffic
Internal scanning

## 5. Host Investigation

# Tools:
# EDR platform
# Netstat / lsof
# Logs

# Actions:
# Check running processes
# Identify suspicious binaries
# Look for persistence mechanisms

lsof -i
netstat -tulnp

## Goal:
Unknown processes
Outbound connections
Privilege escalation

## 6. CREDENTIAL / ACCOUNT ANALYSIS

# Tools:
# SIEM logs
# AD logs
# BloodHound (if available)

# Actions:
# Check login attempts
# Look for brute force / spraying
# Identify privilege escalation

## Goal:
Multiple failed logins
Logins from unusual locations
New admin accounts

