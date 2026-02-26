# JN_PAD — 12-Key Macro Pad

A compact 3×4 hot-swappable mechanical macro pad powered by the **Raspberry Pi Pico 2 (RP2350)**, designed in KiCad 7+.

---

## Features

- **12 keys** (3 columns × 4 rows matrix)
- **Hot-swappable** Kailh MX sockets — swap switches without soldering
- **Cherry MX compatible** switches (linear / tactile / clicky — user choice)
- **Raspberry Pi Pico 2 (RP2350)** microcontroller
- **KMK firmware** (CircuitPython-based, highly customisable)
- Anti-ghosting 1N4148 diodes (COL2ROW orientation)
- SMD diodes and sockets on back side (B.Cu)
- 2-layer PCB, 1.6 mm FR4
- M2 mounting holes at corners for case integration

---

## Photo / Diagram Placeholder

```
┌───────────────────────┐
│  [ SW1 ] [ SW2 ] [ SW3 ] │
│  [ SW4 ] [ SW5 ] [ SW6 ] │
│  [ SW7 ] [ SW8 ] [ SW9 ] │
│  [SW10 ] [SW11 ] [SW12 ] │
│                           │
│      [ Pico 2 ]           │
│          USB-C ↓          │
└───────────────────────┘
```

---

## Project Structure

```
JN_PAD/
├── README.md
├── firmware/
│   ├── code.py          ← KMK firmware for the macropad
│   └── boot.py          ← CircuitPython boot config
├── pcb/
│   ├── JN_PAD.kicad_pro ← KiCad 7+ project file
│   ├── JN_PAD.kicad_sch ← KiCad schematic
│   ├── JN_PAD.kicad_pcb ← KiCad PCB layout
│   └── fp-lib-table     ← Footprint library table referencing MX_V2
├── docs/
│   ├── bom.csv                 ← Bill of materials
│   ├── schematic.txt           ← Human-readable schematic description
│   └── pcb-layout-guide.txt    ← PCB layout placement guide
└── libraries/           ← Clone MX_V2 here (see Setup)
```

---

## Setup

### 1. Clone the MX_V2 Footprint Library

The PCB uses the [ai03-2725/MX_V2](https://github.com/ai03-2725/MX_V2) footprint library for hot-swap switch sockets.

```bash
git clone https://github.com/ai03-2725/MX_V2.git libraries/MX_V2
```

### 2. Copy 3D Models (Optional)

For 3D view in KiCad, copy the 3D model files:

```bash
cp -r libraries/MX_V2/3D/ pcb/
```

### 3. Open in KiCad

Open `pcb/JN_PAD.kicad_pro` in **KiCad 7 or later**.

> **Note:** The `fp-lib-table` references the MX_V2 library via  
> `${KIPRJMOD}/../libraries/MX_V2/MX_Hotswap.pretty`.  
> Make sure you have cloned the library as described above before opening the project.

---

## Firmware

### Requirements

- [CircuitPython](https://circuitpython.org/) for Raspberry Pi Pico 2
- [KMK Firmware](https://github.com/KMKfw/kmk_firmware)

### Flashing

1. **Install CircuitPython** on the Pico 2:
   - Download the Pico 2 UF2 image from [circuitpython.org](https://circuitpython.org/board/raspberry_pi_pico2/)
   - Hold BOOTSEL while plugging in USB, then drag the UF2 to the `RPI-RP2` drive.

2. **Install KMK**:
   - Download the latest KMK release from [github.com/KMKfw/kmk_firmware](https://github.com/KMKfw/kmk_firmware/releases)
   - Copy the `kmk/` folder to the root of the `CIRCUITPY` drive.

3. **Copy firmware**:
   ```bash
   cp firmware/code.py /path/to/CIRCUITPY/
   cp firmware/boot.py /path/to/CIRCUITPY/
   ```

---

## Pin Mapping

| Function | GPIO | Pico 2 Pin |
|----------|------|------------|
| COL0     | GP2  | Pin 4      |
| COL1     | GP3  | Pin 5      |
| COL2     | GP4  | Pin 6      |
| ROW0     | GP6  | Pin 9      |
| ROW1     | GP7  | Pin 10     |
| ROW2     | GP8  | Pin 11     |
| ROW3     | GP9  | Pin 12     |

---

## Bill of Materials (Summary)

| Component                  | Qty | Notes                          |
|----------------------------|-----|--------------------------------|
| Raspberry Pi Pico 2        | 1   | RP2350, mounted on B.Cu        |
| Kailh MX Hot-Swap Socket   | 12  | SMD, B.Cu                      |
| 1N4148 Diode (SOD-123)     | 12  | Anti-ghosting, SMD             |
| Pin Header 1×20 (2.54mm)   | 2   | For Pico 2 mounting            |
| Cherry MX switches         | 12  | User choice                    |
| 1U MX keycaps              | 12  | Any MX-compatible profile      |
| M2×6mm Standoffs           | 4   | PCB/case mounting              |
| M2 Screws                  | 8   | Top and bottom fastening       |

See [`docs/bom.csv`](docs/bom.csv) for the full bill of materials.

---

## License

This project is released under the [MIT License](LICENSE).

---

## Credits

- Switch footprints: [ai03-2725/MX_V2](https://github.com/ai03-2725/MX_V2) — `MX_Hotswap.pretty` / `MX_Hotswap-1U`
- Firmware: [KMKfw/kmk_firmware](https://github.com/KMKfw/kmk_firmware)
