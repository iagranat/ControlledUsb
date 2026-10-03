import os

def create_sym_lib_table(proj_dir):
    content = """(sym_lib_table
  (version 7)
  (lib (name "ControlledUsb")(type "KiCad")(uri "${KIPRJMOD}/ControlledUsb.kicad_sym")(options "")(descr "Project Custom Symbols"))
)
"""
    path = os.path.join(proj_dir, "sym-lib-table")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {path}")

if __name__ == "__main__":
    create_sym_lib_table("d:/Projects/ControlledUsb/hardware")
