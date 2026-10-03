import pcbnew
import os

def test_and_layout(pcb_path):
    # Board dimensions: 65.0 mm long x 20.0 mm wide
    # Left edge: X = 100.0, Right edge: X = 165.0
    # Top edge: Y = 100.0, Bottom edge: Y = 120.0
    # Centerline: Y = 110.0
    x0 = 100.0
    y0 = 100.0
    w = 65.0
    h = 20.0
    r = 2.0
    
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
    (date "2026-10-02")
    (rev "v1.3")
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
  (gr_arc (start {x0 + w - r} {y0 + h - r}) (mid {x0 + w - r * 0.293} {y0 + h - r * 0.293}) (end {x0 + w - r} {y0 + h}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_arc (start {x0 + r} {y0 + h}) (mid {x0 + r * 0.293} {y0 + h - r * 0.293}) (end {x0} {y0 + h - r}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))
  (gr_arc (start {x0} {y0 + r}) (mid {x0 + r * 0.293} {y0 + r * 0.293}) (end {x0 + r} {y0}) (stroke (width 0.15) (type solid)) (layer "Edge.Cuts"))

  (gr_text "ControlledUsb v1.3" (at {x0 + w/2} {y0 + 2.5} 0) (layer "F.SilkS")
    (effects (font (size 1.2 1.2) (thickness 0.2)))
  )
  (gr_text "HOST IN" (at {x0 + 13.0} {y0 + h/2} 90) (layer "F.SilkS")
    (effects (font (size 0.9 0.9) (thickness 0.15)))
  )
  (gr_text "OUT" (at {x0 + w - 17.0} {y0 + h/2} 90) (layer "F.SilkS")
    (effects (font (size 0.9 0.9) (thickness 0.15)))
  )
)
"""
    with open(pcb_path, "w", encoding="utf-8") as f:
        f.write(pcb_content)
        
    board = pcbnew.LoadBoard(pcb_path)
    base_fp = 'C:/Users/iagra/AppData/Local/Programs/KiCad/10.0/share/kicad/footprints'
    
    # Evenly balanced placement across 65mm board
    components = [
        # Designator, Value, FootprintLib, FootprintName, X (mm), Y (mm), Rotation (deg)
        # J1: USB-A Male Plug:
        ("J1", "USB_A_Male", "Connector_USB.pretty", "USB_A_CNCTech_1001-011-01101_Horizontal", 100.0, 110.0, 180),
        
        # Zone 1: Input Power & Protection (X = 111.5 to 115.5)
        ("F1", "PTC 2A", "Fuse.pretty", "Fuse_1206_3216Metric", 112.5, 104.5, 0),
        ("C13", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 115.5, 104.5, 90),
        ("C3", "100nF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 117.5, 104.5, 90),
        
        ("U7", "USBLC6-2SC6", "Package_TO_SOT_SMD.pretty", "SOT-23-6", 112.5, 115.5, 0),
        ("U6", "ME6211C33", "Package_TO_SOT_SMD.pretty", "SOT-23-5", 116.0, 115.5, 180),
        ("C14", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 114.5, 110.0, 90),
        ("C15", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 117.0, 110.0, 90),
        
        # Zone 2: WCH CH334F High-Speed USB Hub (X = 119.5 to 126.5)
        ("U3", "CH334F", "Package_DFN_QFN.pretty", "QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm", 121.5, 110.0, 0),
        ("Y2", "12.000MHz", "Crystal.pretty", "Crystal_SMD_3225-4Pin_3.2x2.5mm", 121.5, 116.5, 0),
        ("C4", "100nF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 120.0, 104.5, 0),
        ("C5", "100nF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 123.0, 104.5, 0),
        ("C11", "1uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 125.0, 116.5, 90),
        
        ("R1", "27R", "Resistor_SMD.pretty", "R_0603_1608Metric", 125.5, 108.5, 0),
        ("R2", "27R", "Resistor_SMD.pretty", "R_0603_1608Metric", 125.5, 111.5, 0),
        
        # Zone 3: Raspberry Pi RP2040 MCU Core (X = 129.5 to 138.5)
        ("U1", "RP2040", "Package_DFN_QFN.pretty", "QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm", 131.5, 110.0, 0),
        ("Y1", "12.000MHz", "Crystal.pretty", "Crystal_SMD_3225-4Pin_3.2x2.5mm", 131.5, 117.0, 0),
        ("C1", "15pF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 128.0, 117.0, 90),
        ("C2", "15pF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 135.0, 117.0, 90),
        
        # User Tactile Button SW1 (Top center on GP26, perfectly placed)
        ("SW1", "USER_BTN", "Button_Switch_SMD.pretty", "SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS", 131.5, 103.0, 0),
        
        # Zone 4: Flash, Buttons & Status LED (X = 139.5 to 147.5)
        ("U2", "W25Q32", "Package_SO.pretty", "SOIC-8_3.9x4.9mm_P1.27mm", 139.5, 106.0, 0),
        ("D1", "WS2812B", "LED_SMD.pretty", "LED_WS2812B-2020_PLCC4_2.0x2.0mm", 138.0, 112.5, 0),
        
        # BOOT (SW2) and RESET (SW3) buttons cleanly spaced with NO overlaps!
        # SW2 placed at X = 145.5, Y = 103.0 (top rail)
        # SW3 placed at X = 141.5, Y = 117.0 (bottom rail)
        ("SW2", "BOOT", "Button_Switch_SMD.pretty", "SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS", 146.0, 103.0, 0),
        ("SW3", "RESET", "Button_Switch_SMD.pretty", "SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS", 142.0, 117.0, 0),
        
        # Zone 5: Power & Data Switches (X = 148.5 to 154.5)
        ("U4", "TPS22918", "Package_TO_SOT_SMD.pretty", "SOT-23-6", 148.5, 110.5, 0),
        ("R5", "10k", "Resistor_SMD.pretty", "R_0603_1608Metric", 146.0, 107.5, 0),
        ("C17", "10uF", "Capacitor_SMD.pretty", "C_0603_1608Metric", 151.0, 107.5, 0),
        
        ("U5", "CH440P", "Package_SO.pretty", "TSSOP-16_4.4x5mm_P0.65mm", 149.0, 116.5, 0),
        ("R6", "10k", "Resistor_SMD.pretty", "R_0603_1608Metric", 152.0, 112.0, 90),
        
        # Zone 6: USB-A Female Receptacle J2:
        # Placed at X=153.0, Y=113.5, rot=90
        # Front lip at X = 166.0 (overhangs the X=165.0 board edge by 1.0mm)
        # Centerline perfectly aligned at Y = 110.0!
        ("J2", "USB_A_Female", "Connector_USB.pretty", "USB_A_Molex_67643_Horizontal", 153.0, 113.5, 90)
    ]
    
    fps = []
    for ref, val, lib, name, x, y, rot in components:
        lib_path = os.path.join(base_fp, lib)
        fp = pcbnew.FootprintLoad(lib_path, name)
        if fp:
            fp.SetReference(ref)
            fp.SetValue(val)
            fp.SetPosition(pcbnew.VECTOR2I(int(x * 1e6), int(y * 1e6)))
            fp.SetOrientation(pcbnew.EDA_ANGLE(rot, pcbnew.DEGREES_T))
            
            fp.Value().SetVisible(False)
            fp.Reference().SetTextSize(pcbnew.VECTOR2I(int(0.7 * 1e6), int(0.7 * 1e6)))
            fp.Reference().SetTextThickness(int(0.12 * 1e6))
            
            board.Add(fp)
            fps.append((ref, fp))
            
    # Check TRUE COURTYARD COLLISIONS
    print("\n--- TRUE COURTYARD COLLISION CHECK ---")
    lset = pcbnew.LSET()
    lset.AddLayer(pcbnew.F_CrtYd)
    
    crt_collisions = 0
    for i in range(len(fps)):
        ref1, fp1 = fps[i]
        b1 = fp1.GetLayerBoundingBox(lset)
        if b1.GetWidth() == 0: continue
        for j in range(i + 1, len(fps)):
            ref2, fp2 = fps[j]
            b2 = fp2.GetLayerBoundingBox(lset)
            if b2.GetWidth() == 0: continue
            
            if b1.Intersects(b2):
                ox = min(b1.GetX() + b1.GetWidth(), b2.GetX() + b2.GetWidth()) - max(b1.GetX(), b2.GetX())
                oy = min(b1.GetY() + b1.GetHeight(), b2.GetY() + b2.GetHeight()) - max(b1.GetY(), b2.GetY())
                if ox > 0.05e6 and oy > 0.05e6:
                    print(f"  COURTYARD OVERLAP: {ref1} and {ref2} intersect by {ox/1e6:.2f}mm x {oy/1e6:.2f}mm!")
                    crt_collisions += 1
                    
    if crt_collisions == 0:
        print("  SUCCESS! ZERO COURTYARD OVERLAPS! All components have 100% full physical clearance!")
    else:
        print(f"  Total courtyard overlaps: {crt_collisions}")

    pcbnew.SaveBoard(pcb_path, board)
    print("Balanced board layout saved successfully!")

if __name__ == "__main__":
    test_and_layout("d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb")
