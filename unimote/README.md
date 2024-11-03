# Unimote
Version 0.2
- Program is not in a functioning state

## 0.2.011

Menu is functional, device and IP discovery is not.

## 0.1.002

UI/UX improvements
- Implemented menu
- Capability to select which devices to scan for

## 0.1.001

Added support for
- broadlink - For broadlink smart devices (IR/RF remotes)
- pychromecast - For controlling chromecast
- paho-mqtt - MQTT (IoT) support
- homeassistant - Home assistant support.

## Overview

Unimote is a network device control program designed for home use, enabling users to discover and interact with various smart devices on their local network. It supports a range of devices, including Roku, TP-Link, Broadlink, Chromecast, and more. It also includes a feature for scanning specific IP addresses for reachability.

Please use this software responsibly and only on networks that you own or have explicit permission to access. Unauthorized network scanning or device control may violate laws or policies.

## Features

Discover and interact with a variety of smart devices on the local network:
-Roku
   -TP-Link devices
   -Printers (SNMP)
   -Broadlink devices
   -Chromecast
   -MQTT devices
   -Home Assistant devices
   -Smart TVs
   -Computers
   -Phones
   -IP Cameras
- Customizable IP address scanning for specific addresses on your network.
- User-friendly CLI with nested menu navigation.
- Device-specific command execution (e.g., toggling lights on Home Assistant, publishing messages via MQTT).

## Requirements
Python 3.7 or higher
The following Python libraries (listed in requirements.txt):
- colorama
- paho-mqtt
- requests
- broadlink
- pychromecast
- homeassistant
- roku
- pyHS100
- pysnmp

## Installation

1. Clone the repository.

2. Isolate Dependencies
   ```bash
   python3 -m venv env
   env\Scripts\activate       //For Windows
   source env/bin/activate    //For MacOS/Linux

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt

## Configuration

The program requires a config.json file to specify IP addresses for network scanning. Place config.json in the root directory of the project (the same location as main.py).

## Usage

The program will prompt you to agree to an agreement regarding responsible use. This program is intended for home networks only.

After agreeing, the main menu will display options:

- Discover All Devices: Scans the network for all supported devices and displays a summary.
- Scan for Smart Devices: Displays a submenu where you can scan for specific types of smart devices.
- Scan for Computers: Scans for computers on the network.
- Scan for Phones: Scans for phones on the network.
- Scan IP Addresses: Checks the reachability of IPs listed in config.json.
- Instructions: Displays setup and usage instructions.
- Quit: Exits the program.

After discovering devices, you can select a device from the list and access additional commands for controlling the device.

## Supported Devices
Smart Devices

- Roku
- TP-Link Smart Devices
- Printers (SNMP-based)
- Broadlink Devices
- Chromecast
- MQTT Devices
- Home Assistant-connected Devices
- Smart TVs
- Other Devices

- Computers
- Phones
- IP Cameras

## Features
- Network Scanning: Detects and lists compatible devices on the local network.
- Device Control: Allows for device-specific commands such as toggling lights (Home Assistant), publishing MQTT messages, and more.
- IP Address Reachability: Verifies if specific IP addresses are reachable, based on the config.json configuration.

## Known Issues

- Some devices may not respond as expected depending on network configuration or firewall settings.
- The current implementation of scan_ip_addresses relies on system ping and may need administrator privileges.
- Home Assistant and MQTT devices require IP addresses and API tokens to function properly.