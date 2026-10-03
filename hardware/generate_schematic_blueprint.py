import uuid
import os

def uid():
    return str(uuid.uuid4())

def generate():
    sch = f"""(kicad_sch
  (version 20231120)
  (generator "ControlledUsb_Builder")
  (generator_version "10.0")
  (uuid "{uid()}")
  (paper "A3")
  (title_block
    (title "ControlledUsb Dongle (Monolithic Production)")
    (date "2026-10-01")
    (rev "v1.0")
    (company "ControlledUsb Open Hardware")
    (comment 1 "High-Speed USB 2.0 Host-Controlled Extension Dongle")
    (comment 2 "CH334F Hub + RP2040 MCU + TPS22918 Power Switch + CH440P Data Switch")
    (comment 3 "Designed for JLCPCB 4-Layer SMT Assembly (Target < $55 USD / 5 pcs)")
  )

  (sheet_instances
    (path "/"
      (page "1")
    )
  )

  (text "BLOCK 1: HOST USB-A MALE INPUT & ESD PROTECTION" (at 25.4 25.4 0) (effects (font (size 2.5 2.5) (bold yes))))
  (text "BLOCK 2: 3.3V SYSTEM POWER (ME6211 LDO)" (at 140 25.4 0) (effects (font (size 2.5 2.5) (bold yes))))
  (text "BLOCK 3: USB 2.0 HIGH-SPEED HUB (CH334F)" (at 250 25.4 0) (effects (font (size 2.5 2.5) (bold yes))))
  (text "BLOCK 4: CONTROLLER MCU (RP2040 & 4MB FLASH)" (at 25.4 120 0) (effects (font (size 2.5 2.5) (bold yes))))
  (text "BLOCK 5: POWER LOAD SWITCH (TPS22918)" (at 180 120 0) (effects (font (size 2.5 2.5) (bold yes))))
  (text "BLOCK 6: HIGH-SPEED USB SWITCH (CH440P)" (at 270 120 0) (effects (font (size 2.5 2.5) (bold yes))))
  (text "BLOCK 7: DOWNSTREAM USB-A EXTENSION PORT" (at 270 200 0) (effects (font (size 2.5 2.5) (bold yes))))
  (text "BLOCK 8: USER BUTTON & RGB NEOPIXEL STATUS LED" (at 25.4 240 0) (effects (font (size 2.5 2.5) (bold yes))))

  (label "VBUS_RAW" (at 45 40 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))
  (label "+5V" (at 75 40 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))
  (label "GND" (at 45 65 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))
  (label "USB_HOST_DP" (at 45 45 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))
  (label "USB_HOST_DM" (at 45 50 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))

  (label "+3V3" (at 180 40 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))
  (label "+1V1" (at 85 170 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))

  (label "HUB_DP1" (at 300 45 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))
  (label "HUB_DM1" (at 300 50 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))
  (label "HUB_DP2" (at 300 65 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))
  (label "HUB_DM2" (at 300 70 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))

  (label "PWR_EN" (at 100 145 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))
  (label "DATA_OE#" (at 100 150 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))
  (label "USER_BTN" (at 100 155 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))
  (label "WS2812_DATA" (at 100 160 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))

  (label "VBUS_SW" (at 235 140 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))
  (label "SW_USB_DP" (at 330 140 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))
  (label "SW_USB_DM" (at 330 145 0) (fields_autoplaced yes) (effects (font (size 1.27 1.27))))
)
"""
    output_path = "d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_sch"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(sch)
    print(f"Generated schematic layout: {output_path}")

if __name__ == "__main__":
    generate()
