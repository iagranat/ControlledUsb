import pcbnew
import os

def populate_aligned_board(pcb_path):
    board = pcbnew.LoadBoard(pcb_path)
    base_fp = 'C:/Users/iagra/AppData/Local/Programs/KiCad/10.0/share/kicad/footprints'
    
    # Clear old footprints
    for fp in list(board.GetFootprints()):
        board.Remove(fp)
        
    components = [
        # Designator, Value, FootprintLib, FootprintName, X (mm), Y (mm), Rotation (deg)
        # J1: USB-A Male Plug:
        # Reference edge X=100.0 (left board edge), Center Y=109.5, rot=180
        ("J1", "USB_A_Male", "Connector_USB.pretty", "USB_A_CNCTech_1001-011-01101_Horizontal", 100.0, 109.5, 180),
        
        # Upstream Protection & Power (X = 111 to 115)
        ("F1", "PTC 2A", "Fuse.pretty", "Fuse_1206_3216Metric", 111.0, 103.5, 0),
        ("U7", "USBLC6-2SC6", "Package_TO_SOT_SMD.pretty", "SOT-23-6", 111.0, 115.5, 0),
        ("C13", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 113.5, 103.5, 90),
        ("C3", "100nF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 113.5, 106.0, 90),
        
        # 3.3V LDO Regulator (X = 114)
        ("U6", "ME6211C33", "Package_TO_SOT_SMD.pretty", "SOT-23-5", 114.0, 115.5, 180),
        ("C14", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 116.5, 115.5, 90),
        ("C15", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 116.5, 103.5, 90),
        
        # WCH CH334F High-Speed USB Hub (X = 118.5)
        ("U3", "CH334F", "Package_DFN_QFN.pretty", "QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm", 118.5, 109.5, 0),
        ("Y2", "12.000MHz", "Crystal.pretty", "Crystal_SMD_3225-4Pin_3.2x2.5mm", 118.5, 115.5, 0),
        ("C4", "100nF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 116.5, 107.0, 0),
        ("C5", "100nF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 121.0, 104.5, 90),
        ("C11", "1uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 121.0, 114.5, 90),
        
        # RP2040 USB series termination resistors (X = 122.5)
        ("R1", "27R", "Resistor_SMD.pretty", "R_0603_1608Metric", 122.5, 108.5, 0),
        ("R2", "27R", "Resistor_SMD.pretty", "R_0603_1608Metric", 122.5, 110.5, 0),
        
        # Raspberry Pi RP2040 MCU (X = 127.5)
        ("U1", "RP2040", "Package_DFN_QFN.pretty", "QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm", 127.5, 109.5, 0),
        ("Y1", "12.000MHz", "Crystal.pretty", "Crystal_SMD_3225-4Pin_3.2x2.5mm", 127.5, 116.0, 0),
        ("C1", "15pF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 124.5, 116.0, 90),
        ("C2", "15pF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 130.5, 116.0, 90),
        
        # User Tactile Button on top edge (X = 127.5, Y = 102.5)
        ("SW1", "USER_BTN", "Button_Switch_SMD.pretty", "SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS", 127.5, 102.5, 0),
        # BOOT & RESET buttons
        ("SW2", "BOOT", "Button_Switch_SMD.pretty", "SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS", 122.0, 116.5, 0),
        ("SW3", "RESET", "Button_Switch_SMD.pretty", "SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS", 133.0, 116.5, 0),
        
        # SPI Flash (X = 134.5) & Status RGB LED (X = 134.5)
        ("U2", "W25Q32", "Package_SO.pretty", "SOIC-8_3.9x4.9mm_P1.27mm", 134.5, 105.0, 0),
        ("D1", "WS2812B", "LED_SMD.pretty", "LED_WS2812B-2020_PLCC4_2.0x2.0mm", 134.5, 112.5, 0),
        
        # Power & Data Switches (X = 138.5)
        ("U4", "TPS22918", "Package_TO_SOT_SMD.pretty", "SOT-23-6", 138.5, 104.5, 0),
        ("R5", "10k", "Resistor_SMD.pretty", "R_0603_1608Metric", 138.5, 107.5, 0),
        ("U5", "CH440P", "Package_SO.pretty", "TSSOP-16_4.4x5mm_P0.65mm", 138.5, 114.5, 0),
        ("R6", "10k", "Resistor_SMD.pretty", "R_0603_1608Metric", 138.5, 111.0, 0),
        
        # Downstream Bulk Cap
        ("C17", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 135.5, 108.5, 90),
        
        # J2: USB-A Female Receptacle:
        # Rotated 90 deg so opening faces right (+X).
        # Placed at X = 145.0, Y = 113.0 -> Perfectly centers at Y = 109.5, front flush with board edge!
        ("J2", "USB_A_Female", "Connector_USB.pretty", "USB_A_Molex_67643_Horizontal", 145.0, 113.0, 90)
    ]
    
    for ref, val, lib, name, x, y, rot in components:
        lib_path = os.path.join(base_fp, lib)
        fp = pcbnew.FootprintLoad(lib_path, name)
        if not fp:
            print(f"Warning: Could not load {name}")
            continue
        fp.SetReference(ref)
        fp.SetValue(val)
        fp.SetPosition(pcbnew.VECTOR2I(int(x * 1e6), int(y * 1e6)))
        fp.SetOrientation(pcbnew.EDA_ANGLE(rot, pcbnew.DEGREES_T))
        board.Add(fp)
        
    pcbnew.SaveBoard(pcb_path, board)
    print("Perfect placement complete! Saved to:", pcb_path)

if __name__ == "__main__":
    populate_aligned_board("d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb")
