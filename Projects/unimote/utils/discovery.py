# utils/discovery.py

import json
import os
from devices import (
    RokuDevice, TPLinkDevice, PrinterDevice, RESTAPIDevice, BroadlinkDevice,
    ChromecastDevice, MQTTDevice, HomeAssistantDevice, SmartTVDevice,
    ComputerDevice, PhoneDevice, IPCameraDevice
)

# Define path to config file
CONFIG_FILE_PATH = "config.json"

def load_ip_addresses():
    """Load a list of IP addresses from the configuration file."""
    if not os.path.exists(CONFIG_FILE_PATH):
        print(f"Configuration file '{CONFIG_FILE_PATH}' not found.")
        return []

    with open(CONFIG_FILE_PATH, 'r') as file:
        config = json.load(file)
        ip_addresses = config.get("ip_addresses", [])
        print(f"Loaded IP addresses from config: {ip_addresses}")
        return ip_addresses

def scan_ip_addresses(ip_addresses):
    """Check if provided IP addresses are reachable."""
    reachable_ips = []
    for ip in ip_addresses:
        # Simple example of checking reachability (can be replaced with actual ping/HTTP checks)
        try:
            response = os.system(f"ping -c 1 {ip}")
            if response == 0:
                print(f"{ip} is reachable")
                reachable_ips.append(ip)
            else:
                print(f"{ip} is not reachable")
        except Exception as e:
            print(f"Error scanning IP {ip}: {e}")
    return reachable_ips

def discover_all_devices():
    """Discover all device types available on the network and summarize results."""
    devices = []
    found_device_types = []  # Track what types of devices were found
    device_types = {
        "Roku Devices": RokuDevice,
        "TP-Link Devices": TPLinkDevice,
        "Printers": PrinterDevice,
        "REST API Devices": RESTAPIDevice,
        "Broadlink Devices": BroadlinkDevice,
        "Chromecast Devices": ChromecastDevice,
        "MQTT Devices": MQTTDevice,
        "Home Assistant Devices": HomeAssistantDevice,
        "Smart TVs": SmartTVDevice,
        "Computers": ComputerDevice,
        "Phones": PhoneDevice,
        "IP Cameras": IPCameraDevice
    }

    for device_name, device_class in device_types.items():
        found_devices = device_class.discover()
        if found_devices:
            found_device_types.append(device_name)  # Only log the type if devices are found
            devices.extend(found_devices)

    # Display a summary of device types found
    if found_device_types:
        print("\nSummary of Devices Found:")
        for device_type in found_device_types:
            print(f"- {device_type}")
    else:
        print("\nNo devices found on the network.")

    return devices
