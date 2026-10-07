import os
import zipfile
import subprocess
import pcbnew

def generate_production_package():
    proj_dir = os.path.dirname(os.path.abspath(__file__))
    pcb_path = os.path.join(proj_dir, "ControlledUsb.kicad_pcb")
    gerber_dir = os.path.join(proj_dir, "gerbers")
    os.makedirs(gerber_dir, exist_ok=True)

    # Clean existing gerber folder
    for f in os.listdir(gerber_dir):
        os.remove(os.path.join(gerber_dir, f))

    board = pcbnew.LoadBoard(pcb_path)
    pctl = pcbnew.PLOT_CONTROLLER(board)
    popt = pctl.GetPlotOptions()

    popt.SetOutputDirectory(gerber_dir)
    popt.SetPlotFrameRef(False)
    popt.SetAutoScale(False)
    popt.SetScale(1.0)
    popt.SetMirror(False)
    popt.SetUseGerberAttributes(True)
    popt.SetUseGerberProtelExtensions(True)
    popt.SetSubtractMaskFromSilk(True)
    popt.SetCreateGerberJobFile(True)
    popt.SetDrillMarksType(pcbnew.DRILL_MARKS_NO_DRILL_SHAPE)

    layers = [
        ("F_Cu", pcbnew.F_Cu),
        ("In1_Cu", pcbnew.In1_Cu),
        ("In2_Cu", pcbnew.In2_Cu),
        ("B_Cu", pcbnew.B_Cu),
        ("F_SilkS", pcbnew.F_SilkS),
        ("B_SilkS", pcbnew.B_SilkS),
        ("F_Mask", pcbnew.F_Mask),
        ("B_Mask", pcbnew.B_Mask),
        ("F_Paste", pcbnew.F_Paste),
        ("B_Paste", pcbnew.B_Paste),
        ("Edge_Cuts", pcbnew.Edge_Cuts),
    ]

    for name, layer_id in layers:
        pctl.SetLayer(layer_id)
        pctl.OpenPlotfile(name, pcbnew.PLOT_FORMAT_GERBER, name)
        pctl.PlotLayer()
        pctl.ClosePlot()
        print(f"Plotted {name}")

    # Generate Excellon Drill Files
    drill_writer = pcbnew.EXCELLON_WRITER(board)
    drill_writer.SetFormat(True, pcbnew.EXCELLON_WRITER.DECIMAL_FORMAT)
    drill_writer.SetOptions(False, False, pcbnew.VECTOR2I(0, 0), True)
    drill_writer.CreateDrillandMapFilesSet(gerber_dir, True, False)
    print("Generated Drill files")

    # Zip Gerbers
    zip_path = os.path.join(proj_dir, "ControlledUsb_Gerbers.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(gerber_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, arcname=file)
    print(f"Created {zip_path} ({os.path.getsize(zip_path)} bytes)")

if __name__ == "__main__":
    generate_production_package()
