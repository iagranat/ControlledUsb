import pcbnew
board = pcbnew.LoadBoard('d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb')
try:
    pcbnew.ImportSpecctraSES(board, 'd:/Projects/ControlledUsb/hardware/ControlledUsb.ses')
    pcbnew.SaveBoard('d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb', board)
    print('SES imported successfully')
except Exception as e:
    print('Failed to import SES:', e)
