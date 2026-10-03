import pcbnew
board = pcbnew.LoadBoard('d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb')
pcbnew.ExportSpecctraDSN(board, 'd:/Projects/ControlledUsb/hardware/ControlledUsb.dsn')
print('Exported DSN')
