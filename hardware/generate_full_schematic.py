import subprocess
import uuid
import os

def uid():
    return str(uuid.uuid4())

def generate_schematic():
    root_uuid = "4c38a598-fbac-4a7d-94fb-08842dc4d130"
    
    # -------------------------------------------------------------
    # 1. Symbol Library Definitions
    # -------------------------------------------------------------
    lib_symbols = f"""	(lib_symbols
		(symbol "ControlledUsb:R_Small"
			(pin_numbers (hide yes))
			(pin_names (offset 0.254) (hide yes))
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
			(property "Value" "R_Small" (at 1.778 0 90) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "R_Small_0_1"
				(rectangle (start -0.762 1.778) (end 0.762 -1.778) (stroke (width 0.2032)) (fill (type none)))
			)
			(symbol "R_Small_1_1"
				(pin passive line (at 0 2.54 270) (length 0.762) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -2.54 90) (length 0.762) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:C_Small"
			(pin_numbers (hide yes))
			(pin_names (offset 0.254) (hide yes))
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Value" "C_Small" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "C_Small_0_1"
				(polyline (pts (xy -1.524 0.508) (xy 1.524 0.508)) (stroke (width 0.254)))
				(polyline (pts (xy -1.524 -0.508) (xy 1.524 -0.508)) (stroke (width 0.254)))
			)
			(symbol "C_Small_1_1"
				(pin passive line (at 0 2.54 270) (length 2.032) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -2.54 90) (length 2.032) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:Polyfuse"
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "F" (at 2.032 0 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Value" "Polyfuse" (at 2.032 -2.032 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "Polyfuse_0_1"
				(rectangle (start -1.016 2.032) (end 1.016 -2.032) (stroke (width 0.254)) (fill (type none)))
				(polyline (pts (xy -1.524 -1.524) (xy 1.524 1.524)) (stroke (width 0.254)))
			)
			(symbol "Polyfuse_1_1"
				(pin passive line (at 0 3.81 270) (length 1.778) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 1.778) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:Crystal_GND24"
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "Y" (at 3.81 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Value" "Crystal_GND24" (at 3.81 0 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "Crystal_GND24_0_1"
				(rectangle (start -2.54 3.048) (end 2.54 -3.048) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "Crystal_GND24_1_1"
				(pin passive line (at -5.08 1.27 0) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -5.08 90) (length 2.032) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 5.08 1.27 180) (length 2.54) (name "3" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 5.08 270) (length 2.032) (name "4" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:USB_A_Plug"
			(pin_names (offset 1.016))
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "J" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
			(property "Value" "USB_A_Plug" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "USB_A_Plug_0_1"
				(rectangle (start -5.08 3.81) (end 5.08 -8.89) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "USB_A_Plug_1_1"
				(pin power_out line (at 7.62 2.54 180) (length 2.54) (name "VBUS" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 7.62 0 180) (length 2.54) (name "D-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 7.62 -2.54 180) (length 2.54) (name "D+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin power_out line (at 7.62 -5.08 180) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 7.62 -7.62 180) (length 2.54) (name "Shield" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:USB_A_Receptacle"
			(pin_names (offset 1.016))
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "J" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
			(property "Value" "USB_A_Receptacle" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "USB_A_Receptacle_0_1"
				(rectangle (start -5.08 3.81) (end 5.08 -8.89) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "USB_A_Receptacle_1_1"
				(pin power_in line (at -7.62 2.54 0) (length 2.54) (name "VBUS" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -7.62 0 0) (length 2.54) (name "D-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -7.62 -2.54 0) (length 2.54) (name "D+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at -7.62 -5.08 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin passive line (at -7.62 -7.62 0) (length 2.54) (name "Shield" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:USBLC6-2SC6"
			(pin_names (offset 1.016))
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "U" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
			(property "Value" "USBLC6-2SC6" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "USBLC6-2SC6_0_1"
				(rectangle (start -7.62 2.54) (end 7.62 -7.62) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "USBLC6-2SC6_1_1"
				(pin bidirectional line (at -10.16 0 0) (length 2.54) (name "IO1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -10.16 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -10.16 -2.54 0) (length 2.54) (name "IO2" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 10.16 -2.54 180) (length 2.54) (name "IO2" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 5.08 270) (length 2.54) (name "VBUS" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 10.16 0 180) (length 2.54) (name "IO1" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:ME6211C33"
			(pin_names (offset 1.016))
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "U" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
			(property "Value" "ME6211C33" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "ME6211C33_0_1"
				(rectangle (start -7.62 2.54) (end 7.62 -7.62) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "ME6211C33_1_1"
				(pin power_in line (at -10.16 0 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -10.16 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin input line (at -10.16 -5.08 0) (length 2.54) (name "EN" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 10.16 -5.08 180) (length 2.54) (name "NC" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin power_out line (at 10.16 0 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:TPS22918"
			(pin_names (offset 1.016))
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "U" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
			(property "Value" "TPS22918" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "TPS22918_0_1"
				(rectangle (start -7.62 2.54) (end 7.62 -7.62) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "TPS22918_1_1"
				(pin power_in line (at -10.16 0 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -10.16 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin input line (at -10.16 -5.08 0) (length 2.54) (name "ON" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 10.16 -5.08 180) (length 2.54) (name "CT" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 10.16 -2.54 180) (length 2.54) (name "QOD" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
				(pin power_out line (at 10.16 0 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:W25Q32"
			(pin_names (offset 1.016))
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "U" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
			(property "Value" "W25Q32" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "W25Q32_0_1"
				(rectangle (start -10.16 5.08) (end 10.16 -7.62) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "W25Q32_1_1"
				(pin input line (at -12.7 2.54 0) (length 2.54) (name "~{{CS}}" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 12.7 0 180) (length 2.54) (name "DO(IO1)" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -12.7 -2.54 0) (length 2.54) (name "~{{WP}}(IO2)" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -10.16 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -12.7 0 0) (length 2.54) (name "DI(IO0)" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
				(pin input line (at -12.7 -5.08 0) (length 2.54) (name "CLK" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 12.7 -2.54 180) (length 2.54) (name "~{{HOLD}}(IO3)" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 7.62 270) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:CH334F"
			(pin_names (offset 1.016))
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "U" (at 0 17.78 0) (effects (font (size 1.27 1.27))))
			(property "Value" "CH334F" (at 0 15.24 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "CH334F_0_1"
				(rectangle (start -15.24 13.97) (end 15.24 -16.51) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "CH334F_1_1"
				(pin power_in line (at -5.08 16.51 270) (length 2.54) (name "V5" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
				(pin power_out line (at 5.08 16.51 270) (length 2.54) (name "V33" (effects (font (size 1.27 1.27)))) (number "20" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -19.05 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "25" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -17.78 7.62 0) (length 2.54) (name "D+U" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -17.78 5.08 0) (length 2.54) (name "D-U" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 7.62 180) (length 2.54) (name "D+1" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 5.08 180) (length 2.54) (name "D-1" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 0 180) (length 2.54) (name "D+2" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 -2.54 180) (length 2.54) (name "D-2" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
				(pin input line (at -17.78 -5.08 0) (length 2.54) (name "XIN" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin output line (at -17.78 -7.62 0) (length 2.54) (name "XOUT" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin input line (at -17.78 -12.7 0) (length 2.54) (name "PSELF" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:CH440P"
			(pin_names (offset 1.016))
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "U" (at 0 15.24 0) (effects (font (size 1.27 1.27))))
			(property "Value" "CH440P" (at 0 12.7 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "CH440P_0_1"
				(rectangle (start -12.7 11.43) (end 12.7 -13.97) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "CH440P_1_1"
				(pin power_in line (at 0 13.97 270) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -16.51 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
				(pin input line (at -15.24 7.62 0) (length 2.54) (name "IN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin input line (at -15.24 5.08 0) (length 2.54) (name "~{{EN}}" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -15.24 0 0) (length 2.54) (name "DA" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -15.24 -2.54 0) (length 2.54) (name "DD" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 0 180) (length 2.54) (name "S1A" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 -2.54 180) (length 2.54) (name "S1D" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:RP2040"
			(pin_names (offset 1.016))
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "U" (at 0 25.4 0) (effects (font (size 1.27 1.27))))
			(property "Value" "RP2040" (at 0 22.86 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "RP2040_0_1"
				(rectangle (start -20.32 20.32) (end 20.32 -25.4) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "RP2040_1_1"
				(pin power_in line (at -5.08 22.86 270) (length 2.54) (name "IOVDD" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 22.86 270) (length 2.54) (name "VREG_VIN" (effects (font (size 1.27 1.27)))) (number "44" (effects (font (size 1.27 1.27)))))
				(pin power_out line (at 5.08 22.86 270) (length 2.54) (name "VREG_VOUT" (effects (font (size 1.27 1.27)))) (number "45" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 10.08 22.86 270) (length 2.54) (name "DVDD" (effects (font (size 1.27 1.27)))) (number "23" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -27.94 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "57" (effects (font (size 1.27 1.27)))))
				(pin input line (at -22.86 12.7 0) (length 2.54) (name "XIN" (effects (font (size 1.27 1.27)))) (number "20" (effects (font (size 1.27 1.27)))))
				(pin output line (at -22.86 10.16 0) (length 2.54) (name "XOUT" (effects (font (size 1.27 1.27)))) (number "21" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -22.86 5.08 0) (length 2.54) (name "USB_DM" (effects (font (size 1.27 1.27)))) (number "46" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -22.86 2.54 0) (length 2.54) (name "USB_DP" (effects (font (size 1.27 1.27)))) (number "47" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -22.86 -2.54 0) (length 2.54) (name "QSPI_SS" (effects (font (size 1.27 1.27)))) (number "51" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -22.86 -5.08 0) (length 2.54) (name "QSPI_SD0" (effects (font (size 1.27 1.27)))) (number "53" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -22.86 -7.62 0) (length 2.54) (name "QSPI_SD1" (effects (font (size 1.27 1.27)))) (number "55" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -22.86 -10.16 0) (length 2.54) (name "QSPI_SD2" (effects (font (size 1.27 1.27)))) (number "54" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -22.86 -12.7 0) (length 2.54) (name "QSPI_SD3" (effects (font (size 1.27 1.27)))) (number "52" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -22.86 -15.24 0) (length 2.54) (name "QSPI_SCLK" (effects (font (size 1.27 1.27)))) (number "56" (effects (font (size 1.27 1.27)))))
				(pin input line (at -22.86 -20.32 0) (length 2.54) (name "RUN" (effects (font (size 1.27 1.27)))) (number "26" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 22.86 12.7 180) (length 2.54) (name "GP14(PWR)" (effects (font (size 1.27 1.27)))) (number "24" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 22.86 10.16 180) (length 2.54) (name "GP15(DATA)" (effects (font (size 1.27 1.27)))) (number "25" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 22.86 5.08 180) (length 2.54) (name "GP16(RGB)" (effects (font (size 1.27 1.27)))) (number "27" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 22.86 0 180) (length 2.54) (name "GP26(BTN)" (effects (font (size 1.27 1.27)))) (number "37" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:SW_Push"
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "SW" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Value" "SW_Push" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "SW_Push_0_1"
				(circle (center -2.032 0) (radius 0.508) (stroke (width 0.254)))
				(circle (center 2.032 0) (radius 0.508) (stroke (width 0.254)))
				(polyline (pts (xy -1.524 1.27) (xy 1.524 1.27)) (stroke (width 0.254)))
			)
			(symbol "SW_Push_1_1"
				(pin passive line (at -5.08 0 0) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 5.08 0 180) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:WS2812B"
			(pin_names (offset 1.016))
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "D" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
			(property "Value" "WS2812B" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "WS2812B_0_1"
				(rectangle (start -7.62 2.54) (end 7.62 -7.62) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "WS2812B_1_1"
				(pin power_in line (at 0 5.08 270) (length 2.54) (name "VDD" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin output line (at 10.16 -2.54 180) (length 2.54) (name "DOUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -10.16 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin input line (at -10.16 -2.54 0) (length 2.54) (name "DIN" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:TestPoint"
			(exclude_from_sim no) (in_bom yes) (on_board yes)
			(property "Reference" "TP" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Value" "TestPoint" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "TestPoint_0_1"
				(circle (center 0 0) (radius 1.27) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "TestPoint_1_1"
				(pin passive line (at -2.54 0 0) (length 1.27) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:GND"
			(power) (pin_numbers (hide yes))
			(property "Reference" "#PWR" (at 0 -2.54 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Value" "GND" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "GND_0_1"
				(polyline (pts (xy -1.27 0) (xy 1.27 0)) (stroke (width 0.254)))
				(polyline (pts (xy -0.635 -0.635) (xy 0.635 -0.635)) (stroke (width 0.254)))
				(polyline (pts (xy -0.254 -1.27) (xy 0.254 -1.27)) (stroke (width 0.254)))
			)
			(symbol "GND_1_1"
				(pin power_in line (at 0 0 270) (length 0) (name "GND" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:+5V"
			(power) (pin_numbers (hide yes))
			(property "Reference" "#PWR" (at 0 2.54 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Value" "+5V" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "+5V_0_1"
				(polyline (pts (xy -0.762 0.762) (xy 0 2.032) (xy 0.762 0.762)) (stroke (width 0.254)))
				(polyline (pts (xy 0 0) (xy 0 2.032)) (stroke (width 0.254)))
			)
			(symbol "+5V_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "+5V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:+3V3"
			(power) (pin_numbers (hide yes))
			(property "Reference" "#PWR" (at 0 2.54 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Value" "+3V3" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "+3V3_0_1"
				(polyline (pts (xy -0.762 0.762) (xy 0 2.032) (xy 0.762 0.762)) (stroke (width 0.254)))
				(polyline (pts (xy 0 0) (xy 0 2.032)) (stroke (width 0.254)))
			)
			(symbol "+3V3_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "+3V3" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "ControlledUsb:+1V1"
			(power) (pin_numbers (hide yes))
			(property "Reference" "#PWR" (at 0 2.54 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Value" "+1V1" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
			(symbol "+1V1_0_1"
				(polyline (pts (xy -0.762 0.762) (xy 0 2.032) (xy 0.762 0.762)) (stroke (width 0.254)))
				(polyline (pts (xy 0 0) (xy 0 2.032)) (stroke (width 0.254)))
			)
			(symbol "+1V1_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "+1V1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
	)"""

    instances = []
    wires = []
    labels = []
    texts = []

    def add_sym(lib_id, ref, val, footprint, x, y, pins, rot=0):
        comp_uuid = uid()
        pin_entries = "\n".join([f'\t\t(pin "{p}" (uuid "{uid()}"))' for p in pins])
        s = f"""	(symbol
		(lib_id "{lib_id}")
		(at {x} {y} {rot})
		(unit 1)
		(exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
		(uuid "{comp_uuid}")
		(property "Reference" "{ref}" (at {x} {y-5} 0) (effects (font (size 1.27 1.27))))
		(property "Value" "{val}" (at {x} {y+5} 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "{footprint}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) (hide yes)))
		(property "Datasheet" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) (hide yes)))
		(property "Description" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) (hide yes)))
{pin_entries}
		(instances
			(project "ControlledUsb"
				(path "/{root_uuid}"
					(reference "{ref}")
					(unit 1)
				)
			)
		)
	)"""
        instances.append(s)

    def add_pwr(lib_id, net_name, x, y):
        comp_uuid = uid()
        s = f"""	(symbol
		(lib_id "{lib_id}")
		(at {x} {y} 0)
		(unit 1)
		(exclude_from_sim no) (in_bom no) (on_board yes) (dnp no)
		(uuid "{comp_uuid}")
		(property "Reference" "#PWR" (at {x} {y} 0) (effects (font (size 1.27 1.27)) (hide yes)))
		(property "Value" "{net_name}" (at {x} {y-2 if "GND" not in net_name else y+2} 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) (hide yes)))
		(property "Datasheet" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) (hide yes)))
		(property "Description" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) (hide yes)))
		(pin "1" (uuid "{uid()}"))
		(instances
			(project "ControlledUsb"
				(path "/{root_uuid}"
					(reference "#PWR")
					(unit 1)
				)
			)
		)
	)"""
        instances.append(s)

    def add_wire(x1, y1, x2, y2):
        w = f"""	(wire (pts (xy {x1} {y1}) (xy {x2} {y2}))
		(stroke (width 0) (type solid))
		(uuid "{uid()}")
	)"""
        wires.append(w)

    def add_label(name, x, y, rot=0):
        l = f"""	(label "{name}" (at {x} {y} {rot}) (fields_autoplaced yes)
		(effects (font (size 1.27 1.27)))
		(uuid "{uid()}")
	)"""
        labels.append(l)

    def add_text(txt, x, y, size=2.5):
        t = f"""	(text "{txt}" (at {x} {y} 0) (effects (font (size {size} {size}) (bold yes))))"""
        texts.append(t)

    # -------------------------------------------------------------
    # BLOCK 1: UPSTREAM USB INPUT & PROTECTION (25..135, 20..90)
    # -------------------------------------------------------------
    add_text("BLOCK 1: USB-A MALE INPUT & ESD PROTECTION", 25, 20)
    
    # J1
    add_sym("ControlledUsb:USB_A_Plug", "J1", "USB_A_Male", "Connector_USB:USB_A_CNCTech_1001-011-01101_Horizontal", 35, 45, ["1", "2", "3", "4", "5"])
    add_wire(42.62, 42.46, 50, 42.46)
    add_label("VBUS_RAW", 50, 42.46)
    add_wire(42.62, 45.0, 50, 45.0)
    add_label("USB_HOST_DM", 50, 45.0)
    add_wire(42.62, 47.54, 50, 47.54)
    add_label("USB_HOST_DP", 50, 47.54)
    add_wire(42.62, 50.08, 48, 50.08)
    add_pwr("ControlledUsb:GND", "GND", 48, 50.08)
    add_wire(42.62, 52.62, 48, 52.62)
    add_pwr("ControlledUsb:GND", "GND", 48, 52.62)

    # F1
    add_sym("ControlledUsb:Polyfuse", "F1", "PTC 2A", "Fuse:Fuse_1206_3216Metric", 65, 42.46, ["1", "2"], rot=90)
    add_wire(58, 42.46, 61.19, 42.46)
    add_label("VBUS_RAW", 58, 42.46, 180)
    add_wire(68.81, 42.46, 75, 42.46)
    add_pwr("ControlledUsb:+5V", "+5V", 75, 42.46)

    # U7
    add_sym("ControlledUsb:USBLC6-2SC6", "U7", "USBLC6-2SC6", "Package_TO_SOT_SMD:SOT-23-6", 95, 45, ["1", "2", "3", "4", "5", "6"])
    add_wire(84.84, 45.0, 78, 45.0)
    add_label("USB_HOST_DM", 78, 45.0, 180)
    add_wire(84.84, 47.54, 78, 47.54)
    add_label("USB_HOST_DP", 78, 47.54, 180)
    add_wire(95, 39.92, 95, 36)
    add_pwr("ControlledUsb:+5V", "+5V", 95, 36)
    add_wire(95, 55.16, 95, 58)
    add_pwr("ControlledUsb:GND", "GND", 95, 58)

    # C13, C3
    add_sym("ControlledUsb:C_Small", "C13", "10uF", "Capacitor_SMD:C_0603_1608Metric", 115, 45, ["1", "2"])
    add_wire(115, 42.46, 115, 38)
    add_pwr("ControlledUsb:+5V", "+5V", 115, 38)
    add_wire(115, 47.54, 115, 52)
    add_pwr("ControlledUsb:GND", "GND", 115, 52)

    add_sym("ControlledUsb:C_Small", "C3", "100nF", "Capacitor_SMD:C_0603_1608Metric", 125, 45, ["1", "2"])
    add_wire(125, 42.46, 125, 38)
    add_pwr("ControlledUsb:+5V", "+5V", 125, 38)
    add_wire(125, 47.54, 125, 52)
    add_pwr("ControlledUsb:GND", "GND", 125, 52)

    # -------------------------------------------------------------
    # BLOCK 2: 3.3V LDO REGULATOR (145..215, 20..90)
    # -------------------------------------------------------------
    add_text("BLOCK 2: 3.3V SYSTEM POWER (ME6211)", 150, 20)
    add_sym("ControlledUsb:ME6211C33", "U6", "ME6211C33", "Package_TO_SOT_SMD:SOT-23-5", 175, 45, ["1", "2", "3", "4", "5"])
    add_wire(164.84, 45.0, 158, 45.0)
    add_pwr("ControlledUsb:+5V", "+5V", 158, 45.0)
    add_wire(164.84, 50.08, 158, 50.08)
    add_pwr("ControlledUsb:+5V", "+5V", 158, 50.08)
    add_wire(175, 55.16, 175, 58)
    add_pwr("ControlledUsb:GND", "GND", 175, 58)
    add_wire(185.16, 45.0, 192, 45.0)
    add_pwr("ControlledUsb:+3V3", "+3V3", 192, 45.0)

    # C14, C15
    add_sym("ControlledUsb:C_Small", "C14", "10uF", "Capacitor_SMD:C_0603_1608Metric", 150, 45, ["1", "2"])
    add_wire(150, 42.46, 150, 38)
    add_pwr("ControlledUsb:+5V", "+5V", 150, 38)
    add_wire(150, 47.54, 150, 52)
    add_pwr("ControlledUsb:GND", "GND", 150, 52)

    add_sym("ControlledUsb:C_Small", "C15", "10uF", "Capacitor_SMD:C_0603_1608Metric", 200, 45, ["1", "2"])
    add_wire(200, 42.46, 200, 38)
    add_pwr("ControlledUsb:+3V3", "+3V3", 200, 38)
    add_wire(200, 47.54, 200, 52)
    add_pwr("ControlledUsb:GND", "GND", 200, 52)

    # -------------------------------------------------------------
    # BLOCK 3: USB 2.0 HIGH-SPEED HUB (230..390, 20..95)
    # -------------------------------------------------------------
    add_text("BLOCK 3: USB 2.0 HIGH-SPEED HUB (CH334F)", 240, 20)
    add_sym("ControlledUsb:CH334F", "U3", "CH334F", "Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm", 290, 50, ["3", "4", "9", "10", "11", "12", "14", "15", "18", "19", "20", "25"])
    add_wire(284.92, 33.49, 284.92, 30)
    add_pwr("ControlledUsb:+5V", "+5V", 284.92, 30)
    add_wire(295.08, 33.49, 295.08, 30)
    add_label("HUB_V33", 295.08, 30, 90)
    add_wire(290, 69.05, 290, 73)
    add_pwr("ControlledUsb:GND", "GND", 290, 73)

    add_wire(272.22, 42.38, 262, 42.38)
    add_label("USB_HOST_DP", 262, 42.38, 180)
    add_wire(272.22, 44.92, 262, 44.92)
    add_label("USB_HOST_DM", 262, 44.92, 180)
    add_wire(272.22, 62.7, 262, 62.7)
    add_pwr("ControlledUsb:GND", "GND", 262, 62.7)

    # Crystal Y2
    add_sym("ControlledUsb:Crystal_GND24", "Y2", "12.000MHz", "Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm", 250, 56, ["1", "2", "3", "4"])
    add_wire(255.08, 54.73, 272.22, 55.08)
    add_wire(244.92, 54.73, 240, 54.73)
    add_wire(240, 54.73, 240, 65)
    add_wire(240, 65, 268, 65)
    add_wire(268, 65, 268, 57.62)
    add_wire(268, 57.62, 272.22, 57.62)
    add_pwr("ControlledUsb:GND", "GND", 250, 61.08)
    add_pwr("ControlledUsb:GND", "GND", 250, 50.92)

    # Caps C4, C11, C5
    add_sym("ControlledUsb:C_Small", "C4", "100nF", "Capacitor_SMD:C_0603_1608Metric", 325, 35, ["1", "2"])
    add_wire(325, 32.46, 325, 28)
    add_pwr("ControlledUsb:+5V", "+5V", 325, 28)
    add_wire(325, 37.54, 325, 41)
    add_pwr("ControlledUsb:GND", "GND", 325, 41)

    add_sym("ControlledUsb:C_Small", "C11", "1uF", "Capacitor_SMD:C_0603_1608Metric", 340, 35, ["1", "2"])
    add_wire(340, 32.46, 340, 28)
    add_label("HUB_V33", 340, 28, 90)
    add_wire(340, 37.54, 340, 41)
    add_pwr("ControlledUsb:GND", "GND", 340, 41)

    add_sym("ControlledUsb:C_Small", "C5", "100nF", "Capacitor_SMD:C_0603_1608Metric", 355, 35, ["1", "2"])
    add_wire(355, 32.46, 355, 28)
    add_label("HUB_V33", 355, 28, 90)
    add_wire(355, 37.54, 355, 41)
    add_pwr("ControlledUsb:GND", "GND", 355, 41)

    # R1, R2
    add_sym("ControlledUsb:R_Small", "R1", "27R", "Resistor_SMD:R_0603_1608Metric", 325, 42.38, ["1", "2"], rot=90)
    add_wire(307.78, 42.38, 322.46, 42.38)
    add_wire(327.54, 42.38, 335, 42.38)
    add_label("MCU_USB_DP", 335, 42.38)

    add_sym("ControlledUsb:R_Small", "R2", "27R", "Resistor_SMD:R_0603_1608Metric", 325, 44.92, ["1", "2"], rot=90)
    add_wire(307.78, 44.92, 322.46, 44.92)
    add_wire(327.54, 44.92, 335, 44.92)
    add_label("MCU_USB_DM", 335, 44.92)

    # Port 2 to CH440P
    add_wire(307.78, 50.0, 320, 50.0)
    add_label("HUB_PORT2_DP", 320, 50.0)
    add_wire(307.78, 52.54, 320, 52.54)
    add_label("HUB_PORT2_DM", 320, 52.54)

    # -------------------------------------------------------------
    # BLOCK 4: RP2040 MCU CORE & CLOCK (25..120, 110..220)
    # -------------------------------------------------------------
    add_text("BLOCK 4: CONTROLLER MCU (RP2040)", 25, 110)
    add_sym("ControlledUsb:RP2040", "U1", "RP2040", "Package_DFN_QFN:QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm", 75, 160, 
            ["1", "20", "21", "23", "24", "25", "26", "27", "37", "44", "45", "46", "47", "51", "52", "53", "54", "55", "56", "57"])
    
    add_wire(69.92, 137.14, 69.92, 130)
    add_pwr("ControlledUsb:+3V3", "+3V3", 69.92, 130)
    add_wire(75, 137.14, 75, 130)
    add_pwr("ControlledUsb:+3V3", "+3V3", 75, 130)
    add_wire(80.08, 137.14, 80.08, 132)
    add_wire(80.08, 132, 85.08, 132)
    add_wire(85.08, 132, 85.08, 137.14)
    add_wire(82.58, 132, 82.58, 128)
    add_pwr("ControlledUsb:+1V1", "+1V1", 82.58, 128)
    add_wire(75, 187.94, 75, 192)
    add_pwr("ControlledUsb:GND", "GND", 75, 192)

    # USB
    add_wire(52.14, 154.92, 45, 154.92)
    add_label("MCU_USB_DM", 45, 154.92, 180)
    add_wire(52.14, 157.46, 45, 157.46)
    add_label("MCU_USB_DP", 45, 157.46, 180)

    # QSPI
    add_wire(52.14, 162.54, 45, 162.54)
    add_label("QSPI_SS", 45, 162.54, 180)
    add_wire(52.14, 165.08, 45, 165.08)
    add_label("QSPI_SD0", 45, 165.08, 180)
    add_wire(52.14, 167.62, 45, 167.62)
    add_label("QSPI_SD1", 45, 167.62, 180)
    add_wire(52.14, 170.16, 45, 170.16)
    add_label("QSPI_SD2", 45, 170.16, 180)
    add_wire(52.14, 172.7, 45, 172.7)
    add_label("QSPI_SD3", 45, 172.7, 180)
    add_wire(52.14, 175.24, 45, 175.24)
    add_label("QSPI_SCLK", 45, 175.24, 180)

    # Control
    add_wire(52.14, 180.32, 45, 180.32)
    add_label("RUN", 45, 180.32, 180)
    add_wire(97.86, 147.3, 108, 147.3)
    add_label("PWR_EN", 108, 147.3)
    add_wire(97.86, 149.84, 108, 149.84)
    add_label("DATA_OE_N", 108, 149.84)
    add_wire(97.86, 154.92, 108, 154.92)
    add_label("RGB_DIN", 108, 154.92)
    add_wire(97.86, 160.0, 108, 160.0)
    add_label("USER_BTN", 108, 160.0)

    # Crystal Y1 & C1, C2
    add_sym("ControlledUsb:Crystal_GND24", "Y1", "12.000MHz", "Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm", 30, 148.5, ["1", "2", "3", "4"])
    add_wire(35.08, 147.23, 52.14, 147.3)
    add_wire(24.92, 147.23, 20, 147.23)
    add_wire(20, 147.23, 20, 152)
    add_wire(20, 152, 48, 152)
    add_wire(48, 152, 48, 149.84)
    add_wire(48, 149.84, 52.14, 149.84)
    add_pwr("ControlledUsb:GND", "GND", 30, 153.58)
    add_pwr("ControlledUsb:GND", "GND", 30, 143.42)

    add_sym("ControlledUsb:C_Small", "C1", "15pF", "Capacitor_SMD:C_0603_1608Metric", 40, 137, ["1", "2"])
    add_wire(40, 134.46, 40, 130)
    add_wire(40, 130, 45, 130)
    add_wire(45, 130, 45, 147.3)
    add_wire(40, 139.54, 40, 142)
    add_pwr("ControlledUsb:GND", "GND", 40, 142)

    add_sym("ControlledUsb:C_Small", "C2", "15pF", "Capacitor_SMD:C_0603_1608Metric", 22, 137, ["1", "2"])
    add_wire(22, 134.46, 22, 130)
    add_wire(22, 130, 20, 130)
    add_wire(20, 130, 20, 147.23)
    add_wire(22, 139.54, 22, 142)
    add_pwr("ControlledUsb:GND", "GND", 22, 142)

    # -------------------------------------------------------------
    # BLOCK 5: FLASH & TEST PADS (130..195, 110..220)
    # -------------------------------------------------------------
    add_text("BLOCK 5: FLASH MEMORY & PADS", 130, 110)
    add_sym("ControlledUsb:W25Q32", "U2", "W25Q32", "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm", 155, 145, ["1", "2", "3", "4", "5", "6", "7", "8"])
    add_wire(142.3, 142.46, 135, 142.46)
    add_label("QSPI_SS", 135, 142.46, 180)
    add_wire(142.3, 145.0, 135, 145.0)
    add_label("QSPI_SD0", 135, 145.0, 180)
    add_wire(142.3, 147.54, 135, 147.54)
    add_label("QSPI_SD2", 135, 147.54, 180)
    add_wire(142.3, 150.08, 135, 150.08)
    add_label("QSPI_SCLK", 135, 150.08, 180)

    add_wire(167.7, 145.0, 175, 145.0)
    add_label("QSPI_SD1", 175, 145.0)
    add_wire(167.7, 147.54, 175, 147.54)
    add_label("QSPI_SD3", 175, 147.54)
    add_wire(155, 137.38, 155, 133)
    add_pwr("ControlledUsb:+3V3", "+3V3", 155, 133)
    add_wire(155, 155.16, 155, 159)
    add_pwr("ControlledUsb:GND", "GND", 155, 159)

    # Test Pads
    add_sym("ControlledUsb:TestPoint", "TP1", "BOOT", "TestPoint:TestPoint_Pad_D1.0mm", 140, 180, ["1"])
    add_wire(137.46, 180, 130, 180)
    add_label("QSPI_SS", 130, 180, 180)

    add_sym("ControlledUsb:TestPoint", "TP2", "RESET", "TestPoint:TestPoint_Pad_D1.0mm", 155, 180, ["1"])
    add_wire(152.46, 180, 145, 180)
    add_label("RUN", 145, 180, 180)

    add_sym("ControlledUsb:TestPoint", "TP3", "GND", "TestPoint:TestPoint_Pad_D1.0mm", 170, 180, ["1"])
    add_wire(167.46, 180, 162, 180)
    add_pwr("ControlledUsb:GND", "GND", 162, 180)

    # -------------------------------------------------------------
    # BLOCK 6: POWER LOAD SWITCH TPS22918 (205..295, 110..220)
    # -------------------------------------------------------------
    add_text("BLOCK 6: POWER LOAD SWITCH (TPS22918)", 205, 110)
    add_sym("ControlledUsb:TPS22918", "U4", "TPS22918", "Package_TO_SOT_SMD:SOT-23-6", 240, 145, ["1", "2", "3", "4", "5", "6"])
    add_wire(229.84, 145.0, 222, 145.0)
    add_pwr("ControlledUsb:+5V", "+5V", 222, 145.0)
    add_wire(229.84, 150.08, 220, 150.08)
    add_label("PWR_EN", 220, 150.08, 180)
    add_wire(240, 155.16, 240, 160)
    add_pwr("ControlledUsb:GND", "GND", 240, 160)

    add_wire(250.16, 147.54, 255, 147.54)
    add_wire(255, 147.54, 255, 145.0)
    add_wire(250.16, 145.0, 265, 145.0)
    add_label("VBUS_SW", 265, 145.0)

    # R5 & C17
    add_sym("ControlledUsb:R_Small", "R5", "10k", "Resistor_SMD:R_0603_1608Metric", 215, 165, ["1", "2"])
    add_wire(215, 162.46, 215, 150.08)
    add_wire(215, 150.08, 220, 150.08)
    add_wire(215, 167.54, 215, 172)
    add_pwr("ControlledUsb:+5V", "+5V", 215, 172)

    add_sym("ControlledUsb:C_Small", "C17", "10uF", "Capacitor_SMD:C_0603_1608Metric", 275, 155, ["1", "2"])
    add_wire(275, 152.46, 275, 145.0)
    add_wire(275, 145.0, 265, 145.0)
    add_wire(275, 157.54, 275, 162)
    add_pwr("ControlledUsb:GND", "GND", 275, 162)

    # -------------------------------------------------------------
    # BLOCK 7: HIGH-SPEED USB SWITCH CH440P (305..395, 110..220)
    # -------------------------------------------------------------
    add_text("BLOCK 7: USB DATA SWITCH (CH440P)", 310, 110)
    add_sym("ControlledUsb:CH440P", "U5", "CH440P", "Package_SO:TSSOP-16_4.4x5mm_P0.65mm", 350, 145, ["1", "2", "4", "8", "12", "14", "15", "16"])
    add_wire(350, 131.03, 350, 126)
    add_pwr("ControlledUsb:+5V", "+5V", 350, 126)
    add_wire(350, 161.51, 350, 166)
    add_pwr("ControlledUsb:GND", "GND", 350, 166)

    add_wire(334.76, 137.38, 325, 137.38)
    add_pwr("ControlledUsb:GND", "GND", 325, 137.38)
    add_wire(334.76, 139.92, 320, 139.92)
    add_label("DATA_OE_N", 320, 139.92, 180)
    add_wire(334.76, 145.0, 320, 145.0)
    add_label("HUB_PORT2_DP", 320, 145.0, 180)
    add_wire(334.76, 147.54, 320, 147.54)
    add_label("HUB_PORT2_DM", 320, 147.54, 180)

    add_wire(365.24, 145.0, 375, 145.0)
    add_label("SW_DP", 375, 145.0)
    add_wire(365.24, 147.54, 375, 147.54)
    add_label("SW_DM", 375, 147.54)

    # R6
    add_sym("ControlledUsb:R_Small", "R6", "10k", "Resistor_SMD:R_0603_1608Metric", 315, 155, ["1", "2"])
    add_wire(315, 152.46, 315, 139.92)
    add_wire(315, 139.92, 320, 139.92)
    add_wire(315, 157.54, 315, 162)
    add_pwr("ControlledUsb:GND", "GND", 315, 162)

    # -------------------------------------------------------------
    # BLOCK 8: DOWNSTREAM USB-A PORT (270..390, 210..280)
    # -------------------------------------------------------------
    add_text("BLOCK 8: DOWNSTREAM USB-A PORT", 270, 210)
    add_sym("ControlledUsb:USB_A_Receptacle", "J2", "USB_A_Female", "Connector_USB:USB_A_Molex_67643_Horizontal", 340, 240, ["1", "2", "3", "4", "5"])
    add_wire(332.38, 237.46, 320, 237.46)
    add_label("VBUS_SW", 320, 237.46, 180)
    add_wire(332.38, 240.0, 320, 240.0)
    add_label("SW_DM", 320, 240.0, 180)
    add_wire(332.38, 242.54, 320, 242.54)
    add_label("SW_DP", 320, 242.54, 180)
    add_wire(332.38, 245.08, 320, 245.08)
    add_pwr("ControlledUsb:GND", "GND", 320, 245.08)
    add_wire(332.38, 247.62, 320, 247.62)
    add_pwr("ControlledUsb:GND", "GND", 320, 247.62)

    # -------------------------------------------------------------
    # BLOCK 9: USER CONTROLS & RGB LED (25..200, 210..280)
    # -------------------------------------------------------------
    add_text("BLOCK 9: USER CONTROLS & RGB STATUS LED", 25, 210)
    
    # SW1
    add_sym("ControlledUsb:SW_Push", "SW1", "USER_BTN", "Button_Switch_SMD:SW_Push_1P1T_NO_CK_KMR2", 50, 240, ["1", "2"])
    add_wire(44.92, 240.0, 38, 240.0)
    add_label("USER_BTN", 38, 240.0, 180)
    add_wire(55.08, 240.0, 60, 240.0)
    add_pwr("ControlledUsb:GND", "GND", 60, 240.0)

    # D1
    add_sym("ControlledUsb:WS2812B", "D1", "WS2812B", "LED_SMD:LED_WS2812B-2020_PLCC4_2.0x2.0mm", 120, 240, ["1", "2", "3", "4"])
    add_wire(120, 234.92, 120, 230)
    add_pwr("ControlledUsb:+3V3", "+3V3", 120, 230)
    add_wire(120, 250.16, 120, 255)
    add_pwr("ControlledUsb:GND", "GND", 120, 255)
    add_wire(109.84, 242.54, 100, 242.54)
    add_label("RGB_DIN", 100, 242.54, 180)
    add_wire(130.16, 242.54, 138, 242.54)
    add_label("RGB_DOUT", 138, 242.54)

    # Full schematic S-expression
    full_sch = f"""(kicad_sch
	(version 20250114)
	(generator "ControlledUsb_Architect")
	(generator_version "10.0")
	(uuid "{root_uuid}")
	(paper "A3")
	(title_block
		(title "ControlledUsb Dongle (Monolithic Production)")
		(date "2026-10-03")
		(rev "v2.1-Complete")
		(company "ControlledUsb Open Hardware")
		(comment 1 "High-Speed USB 2.0 Host-Controlled Inline Dongle")
		(comment 2 "Architecture: CH334F Hub + RP2040 MCU + TPS22918 + CH440P")
		(comment 3 "Monolithic 62mm Design with SMT Assembly")
	)
{lib_symbols}
{chr(10).join(texts)}
{chr(10).join(wires)}
{chr(10).join(labels)}
{chr(10).join(instances)}
	(sheet_instances
		(path "/"
			(page "1")
		)
	)
	(embedded_fonts no)
)
"""
    output_path = "d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_sch"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_sch)
    print("Full schematic written to:", output_path)

if __name__ == '__main__':
    generate_schematic()


