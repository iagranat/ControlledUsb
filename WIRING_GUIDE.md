# 🔌 Breadboard Wiring & Assembly Guide (Verified Working)

This guide details the exact, lab-verified breadboard wiring connections for **USBiagra** / **The Ilan-terrupter**.

---

## 📦 Components Overview

1. **CH334F 2-Port USB 2.0 Hub Breakout**
   * Upstream USB-C connects to PC Host.
   * `PORT1` (Top): Connects to RP2040-Zero (USB CDC Serial Controller).
   * `PORT2` (Bottom): Connects to Switched Downstream Port via TPS22918 & CH440G.
2. **Waveshare RP2040-Zero**
   * Firmware running Arduino/PlatformIO with USB CDC CLI, debounced button state machine, and NeoPixel status.
3. **CH440G USB 2.0 High-Speed Switch (SOP-16 Adapter)**
   * Switches differential data pair ($D+$ on Channel A, $D-$ on Channel D).
4. **TPS22918 Power Load Switch (SOT-23-6 DBV Adapter)**
   * Switches 5V $V_{BUS}$ up to 2A with Quick Output Discharge (QOD).
5. **USB-A Female Breakout**
   * Target downstream port.
6. **Push Button**
   * Connected between `GP26` and `GND`.

---

## 🗺️ Pin-to-Pin Connection Table

### 1. Power & Ground Rails
* **Hub `5V`** $\rightarrow$ **Breadboard Red (+) Rail**
* **Hub `GND`** $\rightarrow$ **Breadboard Blue (-) Rail**
* **All Grounds** (Hub, RP2040-Zero, CH440G Pin 8, TPS22918 Pin 2, USB-A Female GND) must tie to this common ground rail.

---

### 2. Hub Port 1 $\rightarrow$ RP2040-Zero (USB Serial CLI Control)
Using a 4-wire USB-C cable (plugged into RP2040-Zero USB-C receptacle) or direct wire:
* 🔴 **Red (5V)** $\rightarrow$ Hub Port 1 `5V` (or Breadboard 5V rail)
* ⚫ **Black (GND)** $\rightarrow$ Hub Port 1 `GND` (or Breadboard GND rail)
* 🟢 **Green (D+)** $\rightarrow$ Hub Port 1 `D+`
* ⚪ **White (D-)** $\rightarrow$ Hub Port 1 `D-`

---

### 3. CH440G Data Switch (SOP-16 Adapter) — *Verified Channels*
The CH440G switches the USB $D+/D-$ differential pair using Channel A and Channel D:

| CH440G Pin | Function | Connect To | Notes |
| :---: | :--- | :--- | :--- |
| **Pin 1** | `IN` | **GND Rail** | Selects Channel S1 (Low = S1 active) |
| **Pin 2** | `S1A` ($D+$ out) | **USB-A Female `D+`** | Switched $D+$ output to downstream port |
| **Pin 4** | `DA` ($D+$ in) | **Hub Port 2 `D+`** | High-speed $D+$ input from Hub |
| **Pin 8** | `GND` | **GND Rail** | System ground |
| **Pin 12** | `DD` ($D-$ in) | **Hub Port 2 `D-`** | High-speed $D-$ input from Hub |
| **Pin 14** | `S1D` ($D-$ out) | **USB-A Female `D-`** | Switched $D-$ output to downstream port |
| **Pin 15** | `EN#` | **RP2040 `GP15`** | Active LOW enable (0 = Pass, 1 = Tri-state). Add 10k pull-down to GND. |
| **Pin 16** | `VCC` | **5V Rail** | Chip power (place 0.1µF ceramic cap between Pin 16 and GND) |

*(Pins 3, 5, 6, 7, 9, 10, 11, 13 are unused/isolated).*

---

### 4. TPS22918 Power Switch (SOT-23-6 DBV Adapter) — *Verified Pinout*
Controls 5V $V_{BUS}$ power line up to 2A with active discharge:

| TPS22918 Pin | Function | Connect To | Notes |
| :---: | :--- | :--- | :--- |
| **Pin 1** | `VIN` | **Breadboard 5V Rail** | 5V Input from Hub. Add 1µF–10µF bulk capacitor to GND. |
| **Pin 2** | `GND` | **GND Rail** | System ground |
| **Pin 3** | `ON` | **RP2040 `GP14`** | Active HIGH enable (1 = 5V ON, 0 = 0V OFF). Add 10k pull-up to 5V. |
| **Pin 4** | `CT` | *Leave Floating* | Slew rate capacitor (internal fast ~100µs ramp) |
| **Pin 5** | `QOD` | **Tie to Pin 6 (`VOUT`)** | Quick Output Discharge (bleeds downstream rail to 0V when OFF) |
| **Pin 6** | `VOUT` | **USB-A Female `VBUS`** | Switched 5V output to downstream port |

---

### 5. Downstream Extension Port (USB-A Female Breakout)
* **`VBUS`** $\rightarrow$ From TPS22918 **Pin 6 (`VOUT`)**
* **`D-`** $\rightarrow$ From CH440G **Pin 14 (`S1D`)**
* **`D+`** $\rightarrow$ From CH440G **Pin 2 (`S1A`)**
* **`GND`** $\rightarrow$ Common **GND Rail**

---

### 6. Physical Controls & RP2040 Pin Assignment
* **`GP14`** $\rightarrow$ TPS22918 Pin 3 (`ON`)
* **`GP15`** $\rightarrow$ CH440G Pin 15 (`EN#`)
* **`GP26`** $\rightarrow$ Push button (other terminal to `GND`)
* **`GP16`** $\rightarrow$ Onboard WS2812 RGB LED:
  * 🟢 **Solid Green**: Connected (Power ON, Data ON)
  * 🔴 **Solid Red**: Disconnected (Power OFF, Data OFF)
  * 🔵 **Solid Blue**: Charge Only (Power ON, Data OFF)
  * 🟡 **Blinking Yellow**: Power Cycling (Auto reboot)

---

## ⚡ High-Speed (480 Mbps) Wiring Guidelines

When testing high-speed devices (flash drives, SSDs, webcams) on breadboard:
1. **Short Length**: Keep $D+$ and $D-$ wire runs as short as possible (~3 to 5 cm max).
2. **Length Match**: Cut the $D+$ and $D-$ wires to the identical length (within 2-3 mm).
3. **Twisted Pairs**: Lightly twist the Hub $D+/D-$ pair together, and the USB-A Female $D+/D-$ pair together to preserve 90Ω differential impedance.
4. **Direct Ground Return**: Ensure the USB-A Female GND wire runs directly to the common ground rail adjacent to the signal wires.
