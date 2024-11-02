# Unimote


## 0.1.001

Added the following to requirements.py
broadlink - For broadlink smart devices (IR/RF remotes)
pychromecast - For controlling chromecast
paho-mqtt - MQTT (IoT) support
homeassistant - Home assistant support.

Not implemented into code, delete from discovery.py if you want to implement

## Overview

This program allows you to discover and control various devices on your local network, such as Roku TVs, TP-Link Smart Plugs, network printers, and other devices with REST API support.

## Features

- Discover network devices
- Control Roku TVs, TP-Link smart plugs, and SNMP-enabled printers
- Support for additional devices with REST APIs
- Modular design for easy extensibility

## Installation

1. Clone the repository.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt

## Extending the Program

- To add support for a new device:
1. Create a new file in the devices/ directory
2. Implement the NetworkDevice interface
   2.1 Implement new _device.py
   2.2 Implement in requirements.txt
3. Update discovery.py to include the new device class in the discovery process

## Kali Linux

Instructions to install requirements.txt using Kali

Bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   deactivate