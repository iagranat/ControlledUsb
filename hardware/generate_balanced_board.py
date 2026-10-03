import pcbnew
import os

def generate_compact_board(pcb_path):
    x0 = 100.0
    y0 = 100.0
    w = 63.0
    h = 20.0
    r = 2.0
    
    pcb_content = f"""(kicad_pcb
  (version 20231120)
  (generator "ControlledUsb_Compact_Engine")
  (generator_version "10.0")
  (general (thickness 1.6))
  (paper "A4")
  (title_block (title "ControlledUsb") (date "2026-10-03") (rev "v2.0-Compact"))
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
  
  (gr_text "ControlledUsb 63mm" (at 106.0 101.8 0) (layer "F.SilkS")
    (effects (font (size 0.85 0.85) (thickness 0.15)))
  )
  (gr_rect (start 103.0 102.0) (end 161.0 118.0) (stroke (width 0.2) (type solid)) (layer "B.SilkS"))
  (gr_text "ControlledUsb" (at 132.0 105.0 0) (layer "B.SilkS")
    (effects (font (size 2.0 2.0) (thickness 0.28)) (justify mirror))
  )
)
"""
    with open(pcb_path, "w", encoding="utf-8") as f:
        f.write(pcb_content)
        
    board = pcbnew.LoadBoard(pcb_path)
    base_fp = 'C:/Users/iagra/AppData/Local/Programs/KiCad/10.0/share/kicad/footprints'
    
    components = [
        ('J1', 'USB_A_Male', 'Connector_USB.pretty', 'USB_A_CNCTech_1001-011-01101_Horizontal', 100.0, 110.0, 180),
        
        ('F1', 'PTC 2A', 'Fuse.pretty', 'Fuse_1206_3216Metric', 114.5, 103.5, 0),
        ('U7', 'USBLC6-2SC6', 'Package_TO_SOT_SMD.pretty', 'SOT-23-6', 114.5, 108.5, 0),
        ('U6', 'ME6211C33', 'Package_TO_SOT_SMD.pretty', 'SOT-23-5', 114.5, 115.5, 180),
        
        ('C13', '10uF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 118.0, 103.5, 90),
        ('C14', '10uF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 118.0, 112.5, 90),
        ('C15', '10uF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 118.0, 116.5, 90),
        
        ('C11', '1uF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 121.5, 103.5, 0),
        ('C3', '100nF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 121.5, 106.0, 0),
        ('U3', 'CH334F', 'Package_DFN_QFN.pretty', 'QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm', 122.5, 110.0, 0),
        ('Y2', '12.000MHz', 'Crystal.pretty', 'Crystal_SMD_3225-4Pin_3.2x2.5mm', 122.5, 116.0, 0),
        
        ('C4', '100nF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 126.5, 103.5, 0),
        ('R1', '27R', 'Resistor_SMD.pretty', 'R_0603_1608Metric', 127.0, 108.0, 90),
        ('R2', '27R', 'Resistor_SMD.pretty', 'R_0603_1608Metric', 127.0, 111.0, 90),
        ('C5', '100nF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 126.5, 116.0, 0),
        
        ('SW1', 'USER_BTN', 'Button_Switch_SMD.pretty', 'SW_Push_1P1T_NO_CK_KMR2', 131.5, 103.5, 0),
        ('U1', 'RP2040', 'Package_DFN_QFN.pretty', 'QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm', 132.5, 110.0, 0),
        ('Y1', '12.000MHz', 'Crystal.pretty', 'Crystal_SMD_3225-4Pin_3.2x2.5mm', 131.5, 117.0, 0),
        
        ('U2', 'W25Q32', 'Package_SO.pretty', 'SOIC-8_3.9x4.9mm_P1.27mm', 140.0, 104.0, 90),
        ('D1', 'WS2812B', 'LED_SMD.pretty', 'LED_WS2812B-2020_PLCC4_2.0x2.0mm', 138.5, 111.0, 0),
        ('C1', '15pF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 137.5, 115.0, 90),
        ('C2', '15pF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 139.0, 115.0, 90),
        
        ('U4', 'TPS22918', 'Package_TO_SOT_SMD.pretty', 'SOT-23-6', 145.0, 103.5, 0),
        ('R5', '10k', 'Resistor_SMD.pretty', 'R_0603_1608Metric', 145.0, 106.5, 0),
        ('U5', 'CH440P', 'Package_SO.pretty', 'TSSOP-16_4.4x5mm_P0.65mm', 144.0, 112.5, 0),
        ('R6', '10k', 'Resistor_SMD.pretty', 'R_0603_1608Metric', 144.5, 117.0, 0),
        ('C17', '10uF', 'Capacitor_SMD.pretty', 'C_0603_1608Metric', 145.0, 101.0, 0),
        
        ('TP1', 'BOOT', 'TestPoint.pretty', 'TestPoint_Pad_D1.0mm', 136.0, 117.5, 0),
        ('TP2', 'RESET', 'TestPoint.pretty', 'TestPoint_Pad_D1.0mm', 138.5, 117.5, 0),
        ('TP3', 'GND', 'TestPoint.pretty', 'TestPoint_Pad_D1.0mm', 141.0, 117.5, 0),
        
        ('J2', 'USB_A_Female', 'Connector_USB.pretty', 'USB_A_Molex_67643_Horizontal', 151.0, 113.5, 90),
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
                fp.Reference().SetVisible(False)
                if ref == 'D1' and len(fp.Models()) > 0:
                    m = fp.Models()[0]
                    m.m_Filename = '${KICAD10_3DMODEL_DIR}/LED_SMD.3dshapes/LED_WS2812B-Mini_PLCC4_3.5x3.5mm.step'
                    m.m_Scale = pcbnew.VECTOR3D(2.0/3.5, 2.0/3.5, 2.0/3.5)
                    
                board.Add(fp)
                fps.append((ref, fp))
        except: pass
            
    lset = pcbnew.LSET()
    lset.AddLayer(pcbnew.F_CrtYd)
    
    collisions = []
    for i in range(len(fps)):
        b1 = fps[i][1].GetLayerBoundingBox(lset)
        if b1.GetWidth() == 0: continue
        for j in range(i + 1, len(fps)):
            b2 = fps[j][1].GetLayerBoundingBox(lset)
            if b2.GetWidth() == 0: continue
            
            if b1.Intersects(b2):
                ox = min(b1.GetX() + b1.GetWidth(), b2.GetX() + b2.GetWidth()) - max(b1.GetX(), b2.GetX())
                oy = min(b1.GetY() + b1.GetHeight(), b2.GetY() + b2.GetHeight()) - max(b1.GetY(), b2.GetY())
                if ox > 0.05e6 and oy > 0.05e6:
                    collisions.append(f"{fps[i][0]} & {fps[j][0]}: {ox/1e6:.2f}x{oy/1e6:.2f}mm")
                    
    for c in collisions: print(c)
    if not collisions:
        print("NO COLLISIONS! Saving 63mm board.")
        pcbnew.SaveBoard(pcb_path, board)
        
if __name__ == '__main__':
    generate_compact_board("d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb")









