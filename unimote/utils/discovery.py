# utils/discovery.py

import requests
import json
import os

DEFAULT_IP_ADDRESSES = [
    "http://10.0.0.1/",
    "http://192.168.0.1/",
    "http://192.168.1.1/"
]

CONFIG_FILE_PATH = "config.json"

def load_ip_addresses():
    """Load IP addresses from a configuration file or use defaults."""
    if os.path.exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH, "r") as file:
            config = json.load(file)
            ip_addresses = config.get("ip_addresses", [])
            if ip_addresses:
                return ip_addresses
    return DEFAULT_IP_ADDRESSES

def scan_ip_addresses(ip_addresses):
    """Scan a list of IP addresses to check if each one is reachable."""
    reachable_ips = []
    for ip in ip_addresses:
        try:
            response = requests.get(ip, timeout=2)  # Adjust timeout as needed
            if response.status_code == 200:
                print(f"IP {ip} is reachable.")
                reachable_ips.append(ip)
            else:
                print(f"IP {ip} returned status code {response.status_code}.")
        except requests.RequestException as e:
            print(f"IP {ip} is not reachable. Error: {e}")
    return reachable_ips
