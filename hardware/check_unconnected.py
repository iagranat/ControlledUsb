import pcbnew
board = pcbnew.LoadBoard('d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb')
unconnected = []
for fp in board.GetFootprints():
    for pad in fp.Pads():
        if pad.GetNetname() == '':
            unconnected.append(f"{fp.GetReference()}-{pad.GetPadName()}")
print(f"Unconnected pads: {unconnected}")
