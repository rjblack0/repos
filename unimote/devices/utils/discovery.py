from devices.roku_device import RokuDevice
from devices.tplink_device import TPLinkDevice
from devices.printer_device import PrinterDevice
from devices.rest_api_device import RESTAPIDevice

def discover_all_devices():
    device_classes = [RokuDevice, TPLinkDevice, PrinterDevice, RESTAPIDevice]
    all_devices = []
    for cls in device_classes:
        try:
            devices = cls.discover()
            all_devices.extend(devices)
        except Exception as e:
            print(f"Error discovering devices with {cls.__name__}: {e}")
    return all_devices
