import pcbnew
import os

def adjust_pcb_edge(pcb_path):
    # Board dimensions: 57.0 mm long x 19.0 mm wide
    # Left edge: X = 100.0
    # Right edge: X = 157.0 (so J2 front lip at X=158.0 overhangs cleanly by 1.0mm)
    # Centerline Y = 109.5
    x0 = 100.0
    y0 = 100.0
    w = 57.0
    h = 19.0
    r = 1.5
    
    # 1. Update board base S-expression
    pcb_content = f"""(kicad_pcb
  (version 20231120)
  (generator "ControlledUsb_PCB_Builder")
  (generator_version "10.0")
  (general
    (thickness 1.6)
    (legacy_teardrops no)
  )
  (paper "A4")
  (title_block
    (title "ControlledUsb Dongle")
    (date "2026-10-01")
    (rev "v1.0")
    (company "ControlledUsb Open Hardware")
    (comment 1 "High-Speed USB 2.0 Host-Controlled Extension Dongle")
    (comment 2 "Stackup: JLCPCB JLC04161H 4-Layer (Top/GND/Power/Bottom)")
  )
  (layers
    (0 "F.Cu" signal)
    (1 "In1.Cu" power "GND")
    (2 "In2.Cu" power "PWR")
    (31 "B.Cu" signal)
    (32 "B.Adhes" user "B.Adhesive")
    (33 "F.Adhes" user "F.Adhesive")
    (34 "B.Paste" user)
    (35 "F.Paste" user)
    (36 "B.SilkS" user "B.Silkscreen")
    (37 "F.SilkS" user "F.Silkscreen")
    (38 "B.Mask" user)
    (39 "F.Mask" user)
    (40 "Dwgs.User" user "User.Drawings")
    (41 "Cmts.User" user "User.Comments")
    (42 "Eco1.User" user "User.Eco1")
    (43 "Eco2.User" user "User.Eco2")
    (44 "Edge.Cuts" user)
    (45 "Margin" user)
    (46 "B.CrtYd" user "B.Courtyard")
    (47 "F.CrtYd" user "F.Courtyard")
    (48 "B.Fab" user)
    (49 "F.Fab" user)
  )
  (setup
    (pad_to_mask_clearance 0)
    (allow_soldermask_bridges_in_footprints no)
    (pcbplotparams
      (layerselection 0x00010fc_ffffffff)
      (plot_on_all_layers_selection 0x0000000_00000000)
      (disableapertmacros no)
      (usegerberextensions yes)
      (usegerberattributes yes)
      (usegerberadvancedattributes yes)
      (creategerberjobfile yes)
      (dashed_line_dash_ratio 12.000000)
      (dashed_line_gap_ratio 3.000000)
      (svgprecision 4)
      (plotframeref no)
      (viasonmask no)
      (mode 1)
      (useauxorigin no)
      (hpglpennumber 1)
      (hpglpenspeed 20)
      (hpglpendiameter 15.000000)
      (pdf_front_fp_property_popups yes)
      (pdf_back_fp_property_popups yes)
      (dxfpadmode 0)
      (dxfshapemode 1)
      (dxfprecision 4)
      (dxfvias no)
      (dxftEXTmode 0)
      (dxfcoppercolor 0)
      (dxfusepcbnewfont yes)
      (outputformat 1)
      (mirror no)
      (drillshape 1)
      (scaleselection 1)
      (outputdirectory "gerber/")
    )
  )

  (gr_line (start {x0 + r} {y0}) (end {x0 + w - r} {y0}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_line (start {x0 + w} {y0 + r}) (end {x0 + w} {y0 + h - r}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_line (start {x0 + w - r} {y0 + h}) (end {x0 + r} {y0 + h}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_line (start {x0} {y0 + h - r}) (end {x0} {y0 + r}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_arc (start {x0 + w - r} {y0 + r}) (mid {x0 + w - r * 0.293} {y0 + r * 0.293}) (end {x0 + w} {y0 + r}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_arc (start {x0 + w} {y0 + h - r}) (mid {x0 + w - r * 0.293} {y0 + h - r * 0.293}) (end {x0 + w - r} {y0 + h}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_arc (start {x0 + r} {y0 + h}) (mid {x0 + r * 0.293} {y0 + h - r * 0.293}) (end {x0} {y0 + h - r}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_arc (start {x0} {y0 + r}) (mid {x0 + r * 0.293} {y0 + r * 0.293}) (end {x0 + r} {y0}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))

  (gr_text "ControlledUsb v1.0" (at {x0 + w/2} {y0 + 3.0} 0) (layer "F.SilkS")
    (effects (font (size 1.2 1.2) (thickness 0.2)))
  )
  (gr_text "HOST IN" (at {x0 + 13.0} {y0 + h/2} 90) (layer "F.SilkS")
    (effects (font (size 0.9 0.9) (thickness 0.15)))
  )
  (gr_text "OUT" (at {x0 + w - 16.0} {y0 + h/2} 90) (layer "F.SilkS")
    (effects (font (size 0.9 0.9) (thickness 0.15)))
  )
)
"""
    with open(pcb_path, "w", encoding="utf-8") as f:
        f.write(pcb_content)
        
    # 2. Populate components
    board = pcbnew.LoadBoard(pcb_path)
    base_fp = 'C:/Users/iagra/AppData/Local/Programs/KiCad/10.0/share/kicad/footprints'
    
    components = [
        # Designator, Value, FootprintLib, FootprintName, X (mm), Y (mm), Rotation (deg)
        ("J1", "USB_A_Male", "Connector_USB.pretty", "USB_A_CNCTech_1001-011-01101_Horizontal", 100.0, 109.5, 180),
        
        ("F1", "PTC 2A", "Fuse.pretty", "Fuse_1206_3216Metric", 110.5, 103.5, 0),
        ("U7", "USBLC6-2SC6", "Package_TO_SOT_SMD.pretty", "SOT-23-6", 110.5, 115.5, 0),
        ("C13", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 113.0, 103.5, 90),
        ("C3", "100nF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 113.0, 106.0, 90),
        
        ("U6", "ME6211C33", "Package_TO_SOT_SMD.pretty", "SOT-23-5", 113.5, 115.5, 180),
        ("C14", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 116.0, 115.5, 90),
        ("C15", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 116.0, 103.5, 90),
        
        ("U3", "CH334F", "Package_DFN_QFN.pretty", "QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm", 118.0, 109.5, 0),
        ("Y2", "12.000MHz", "Crystal.pretty", "Crystal_SMD_3225-4Pin_3.2x2.5mm", 118.0, 115.5, 0),
        ("C4", "100nF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 116.0, 107.0, 0),
        ("C5", "100nF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 120.5, 104.5, 90),
        ("C11", "1uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 120.5, 114.5, 90),
        
        ("R1", "27R", "Resistor_SMD.pretty", "R_0603_1608Metric", 122.0, 108.5, 0),
        ("R2", "27R", "Resistor_SMD.pretty", "R_0603_1608Metric", 122.0, 110.5, 0),
        
        ("U1", "RP2040", "Package_DFN_QFN.pretty", "QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm", 127.0, 109.5, 0),
        ("Y1", "12.000MHz", "Crystal.pretty", "Crystal_SMD_3225-4Pin_3.2x2.5mm", 127.0, 116.0, 0),
        ("C1", "15pF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 124.0, 116.0, 90),
        ("C2", "15pF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 130.0, 116.0, 90),
        
        ("SW1", "USER_BTN", "Button_Switch_SMD.pretty", "SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS", 127.0, 102.5, 0),
        ("SW2", "BOOT", "Button_Switch_SMD.pretty", "SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS", 121.5, 116.5, 0),
        ("SW3", "RESET", "Button_Switch_SMD.pretty", "SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS", 132.5, 116.5, 0),
        
        ("U2", "W25Q32", "Package_SO.pretty", "SOIC-8_3.9x4.9mm_P1.27mm", 134.0, 105.0, 0),
        ("D1", "WS2812B", "LED_SMD.pretty", "LED_WS2812B-2020_PLCC4_2.0x2.0mm", 134.0, 112.5, 0),
        
        ("U4", "TPS22918", "Package_TO_SOT_SMD.pretty", "SOT-23-6", 138.0, 104.5, 0),
        ("R5", "10k", "Resistor_SMD.pretty", "R_0603_1608Metric", 138.0, 107.5, 0),
        ("U5", "CH440P", "Package_SO.pretty", "TSSOP-16_4.4x5mm_P0.65mm", 138.0, 114.5, 0),
        ("R6", "10k", "Resistor_SMD.pretty", "R_0603_1608Metric", 138.0, 111.0, 0),
        
        ("C17", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 135.0, 108.5, 90),
        
        # J2: USB-A Female Receptacle placed at X=145.0, Y=113.0, rot=90
        # Front lip is at X = 158.0. Since board edge is at X = 157.0:
        # The connector overhangs the PCB edge by exactly 1.0 mm!
        ("J2", "USB_A_Female", "Connector_USB.pretty", "USB_A_Molex_67643_Horizontal", 145.0, 113.0, 90)
    ]
    
    for ref, val, lib, name, x, y, rot in components:
        lib_path = os.path.join(base_fp, lib)
        fp = pcbnew.FootprintLoad(lib_path, name)
        if fp:
            fp.SetReference(ref)
            fp.SetValue(val)
            fp.SetPosition(pcbnew.VECTOR2I(int(x * 1e6), int(y * 1e6)))
            fp.SetOrientation(pcbnew.EDA_ANGLE(rot, pcbnew.DEGREES_T))
            board.Add(fp)
            
    pcbnew.SaveBoard(pcb_path, board)
    print("PCB successfully updated with 1.0mm connector overhang!")

if __name__ == "__main__":
    adjust_pcb_edge("d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb")
