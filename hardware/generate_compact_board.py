import pcbnew
import os

def generate_compact_board(pcb_path):
    x0 = 100.0
    y0 = 100.0
    w = 62.0
    h = 20.0
    r = 2.0
    
    pcb_content = f"""(kicad_pcb
  (version 20231120)
  (generator "ControlledUsb_Compact_Engine")
  (generator_version "10.0")
  (general (thickness 1.6))
  (paper "A4")
  (title_block (title "ControlledUsb") (date "2026-10-03") (rev "v2.1-Dense"))
  (layers
    (0 "F.Cu" signal) (1 "In1.Cu" power "GND") (2 "In2.Cu" power "PWR") (31 "B.Cu" signal)
    (36 "B.SilkS" user) (37 "F.SilkS" user) (44 "Edge.Cuts" user) (46 "B.CrtYd" user) (47 "F.CrtYd" user)
  )
  (gr_line (start {x0 + r} {y0}) (end {x0 + w - r} {y0}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_arc (start {x0 + w - r} {y0}) (mid {x0 + w - r + r*0.7071} {y0 + r - r*0.7071}) (end {x0 + w} {y0 + r}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_line (start {x0 + w} {y0 + r}) (end {x0 + w} {y0 + h - r}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_arc (start {x0 + w} {y0 + h - r}) (mid {x0 + w - r + r*0.7071} {y0 + h - r + r*0.7071}) (end {x0 + w - r} {y0 + h}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_line (start {x0 + w - r} {y0 + h}) (end {x0 + r} {y0 + h}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_arc (start {x0 + r} {y0 + h}) (mid {x0 + r - r*0.7071} {y0 + h - r + r*0.7071}) (end {x0} {y0 + h - r}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_line (start {x0} {y0 + h - r}) (end {x0} {y0 + r}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_arc (start {x0} {y0 + r}) (mid {x0 + r - r*0.7071} {y0 + r - r*0.7071}) (end {x0 + r} {y0}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  
  (gr_text "ControlledUsb 62mm" (at 106.0 101.8 0) (layer "F.SilkS") (effects (font (size 0.85 0.85) (thickness 0.15))))
  (gr_text "HOST IN" (at 106.0 118.2 0) (layer "F.SilkS") (effects (font (size 0.75 0.75) (thickness 0.14))))
  (gr_text "DEVICE OUT" (at 148.0 101.5 0) (layer "F.SilkS") (effects (font (size 0.70 0.70) (thickness 0.12))))
  (gr_text "USER" (at 130.0 101.5 0) (layer "F.SilkS") (effects (font (size 0.65 0.65) (thickness 0.12))))
  (gr_text "BOOT" (at 134.5 119.0 0) (layer "F.SilkS") (effects (font (size 0.55 0.55) (thickness 0.11))))
  (gr_text "RESET" (at 137.0 119.0 0) (layer "F.SilkS") (effects (font (size 0.55 0.55) (thickness 0.11))))
  (gr_text "GND" (at 139.5 119.0 0) (layer "F.SilkS") (effects (font (size 0.55 0.55) (thickness 0.11))))
  (gr_text "RGB" (at 135.0 111.0 90) (layer "F.SilkS") (effects (font (size 0.60 0.60) (thickness 0.12))))
  (gr_text "FLASH" (at 137.5 101.5 0) (layer "F.SilkS") (effects (font (size 0.55 0.55) (thickness 0.11))))
  (gr_text "HUB" (at 121.0 107.5 0) (layer "F.SilkS") (effects (font (size 0.60 0.60) (thickness 0.12))))
  (gr_text "5V SW" (at 142.5 101.5 0) (layer "F.SilkS") (effects (font (size 0.55 0.55) (thickness 0.11))))
  (gr_text "DATA SW" (at 143.0 115.0 0) (layer "F.SilkS") (effects (font (size 0.55 0.55) (thickness 0.11))))
  (gr_text "3V3" (at 111.5 115.5 90) (layer "F.SilkS") (effects (font (size 0.60 0.60) (thickness 0.12))))
  (gr_text "2A" (at 111.5 104.5 0) (layer "F.SilkS") (effects (font (size 0.60 0.60) (thickness 0.12))))

  (gr_rect (start 103.0 102.0) (end 160.0 118.0) (stroke (width 0.2) (type solid)) (layer "B.SilkS"))
  (gr_text "ControlledUsb" (at 131.5 105.0 0) (layer "B.SilkS") (effects (font (size 2.0 2.0) (thickness 0.28)) (justify mirror)))
  (gr_text "High-Speed USB 2.0 Host-Controlled Dongle" (at 131.5 107.8 0) (layer "B.SilkS") (effects (font (size 0.85 0.85) (thickness 0.14)) (justify mirror)))
  (gr_text "GP26: USER BTN   |   GP16: RGB NEOPIXEL" (at 131.5 110.5 0) (layer "B.SilkS") (effects (font (size 0.70 0.70) (thickness 0.12)) (justify mirror)))
  (gr_text "GP14: 5V LOAD SW |   GP15: DATA SWITCH" (at 131.5 112.7 0) (layer "B.SilkS") (effects (font (size 0.70 0.70) (thickness 0.12)) (justify mirror)))
  (gr_text "UART: GP0 (TX), GP1 (RX) @ 115200 8N1" (at 131.5 114.9 0) (layer "B.SilkS") (effects (font (size 0.70 0.70) (thickness 0.12)) (justify mirror)))
  (gr_text "Hardware v2.1 | KiCad 10 | Open Hardware" (at 131.5 116.8 0) (layer "B.SilkS") (effects (font (size 0.65 0.65) (thickness 0.11)) (justify mirror)))
)
"""
    with open(pcb_path, "w", encoding="utf-8") as f:
        f.write(pcb_content)
        
    board = pcbnew.LoadBoard(pcb_path)
    base_fp = 'C:/Users/iagra/AppData/Local/Programs/KiCad/10.0/share/kicad/footprints'
    
    components = [
        ('J1', 'USB_A_Male', 'Connector_USB.pretty', 'USB_A_CNCTech_1001-011-01101_Horizontal', 100.0, 110.0, 180),
        ('F1', 'PTC 2A', 'Fuse.pretty', 'Fuse_1206_3216Metric', 113.5, 104.5, 90),
        ('U7', 'USBLC6-2SC6', 'Package_TO_SOT_SMD.pretty', 'SOT-23-6', 113.5, 109.5, 0),
        ('U6', 'ME6211C33', 'Package_TO_SOT_SMD.pretty', 'SOT-23-5', 113.5, 115.5, 180),
        
        ('C13', '10uF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 116.5, 103.5, 90),
        ('C14', '10uF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 116.5, 112.5, 90),
        ('C15', '10uF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 116.5, 116.5, 90),
        
        ('C11', '1uF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 120.0, 103.5, 0),
        ('C3', '100nF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 120.0, 106.0, 0),
        ('U3', 'CH334F', 'Package_DFN_QFN.pretty', 'QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm', 121.0, 110.0, 0),
        ('Y2', '12.000MHz', 'Crystal.pretty', 'Crystal_SMD_3225-4Pin_3.2x2.5mm', 121.0, 116.0, 0),
        
        ('C4', '100nF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 125.0, 103.5, 0),
        ('R1', '27R', 'Resistor_SMD.pretty', 'R_0603_1608Metric', 125.5, 108.0, 90),
        ('R2', '27R', 'Resistor_SMD.pretty', 'R_0603_1608Metric', 125.5, 111.0, 90),
        ('C5', '100nF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 125.0, 116.0, 0),
        
        ('SW1', 'USER_BTN', 'Button_Switch_SMD.pretty', 'SW_Push_1P1T_NO_CK_KMR2', 130.0, 103.5, 0),
        ('U1', 'RP2040', 'Package_DFN_QFN.pretty', 'QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm', 131.0, 110.0, 0),
        ('Y1', '12.000MHz', 'Crystal.pretty', 'Crystal_SMD_3225-4Pin_3.2x2.5mm', 130.0, 117.0, 0),
        
        ('U2', 'W25Q32', 'Package_SO.pretty', 'SOIC-8_3.9x4.9mm_P1.27mm', 137.5, 104.5, 90),
        ('D1', 'WS2812B', 'LED_SMD.pretty', 'LED_WS2812B-2020_PLCC4_2.0x2.0mm', 136.5, 111.0, 90),
        ('C1', '15pF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 135.5, 115.0, 90),
        ('C2', '15pF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 138.0, 115.0, 90),
        
        ('TP1', 'BOOT', 'TestPoint.pretty', 'TestPoint_Pad_D1.0mm', 134.5, 117.5, 0),
        ('TP2', 'RESET', 'TestPoint.pretty', 'TestPoint_Pad_D1.0mm', 137.0, 117.5, 0),
        ('TP3', 'GND', 'TestPoint.pretty', 'TestPoint_Pad_D1.0mm', 139.5, 117.5, 0),
        
        ('U4', 'TPS22918', 'Package_TO_SOT_SMD.pretty', 'SOT-23-6', 142.5, 104.0, 0),
        ('R5', '10k', 'Resistor_SMD.pretty', 'R_0603_1608Metric', 142.5, 107.0, 0),
        ('U5', 'CH440P', 'Package_SO.pretty', 'TSSOP-16_4.4x5mm_P0.65mm', 143.0, 112.5, 0),
        ('R6', '10k', 'Resistor_SMD.pretty', 'R_0603_1608Metric', 143.0, 117.0, 0),
        ('C17', '10uF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 146.5, 104.0, 90),
        
        ('J2', 'USB_A_Female', 'Connector_USB.pretty', 'USB_A_Molex_67643_Horizontal', 150.0, 113.5, 90),
    ]
    
    fps = []
    for ref, val, lib, name, x, y, rot in components:
        try:
            fp = pcbnew.FootprintLoad(os.path.join(base_fp, lib), name)
            if fp:
                fp.SetReference(ref)
                fp.SetValue(val)
                fp.SetPosition(pcbnew.VECTOR2I(int(x * 1e6), int(y * 1e6)))
                fp.SetOrientation(pcbnew.EDA_ANGLE(rot, pcbnew.DEGREES_T))
                
                fp.Value().SetVisible(False)
                
                if ref.startswith('R') or ref.startswith('C'):
                    fp.Reference().SetVisible(True)
                    # Scale down the reference text so it fits the compact layout
                    fp.Reference().SetTextSize(pcbnew.VECTOR2I(int(0.6 * 1e6), int(0.6 * 1e6)))
                    fp.Reference().SetTextThickness(int(0.12 * 1e6))
                    # Nudge the reference label slightly so it doesn't cover pads
                    if rot == 0:
                        fp.Reference().SetPosition(pcbnew.VECTOR2I(int(x * 1e6), int((y - 1.2) * 1e6)))
                    elif rot == 90:
                        fp.Reference().SetPosition(pcbnew.VECTOR2I(int((x - 1.2) * 1e6), int(y * 1e6)))
                        fp.Reference().SetTextAngle(pcbnew.EDA_ANGLE(90, pcbnew.DEGREES_T))
                else:
                    fp.Reference().SetVisible(False)

                if ref == 'D1' and len(fp.Models()) > 0:
                    m = fp.Models()[0]
                    m.m_Filename = '${KICAD10_3DMODEL_DIR}/LED_SMD.3dshapes/LED_WS2812B-Mini_PLCC4_3.5x3.5mm.step'
                    m.m_Scale = pcbnew.VECTOR3D(2.0/3.5, 2.0/3.5, 2.0/3.5)
                    
                board.Add(fp)
                fps.append((ref, fp))
        except: pass
            
    pcbnew.SaveBoard(pcb_path, board)
    print("Regenerated 62mm compact layout with passives labels!")

if __name__ == '__main__':
    generate_compact_board("d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb")
