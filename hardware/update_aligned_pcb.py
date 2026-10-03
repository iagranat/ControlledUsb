import pcbnew
import os

def update_pcb(pcb_path):
    # Board dimensions: 60mm long x 19mm wide
    # Left edge: X = 100.0, Right edge: X = 160.0
    # Top edge: Y = 100.0, Bottom edge: Y = 119.0
    # Centerline: Y = 109.5
    x0 = 100.0
    y0 = 100.0
    w = 60.0
    h = 19.0
    r = 1.5  # 1.5mm rounded corner radius
    
    board = pcbnew.LoadBoard(pcb_path)
    base_fp = 'C:/Users/iagra/AppData/Local/Programs/KiCad/10.0/share/kicad/footprints'
    
    # 1. Update Edge.Cuts and silkscreen drawings
    for d in list(board.GetDrawings()):
        layer = d.GetLayerName()
        if layer in ["Edge.Cuts", "F.SilkS", "B.SilkS"]:
            board.Remove(d)
            
    # Add Edge.Cuts lines and arcs
    def add_line(sx, sy, ex, ey):
        line = pcbnew.PCB_SHAPE(board)
        line.SetShape(pcbnew.SHAPE_T_SEGMENT)
        line.SetLayer(pcbnew.Edge_Cuts)
        line.SetWidth(int(0.15 * 1e6))
        line.SetStart(pcbnew.VECTOR2I(int(sx * 1e6), int(sy * 1e6)))
        line.SetEnd(pcbnew.VECTOR2I(int(ex * 1e6), int(ey * 1e6)))
        board.Add(line)

    def add_arc(cx, cy, start_angle, end_angle):
        arc = pcbnew.PCB_SHAPE(board)
        arc.SetShape(pcbnew.SHAPE_T_ARC)
        arc.SetLayer(pcbnew.Edge_Cuts)
        arc.SetWidth(int(0.15 * 1e6))
        arc.SetCenter(pcbnew.VECTOR2I(int(cx * 1e6), int(cy * 1e6)))
        # Arc with radius r
        import math
        sa = math.radians(start_angle)
        ea = math.radians(end_angle)
        sx = cx + r * math.cos(sa)
        sy = cy + r * math.sin(sa)
        ex = cx + r * math.cos(ea)
        ey = cy + r * math.sin(ea)
        mid_angle = math.radians((start_angle + end_angle) / 2)
        mx = cx + r * math.cos(mid_angle)
        my = cy + r * math.sin(mid_angle)
        arc.SetArcGeometry(pcbnew.VECTOR2I(int(sx * 1e6), int(sy * 1e6)),
                           pcbnew.VECTOR2I(int(mx * 1e6), int(my * 1e6)),
                           pcbnew.VECTOR2I(int(ex * 1e6), int(ey * 1e6)))
        board.Add(arc)

    # 4 straight edges
    add_line(x0 + r, y0, x0 + w - r, y0)             # Top edge
    add_line(x0 + w, y0 + r, x0 + w, y0 + h - r)     # Right edge
    add_line(x0 + w - r, y0 + h, x0 + r, y0 + h)     # Bottom edge
    add_line(x0, y0 + h - r, x0, y0 + r)             # Left edge
    
    # 4 rounded corners
    add_arc(x0 + w - r, y0 + r, 270, 360)            # Top-right
    add_arc(x0 + w - r, y0 + h - r, 0, 90)           # Bottom-right
    add_arc(x0 + r, y0 + h - r, 90, 180)             # Bottom-left
    add_arc(x0 + r, y0 + r, 180, 270)                # Top-left

    # Silkscreen text
    def add_text(txt, tx, ty, rot=0, size=1.0, layer=pcbnew.F_SilkS):
        text = pcbnew.PCB_TEXT(board)
        text.SetText(txt)
        text.SetLayer(layer)
        text.SetPosition(pcbnew.VECTOR2I(int(tx * 1e6), int(ty * 1e6)))
        text.SetTextSize(pcbnew.VECTOR2I(int(size * 1e6), int(size * 1e6)))
        text.SetTextThickness(int(size * 0.15 * 1e6))
        text.SetTextAngle(pcbnew.EDA_ANGLE(rot, pcbnew.DEGREES_T))
        board.Add(text)

    add_text("ControlledUsb v1.0", x0 + w/2, y0 + 3.0, 0, 1.2)
    add_text("HOST IN", x0 + 13.0, y0 + h/2, 90, 0.9)
    add_text("OUT", x0 + w - 16.0, y0 + h/2, 90, 0.9)

    # 2. Place components with exact alignment
    # Clear old footprints
    for fp in list(board.GetFootprints()):
        board.Remove(fp)
        
    components = [
        # Designator, Value, FootprintLib, FootprintName, X (mm), Y (mm), Rotation (deg)
        # J1: USB-A Male Plug: placed at X=100.0 (left edge), Center Y=109.5, rot=180
        ("J1", "USB_A_Male", "Connector_USB.pretty", "USB_A_CNCTech_1001-011-01101_Horizontal", 100.0, 109.5, 180),
        
        # Upstream Protection & Filtering (X ~ 107 to 112)
        ("F1", "PTC 2A", "Fuse.pretty", "Fuse_1206_3216Metric", 109.0, 104.5, 90),
        ("U7", "USBLC6-2SC6", "Package_TO_SOT_SMD.pretty", "SOT-23-6", 109.0, 114.5, 0),
        ("C13", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 112.0, 104.5, 0),
        ("C3", "100nF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 112.0, 107.0, 0),
        
        # 3.3V LDO Regulator (X ~ 115)
        ("U6", "ME6211C33", "Package_TO_SOT_SMD.pretty", "SOT-23-5", 115.5, 104.5, 0),
        ("C14", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 115.5, 107.5, 0),
        ("C15", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 115.5, 114.5, 0),
        
        # WCH CH334F High-Speed USB Hub (X ~ 121)
        ("U3", "CH334F", "Package_DFN_QFN.pretty", "QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm", 121.5, 109.5, 0),
        ("Y2", "12.000MHz", "Crystal.pretty", "Crystal_SMD_3225-4Pin_3.2x2.5mm", 121.5, 115.5, 0),
        ("C4", "100nF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 119.0, 106.0, 90),
        ("C5", "100nF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 124.0, 106.0, 90),
        ("C11", "1uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 124.0, 113.0, 90),
        ("C16", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 119.0, 113.0, 90),
        
        # RP2040 USB series termination resistors (X ~ 127)
        ("R1", "27R", "Resistor_SMD.pretty", "R_0603_1608Metric", 127.0, 108.5, 0),
        ("R2", "27R", "Resistor_SMD.pretty", "R_0603_1608Metric", 127.0, 110.5, 0),
        
        # Raspberry Pi RP2040 MCU (X ~ 133.5)
        ("U1", "RP2040", "Package_DFN_QFN.pretty", "QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm", 133.5, 109.5, 0),
        ("Y1", "12.000MHz", "Crystal.pretty", "Crystal_SMD_3225-4Pin_3.2x2.5mm", 133.5, 116.0, 0),
        ("C1", "15pF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 130.5, 116.0, 90),
        ("C2", "15pF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 136.5, 116.0, 90),
        
        # User Tactile Button on top edge (X ~ 133.5, Y = 102.5)
        ("SW1", "USER_BTN", "Button_Switch_SMD.pretty", "SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS", 133.5, 102.5, 0),
        # BOOT & RESET buttons along bottom edge
        ("SW2", "BOOT", "Button_Switch_SMD.pretty", "SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS", 127.0, 116.5, 0),
        ("SW3", "RESET", "Button_Switch_SMD.pretty", "SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS", 140.0, 116.5, 0),
        
        # SPI Flash (X ~ 141) & Status RGB LED
        ("U2", "W25Q32", "Package_SO.pretty", "SOIC-8_3.9x4.9mm_P1.27mm", 141.0, 105.0, 0),
        ("D1", "WS2812B", "LED_SMD.pretty", "LED_WS2812B-2020_PLCC4_2.0x2.0mm", 140.0, 112.5, 0),
        
        # Power & Data Switches (X ~ 146.5)
        ("U4", "TPS22918", "Package_TO_SOT_SMD.pretty", "SOT-23-6", 146.5, 105.0, 0),
        ("R5", "10k", "Resistor_SMD.pretty", "R_0603_1608Metric", 144.0, 102.5, 90),
        ("U5", "CH440P", "Package_SO.pretty", "TSSOP-16_4.4x5mm_P0.65mm", 146.5, 112.5, 0),
        ("R6", "10k", "Resistor_SMD.pretty", "R_0603_1608Metric", 144.0, 116.5, 90),
        
        # Downstream ESD & Bulk Cap (X ~ 150)
        ("U8", "USBLC6-2SC6", "Package_TO_SOT_SMD.pretty", "SOT-23-6", 150.5, 113.0, 0),
        ("C17", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 150.5, 105.0, 0),
        
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
    print("PCB successfully updated with properly aligned connectors!")

if __name__ == "__main__":
    update_pcb("d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb")
