"""
Raspberry Pi Pico 2 — JN_PAD 12-Key Macropad Firmware
Framework: KMK (CircuitPython-based keyboard firmware)
PCB Library: ai03-2725/MX_V2 (MX_Hotswap-1U footprints)
"""

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

# Pin definitions matching PCB schematic
keyboard.col_pins = (board.GP2, board.GP3, board.GP4)
keyboard.row_pins = (board.GP6, board.GP7, board.GP8, board.GP9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Layers module
layers = Layers()
keyboard.modules.append(layers)

# Keymap: 3 columns × 4 rows = 12 keys
# Layer 0: F13–F24 (ideal for macro mapping in host software)
keyboard.keymap = [
    [
        KC.F13,   KC.F14,   KC.F15,     # Row 0: SW1,  SW2,  SW3
        KC.F16,   KC.F17,   KC.F18,     # Row 1: SW4,  SW5,  SW6
        KC.F19,   KC.F20,   KC.F21,     # Row 2: SW7,  SW8,  SW9
        KC.F22,   KC.F23,   KC.F24,     # Row 3: SW10, SW11, SW12
    ],
]

if __name__ == '__main__':
    keyboard.go()
