import pcbnew

board = pcbnew.LoadBoard('d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb')
net_gnd = board.FindNet('GND')

for ref in ['J1', 'J2']:
    fp = board.FindFootprintByReference(ref)
    if fp:
        for pad in fp.Pads():
            if pad.GetPadName() == '' or pad.GetPadName().startswith('M'):
                pad.SetNet(net_gnd)

pcbnew.SaveBoard('d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb', board)
