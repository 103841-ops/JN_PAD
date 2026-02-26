"""
CircuitPython boot configuration for JN_PAD macropad.

This file runs before code.py on every power-up / reset.
It exposes the device as a standard USB HID keyboard.
"""

import usb_hid

# Enable standard HID devices (keyboard + mouse + consumer control)
usb_hid.enable((usb_hid.Device.KEYBOARD, usb_hid.Device.MOUSE, usb_hid.Device.CONSUMER_CONTROL))
