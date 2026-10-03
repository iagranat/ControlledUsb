# Controlled USB 2.0 Extension Cable

An intelligent USB 2.0 High-Speed (480 Mbps) inline extension cable with host-controlled power & data disconnection.

---

## 🛠️ System Architecture

```
                  +-------------------------------------------------------------+
                  |                     USB DONGLE                              |
                  |                                                             |
USB-A Male ------>| ===> CH334F 2-Port USB Hub                                  |
(From PC)         |       |                                                     |
                  |       +-- Port 1 ----> Waveshare RP2040-Zero (USB CDC Serial|
                  |       |                (GP16 = Onboard WS2812 RGB LED)      |
                  |       |                         |                           |
                  |       |             GP14 (PWR)  | GP15 (DATA)               |
                  |       |             Active HIGH | Active LOW                |
                  |       |                         v                           |
                  |       +-- Port 2 --+-> [CH440G High-Speed Switch] (D+/D-) ->|---> USB-A Female
                  |                    |                                        |     (Target Device)
                  |                    +-> [TPS22918 Load Switch] (VBUS, 2A) -->|
                  |                                                             |
                  |   GND (Common ground throughout) -------------------------->|
                  +-------------------------------------------------------------+
```

---

## 📌 Pinout & Connections

### RP2040-Zero
| RP2040 Pin | Connected To | Description / Logic |
| :--- | :--- | :--- |
| **GP16** | *Onboard WS2812* | Status RGB LED (Green = ON, Red = OFF, Yellow = Cycling, Blue = Charge) |
| **GP14** | **TPS22918** `ON` | High-side power switch enable (Active **HIGH**: `1` = 5V ON, `0` = 0V OFF) |
| **GP15** | **CH440G** `EN` | USB data switch output enable (Active **LOW**: `0` = Pass, `1` = Cut) |
| **GP26** | **Push Button** | Tactile button to GND (Internal pull-up enabled) |

---

## 🚦 RGB Status Indications

| Color | State | $V_{BUS}$ (Power) | $D+/D-$ (Data) | Description |
| :--- | :---: | :---: | :---: | :--- |
| 🟢 **Green** | `CONNECTED` | **ON** | **ON** | Normal operation. |
| 🔴 **Red** | `DISCONNECTED`| **OFF** | **OFF** | Completely unpowered and un-enumerated. |
| 🔵 **Blue** | `CHARGE_ONLY` | **ON** | **OFF** | Safe charging without data communication. |
| 🟡 **Yellow** *(Blinking)* | `CYCLING` | *Rebooting* | *Rebooting* | Active reboot/cycle in progress. |

---

## 🕹️ Controls

### 1. Serial Commands (115200 baud, Newline)
* `ON` or `CONNECT` — Connect power and data (with safe sequencing).
* `OFF` or `DISCONNECT` — Disconnect data first, then cut power.
* `CHARGE` — Keep 5V active, cut data lines.
* `CYCLE <ms>` — Reboot port for specified milliseconds (e.g. `CYCLE 1500`).
* `STATUS` or `?` — Query current state.
* `HELP` — List commands.

### 2. Physical Button
* **Short Click (< 1.2s)**: Toggle between `CONNECTED` and `DISCONNECTED`.
* **Long Press (> 1.2s)**: Trigger automated 1-second power cycle (`CYCLE 1000`).

---

## 🚀 Building & Flashing with PlatformIO

1. Plug the **RP2040-Zero** into your PC while holding the **`BOOT`** button.
2. Open this folder in Antigravity IDE (with the PlatformIO extension installed).
3. Click the **Build** (`✓`) button in the bottom status bar.
4. Click the **Upload** (`→`) button to flash the firmware.
5. Click the **Serial Monitor** (`🔌`) button to open the terminal.

---

## 🐍 Python CLI Utility

Run from the `tools/` folder:
```powershell
python switch_cli.py on
python switch_cli.py off
python switch_cli.py cycle 1000
python switch_cli.py status
```
