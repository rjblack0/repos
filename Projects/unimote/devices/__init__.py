# devices/__init__.py

from .roku_device import RokuDevice
from .tplink_device import TPLinkDevice
from .printer_device import PrinterDevice
from .rest_api_device import RESTAPIDevice
from .broadlink_device import BroadlinkDevice
from .chromecast_device import ChromecastDevice
from .mqtt_device import MQTTDevice
from .home_assistant_device import HomeAssistantDevice
from .smart_tv_device import SmartTVDevice
from .computer_device import ComputerDevice
from .phone_device import PhoneDevice
from .ip_camera_device import IPCameraDevice  # Add this line

__all__ = [
    "RokuDevice", "TPLinkDevice", "PrinterDevice", "RESTAPIDevice",
    "BroadlinkDevice", "ChromecastDevice", "MQTTDevice", "HomeAssistantDevice",
    "SmartTVDevice", "ComputerDevice", "PhoneDevice", "IPCameraDevice"  # Add these devices to the list
]
