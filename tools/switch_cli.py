"""
Controlled USB Switch - Host Python CLI Utility
Usage:
    python switch_cli.py on
    python switch_cli.py off
    python switch_cli.py charge
    python switch_cli.py cycle 1500
    python switch_cli.py status
"""

import sys
import time
import serial
import serial.tools.list_ports

def find_switch_port():
    """Auto-detects the RP2040 CDC Serial Port."""
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # Match Raspberry Pi / RP2040 VID (0x2E8A) or typical USB Serial strings
        if "2E8A" in port.hwid.upper() or "RP2040" in port.description.upper() or "USB SERIAL" in port.description.upper():
            return port.device
    if len(ports) > 0:
        return ports[0].device
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python switch_cli.py [on | off | charge | cycle <ms> | status]")
        sys.exit(1)

    command = " ".join(sys.argv[1:]).strip()
    port = find_switch_port()

    if not port:
        print("Error: Could not find any connected USB serial port.")
        sys.exit(1)

    print(f"Connecting to USB Switch on {port}...")
    try:
        with serial.Serial(port, 115200, timeout=1.5) as ser:
            time.sleep(0.1)
            ser.write((command + "\n").encode())
            time.sleep(0.2)
            while ser.in_waiting:
                line = ser.readline().decode("utf-8", errors="ignore").strip()
                if line:
                    print(f"  {line}")
    except Exception as e:
        print(f"Error communicating with device: {e}")

if __name__ == "__main__":
    main()
