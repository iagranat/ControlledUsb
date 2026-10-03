import pcbnew
import os

def populate_board(pcb_path):
    board = pcbnew.LoadBoard(pcb_path)
    base_fp = 'C:/Users/iagra/AppData/Local/Programs/KiCad/10.0/share/kicad/footprints'
    
    components = [
        # Designator, Value, FootprintLib, FootprintName, X (mm), Y (mm), Rotation (deg)
        ("J1", "USB_A_Male", "Connector_USB.pretty", "USB_A_CNCTech_1001-011-01101_Horizontal", 102.0, 109.5, 180),
        ("F1", "PTC 2A", "Fuse.pretty", "Fuse_1206_3216Metric", 108.0, 104.5, 90),
        ("U7", "USBLC6-2SC6", "Package_TO_SOT_SMD.pretty", "SOT-23-6", 108.0, 114.5, 0),
        ("C13", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 110.5, 104.5, 0),
        ("C3", "100nF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 110.5, 107.0, 0),
        ("U6", "ME6211C33", "Package_TO_SOT_SMD.pretty", "SOT-23-5", 113.5, 104.0, 0),
        ("C14", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 113.5, 107.0, 0),
        ("C15", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 113.5, 109.0, 0),
        
        ("U3", "CH334F", "Package_DFN_QFN.pretty", "QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm", 119.0, 109.5, 0),
        ("Y2", "12.000MHz", "Crystal.pretty", "Crystal_SMD_3225-4Pin_3.2x2.5mm", 119.0, 115.5, 0),
        ("C4", "100nF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 116.5, 106.0, 90),
        ("C5", "100nF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 121.5, 106.0, 90),
        ("C11", "1uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 121.5, 113.0, 90),
        ("C16", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 116.5, 113.0, 90),
        
        ("R1", "27R", "Resistor_SMD.pretty", "R_0603_1608Metric", 124.0, 108.0, 0),
        ("R2", "27R", "Resistor_SMD.pretty", "R_0603_1608Metric", 124.0, 110.0, 0),
        
        ("U1", "RP2040", "Package_DFN_QFN.pretty", "QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm", 130.0, 109.5, 0),
        ("Y1", "12.000MHz", "Crystal.pretty", "Crystal_SMD_3225-4Pin_3.2x2.5mm", 130.0, 116.0, 0),
        ("C1", "15pF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 127.5, 116.0, 90),
        ("C2", "15pF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 132.5, 116.0, 90),
        
        ("SW1", "USER_BTN", "Button_Switch_SMD.pretty", "SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS", 130.0, 102.5, 0),
        ("SW2", "BOOT", "Button_Switch_SMD.pretty", "SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS", 124.0, 116.5, 0),
        ("SW3", "RESET", "Button_Switch_SMD.pretty", "SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS", 136.0, 116.5, 0),
        
        ("U2", "W25Q32", "Package_SO.pretty", "SOIC-8_3.9x4.9mm_P1.27mm", 137.5, 105.0, 0),
        ("D1", "WS2812B", "LED_SMD.pretty", "LED_WS2812B-2020_PLCC4_2.0x2.0mm", 137.0, 112.5, 0),
        
        ("U4", "TPS22918", "Package_TO_SOT_SMD.pretty", "SOT-23-6", 143.0, 105.0, 0),
        ("R5", "10k", "Resistor_SMD.pretty", "R_0603_1608Metric", 140.5, 102.5, 90),
        ("U5", "CH440P", "Package_SO.pretty", "TSSOP-16_4.4x5mm_P0.65mm", 143.0, 112.5, 0),
        ("R6", "10k", "Resistor_SMD.pretty", "R_0603_1608Metric", 140.5, 116.5, 90),
        
        ("U8", "USBLC6-2SC6", "Package_TO_SOT_SMD.pretty", "SOT-23-6", 147.5, 113.0, 0),
        ("C17", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 147.5, 105.0, 0),
        ("J2", "USB_A_Female", "Connector_USB.pretty", "USB_A_Molex_67643_Horizontal", 152.0, 109.5, 0)
    ]
    
    # Remove any existing footprints
    for fp in list(board.GetFootprints()):
        board.Remove(fp)
        
    for ref, val, lib, name, x, y, rot in components:
        lib_path = os.path.join(base_fp, lib)
        fp = pcbnew.FootprintLoad(lib_path, name)
        if not fp:
            print(f"Warning: Could not load {name}")
            continue
        fp.SetReference(ref)
        fp.SetValue(val)
        fp.SetPosition(pcbnew.VECTOR2I(int(x * 1000000), int(y * 1000000)))
        fp.SetOrientation(pcbnew.EDA_ANGLE(rot, pcbnew.DEGREES_T))
        board.Add(fp)
        print(f"Placed {ref} ({val}) at ({x}, {y})")
        
    pcbnew.SaveBoard(pcb_path, board)
    print("All components placed and board saved successfully!")

if __name__ == "__main__":
    populate_board("d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb")
