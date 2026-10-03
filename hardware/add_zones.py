import pcbnew

def add_copper_fills():
    pcb_path = "d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb"
    board = pcbnew.LoadBoard(pcb_path)
    
    net_gnd = board.FindNet("GND")

    pts = [
        pcbnew.VECTOR2I(int(95 * 1e6), int(95 * 1e6)),
        pcbnew.VECTOR2I(int(170 * 1e6), int(95 * 1e6)),
        pcbnew.VECTOR2I(int(170 * 1e6), int(125 * 1e6)),
        pcbnew.VECTOR2I(int(95 * 1e6), int(125 * 1e6))
    ]
    
    layers = [pcbnew.F_Cu, pcbnew.In1_Cu, pcbnew.In2_Cu, pcbnew.B_Cu]
    
    for layer in layers:
        zone = pcbnew.ZONE(board)
        zone.SetLayer(layer)
        zone.SetNet(net_gnd)
        
        poly = pcbnew.SHAPE_POLY_SET()
        poly.NewOutline()
        for pt in pts:
            poly.Append(pt.x, pt.y)
        
        zone.SetOutline(poly)
        zone.SetIsRuleArea(False)
        
        board.Add(zone)

    filler = pcbnew.ZONE_FILLER(board)
    filler.Fill(board.Zones())
    
    pcbnew.SaveBoard(pcb_path, board)
    print("Added and filled GND zones on 4 layers!")

if __name__ == '__main__':
    add_copper_fills()
