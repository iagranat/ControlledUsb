import os
import json
import csv

def generate_kicad_project(base_dir):
    os.makedirs(base_dir, exist_ok=True)
    
    proj_name = "ControlledUsb"
    pro_path = os.path.join(base_dir, f"{proj_name}.kicad_pro")
    sch_path = os.path.join(base_dir, f"{proj_name}.kicad_sch")
    bom_path = os.path.join(base_dir, "BOM_JLCPCB.csv")
    
    # 1. Generate .kicad_pro
    pro_data = {
        "board": {
            "3dviewports": [],
            "design_settings": {
                "boundary_edge_to_copper": 0.5,
                "copper_line_width": 0.15,
                "copper_ring_width": 0.15,
                "copper_to_hole": 0.25,
                "copper_to_line": 0.15,
                "drill_size": 0.3,
                "hole_size": 0.3,
                "min_clearance": 0.127,
                "min_copper_edge_clearance": 0.3,
                "min_hole_clearance": 0.25,
                "min_through_hole_annular_ring": 0.15,
                "min_track_width": 0.127,
                "track_width": 0.2,
                "via_dia": 0.6,
                "via_drill": 0.3
            },
            "layer_presets": [],
            "viewports": []
        },
        "boards": [],
        "cvpcb": {
            "equivalence_files": []
        },
        "libraries": {
            "pinned_footprint_libs": [],
            "pinned_symbol_libs": []
        },
        "meta": {
            "filename": f"{proj_name}.kicad_pro",
            "version": 1
        },
        "net_selector": {
            "filters": []
        },
        "pcbnew": {
            "last_paths": {
                "gencad": "",
                "idf": "",
                "netlist": "",
                "plot": "",
                "pos": "",
                "specctra_dsn": "",
                "step": "",
                "svg": "",
                "vrml": ""
            }
        },
        "schematic": {
            "annotate_start_num": 1,
            "drawing": {
                "dashed_lines_dash_length_ratio": 12.0,
                "dashed_lines_gap_length_ratio": 3.0,
                "default_line_thickness": 6.0,
                "default_text_size": 50.0,
                "field_names": [],
                "intersheets_ref_own_page": False,
                "intersheets_ref_prefix": "",
                "intersheets_ref_short": False,
                "intersheets_ref_show": False,
                "intersheets_ref_suffix": "",
                "junction_size_choice": 3,
                "label_size_ratio": 0.375,
                "pin_symbol_size": 25.0,
                "text_offset_ratio": 0.15
            },
            "legacy_lib_dir": "",
            "legacy_lib_list": []
        },
        "sheets": [
            [
                "00000000-0000-0000-0000-000000000000",
                ""
            ]
        ]
    }
    
    with open(pro_path, "w", encoding="utf-8") as f:
        json.dump(pro_data, f, indent=2)
        
    print(f"Created: {pro_path}")

if __name__ == "__main__":
    generate_kicad_project("d:/Projects/ControlledUsb/hardware")
