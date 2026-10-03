import uuid
import os

def gen_uuid():
    return str(uuid.uuid4())

def generate_kicad_sch(output_path):
    # Generates a valid KiCad 7/8 schematic S-expression file
    sch_content = f"""(kicad_sch
  (version 20231120)
  (generator "ControlledUsb_Generator")
  (generator_version "8.0")
  (uuid "{gen_uuid()}")
  (paper "A3")
  (title_block
    (title "ControlledUsb Dongle (Monolithic)")
    (date "2026-10-01")
    (rev "v1.0")
    (company "ControlledUsb Open Hardware")
    (comment 1 "High-Speed USB 2.0 Host-Controlled Interrupter")
    (comment 2 "Architecture: CH334F Hub + RP2040 MCU + TPS22918 + CH440P")
  )
  (lib_symbols
  )
  (sheet_instances
    (path "/"
      (page "1")
    )
  )
)
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(sch_content)
    print(f"Generated schematic: {output_path}")

if __name__ == "__main__":
    generate_kicad_sch("d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_sch")
