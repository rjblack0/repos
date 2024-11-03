# menu.py

import sys
from devices import (
    RokuDevice, TPLinkDevice, PrinterDevice, RESTAPIDevice,
    BroadlinkDevice, ChromecastDevice, MQTTDevice, HomeAssistantDevice
)
from utils.discovery import discover_all_devices
from colorama import init

init(autoreset=True)

def show_agreement():
    """Display agreement and prompt the user to agree."""
    print("Welcome to Unimote - Network Device Control")
    print("This program is for home use only. By proceeding, you agree that:")
    print("- This software should only be used on networks you own or have explicit permission to access.")
    print("- Unauthorized network scanning or device control may violate laws or policies.")
    
    agreement = input("Do you agree to use this software responsibly? (y/n): ").strip().lower()
    if agreement != 'y':
        print("You did not agree to the terms. Exiting...")
        sys.exit(0)

def display_main_menu():
    """Display the main menu options to the user."""
    print("\nMain Menu - Please select an option:")
    print("1. Scan for Roku devices")
    print("2. Scan for TP-Link devices")
    print("3. Scan for Printers (SNMP)")
    print("4. Scan for Broadlink devices")
    print("5. Scan for Chromecast devices")
    print("6. Scan for MQTT devices")
    print("7. Scan for Home Assistant devices")
    print("8. Scan for all devices")
    print("9. Instructions")
    print("0. Quit")

def show_instructions():
    """Display instructions for setting up the program."""
    print("\nInstructions:")
    print("1. Ensure you are connected to the network where devices are located.")
    print("2. When scanning for specific device types, be prepared to enter required information:")
    print("   - IP Address: Enter the IP address if prompted (e.g., for MQTT or Home Assistant).")
    print("   - API Token: For Home Assistant, you may need an API token. Generate this in Home Assistant settings.")
    print("3. Required Libraries:")
    print("   - Install all dependencies using 'pip install -r requirements.txt'.")
    print("   - Libraries include 'roku', 'pyHS100', 'pysnmp', 'requests', 'colorama', 'broadlink', 'pychromecast', 'paho-mqtt', and 'homeassistant'.")
    print("4. Follow on-screen prompts to interact with devices.")
    input("\nPress Enter to return to the main menu.")

def prompt_for_ip():
    """Prompt the user for an IP address."""
    return input("Enter the IP address of the device: ").strip()

def prompt_for_token():
    """Prompt the user for an API token."""
    return input("Enter the API token: ").strip()

def scan_for_devices(option):
    """Scan for devices based on user selection."""
    if option == "1":
        print("\nScanning for Roku devices...")
        devices = RokuDevice.discover()
    elif option == "2":
        print("\nScanning for TP-Link devices...")
        devices = TPLinkDevice.discover()
    elif option == "3":
        print("\nScanning for Printer devices...")
        devices = PrinterDevice.discover()
    elif option == "4":
        print("\nScanning for Broadlink devices...")
        devices = BroadlinkDevice.discover()
    elif option == "5":
        print("\nScanning for Chromecast devices...")
        devices = ChromecastDevice.discover()
    elif option == "6":
        print("\nScanning for MQTT devices...")
        broker_ip = prompt_for_ip()
        devices = MQTTDevice.discover(broker_ip)
    elif option == "7":
        print("\nScanning for Home Assistant devices...")
        hass_ip = prompt_for_ip()
        token = prompt_for_token()
        devices = HomeAssistantDevice.discover(hass_ip, token)
    elif option == "8":
        print("\nScanning for all devices...")
        devices = discover_all_devices()
    else:
        print("\nInvalid option. Please try again.")
        return []

    # Display results and ask to scan again or return to main menu
    if devices:
        print("\nDiscovered Devices:")
        for idx, device in enumerate(devices, start=1):
            print(f"{idx}. {device.__class__.__name__} at {device.ip}")
    else:
        print("\nNo devices found.")

    # Prompt for next action
    while True:
        choice = input("\nWould you like to (r)escan, or return to (m)ain menu? ").strip().lower()
        if choice == 'r':
            return scan_for_devices(option)  # Rescan for the same option
        elif choice == 'm':
            return devices
        else:
            print("Invalid choice. Please enter 'r' to rescan or 'm' to return to main menu.")
