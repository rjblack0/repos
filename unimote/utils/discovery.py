# utils/discovery.py

import json
import requests
from devices import (
    RokuDevice, TPLinkDevice, PrinterDevice, RESTAPIDevice, BroadlinkDevice,
    ChromecastDevice, MQTTDevice, HomeAssistantDevice, SmartTVDevice,
    ComputerDevice, PhoneDevice, IPCameraDevice
)

CONFIG_FILE = "config.json"

def load_ip_addresses():
    """Load a list of IP addresses from the config.json file."""
    try:
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
            return config.get("ip_addresses", [])
    except FileNotFoundError:
        print(f"{CONFIG_FILE} not found. Please ensure it exists in the project root.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {CONFIG_FILE}. Please check the file format.")
        return []

def scan_ip_addresses(ip_addresses):
    """Scan a list of IP addresses to see if they are reachable."""
    reachable_ips = []
    for ip in ip_addresses:
        try:
            response = requests.get(ip, timeout=5)
            if response.status_code == 200:
                reachable_ips.append(ip)
                print(f"IP {ip} is reachable.")
            else:
                print(f"IP {ip} responded with status code {response.status_code}.")
        except requests.RequestException:
            print(f"IP {ip} is not reachable.")
    return reachable_ips

def discover_all_devices():
    """Discover all device types available on the network."""
    devices = []
    devices.extend(RokuDevice.discover())
    devices.extend(TPLinkDevice.discover())
    devices.extend(PrinterDevice.discover())
    devices.extend(RESTAPIDevice.discover())
    devices.extend(BroadlinkDevice.discover())
    devices.extend(ChromecastDevice.discover())
    devices.extend(MQTTDevice.discover())
    devices.extend(HomeAssistantDevice.discover())
    devices.extend(SmartTVDevice.discover())
    devices.extend(ComputerDevice.discover())
    devices.extend(PhoneDevice.discover())
    devices.extend(IPCameraDevice.discover())
    return devices
