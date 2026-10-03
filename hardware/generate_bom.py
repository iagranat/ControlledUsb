import csv
import os

def generate_jlcpcb_bom(filepath):
    # JLCPCB Standard BOM Format:
    # Comment, Designator, Footprint, LCSC Part #
    bom_entries = [
        {"Comment": "RP2040 (Dual-Core Cortex-M0+ MCU)", "Designator": "U1", "Footprint": "QFN-56_7x7mm_P0.4mm", "LCSC": "C2040"},
        {"Comment": "W25Q32JVSSIQ (4MB SPI Flash)", "Designator": "U2", "Footprint": "SOIC-8_3.9x4.9mm_P1.27mm", "LCSC": "C7405788"},
        {"Comment": "CH334F (USB 2.0 High-Speed 4-Port Hub)", "Designator": "U3", "Footprint": "QFN-24_4x4mm_P0.5mm", "LCSC": "C5142940"},
        {"Comment": "TPS22918DBVR (5V 2A Load Switch with QOD)", "Designator": "U4", "Footprint": "SOT-23-6", "LCSC": "C2835607"},
        {"Comment": "CH440P (High-Speed USB Analog Switch)", "Designator": "U5", "Footprint": "TSSOP-16_4.4x5.0mm_P0.65mm", "LCSC": "C53407"},
        {"Comment": "ME6211C33M5G-N (3.3V 500mA LDO)", "Designator": "U6", "Footprint": "SOT-23-5", "LCSC": "C82942"},
        {"Comment": "USBLC6-2SC6 (USB ESD Protection)", "Designator": "U7", "Footprint": "SOT-23-6", "LCSC": "C7519"},
        {"Comment": "USBLC6-2SC6 (USB ESD Protection)", "Designator": "U8", "Footprint": "SOT-23-6", "LCSC": "C7519"},
        {"Comment": "WS2812B-2020 (Addressable RGB LED)", "Designator": "D1", "Footprint": "LED_2020_2.0x2.0mm", "LCSC": "C2843785"},
        {"Comment": "12.000MHz SMD Crystal", "Designator": "Y1", "Footprint": "Crystal_SMD_3225-4P_3.2x2.5mm", "LCSC": "C16212"},
        {"Comment": "12.000MHz SMD Crystal", "Designator": "Y2", "Footprint": "Crystal_SMD_3225-4P_3.2x2.5mm", "LCSC": "C16212"},
        {"Comment": "Tactile Button (User Button GP26)", "Designator": "SW1", "Footprint": "SW_SPST_3x4x2.5mm_SMD", "LCSC": "C318884"},
        {"Comment": "Tactile Button (BOOT Button)", "Designator": "SW2", "Footprint": "SW_SPST_3x4x2.5mm_SMD", "LCSC": "C318884"},
        {"Comment": "Tactile Button (RESET Button)", "Designator": "SW3", "Footprint": "SW_SPST_3x4x2.5mm_SMD", "LCSC": "C318884"},
        {"Comment": "PTC Resettable Fuse 2A 6V", "Designator": "F1", "Footprint": "Fuse_1206_3216Metric", "LCSC": "C394336"},
        {"Comment": "USB-A Male Plug SMD+TH", "Designator": "J1", "Footprint": "USB_A_Male_SMD_TH", "LCSC": "C77873"},
        {"Comment": "USB-A Female Receptacle RA TH", "Designator": "J2", "Footprint": "USB_A_Female_Horizontal", "LCSC": "C10398"},
        
        # Resistors
        {"Comment": "27R 1% 0603", "Designator": "R1, R2", "Footprint": "R_0603_1608Metric", "LCSC": "C25114"},
        {"Comment": "10k 1% 0603", "Designator": "R5, R6, R8", "Footprint": "R_0603_1608Metric", "LCSC": "C25804"},
        {"Comment": "1k 1% 0603", "Designator": "R7", "Footprint": "R_0603_1608Metric", "LCSC": "C21190"},
        
        # Capacitors
        {"Comment": "15pF 50V C0G 0603", "Designator": "C1, C2", "Footprint": "C_0603_1608Metric", "LCSC": "C1644"},
        {"Comment": "100nF 50V X7R 0603", "Designator": "C3, C4, C5, C6, C7, C8, C9, C10", "Footprint": "C_0603_1608Metric", "LCSC": "C14663"},
        {"Comment": "1uF 50V X7R 0603", "Designator": "C11, C12", "Footprint": "C_0603_1608Metric", "LCSC": "C15849"},
        {"Comment": "10uF 16V X5R 0603", "Designator": "C13, C14, C15, C16", "Footprint": "C_0603_1608Metric", "LCSC": "C19702"}
    ]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Comment", "Designator", "Footprint", "LCSC Part #"])
        writer.writeheader()
        for row in bom_entries:
            writer.writerow({
                "Comment": row["Comment"],
                "Designator": row["Designator"],
                "Footprint": row["Footprint"],
                "LCSC Part #": row["LCSC"]
            })
    print(f"Generated JLCPCB BOM: {filepath}")

if __name__ == "__main__":
    generate_jlcpcb_bom("d:/Projects/ControlledUsb/hardware/BOM_JLCPCB.csv")
