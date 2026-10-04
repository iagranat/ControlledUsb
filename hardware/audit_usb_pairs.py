import pcbnew

board = pcbnew.LoadBoard('d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb')

usb_nets = ['USB_HOST_DP', 'USB_HOST_DM', 'HUB_PORT1_DP', 'HUB_PORT1_DM', 'MCU_USB_DP', 'MCU_USB_DM', 'HUB_PORT2_DP', 'HUB_PORT2_DM', 'SW_DP', 'SW_DM']

print("=== USB Tracks and Vias Audit ===")
for net_name in usb_nets:
    net = board.FindNet(net_name)
    if not net:
        print(f"{net_name}: NET NOT FOUND")
        continue
    
    tracks = [t for t in board.GetTracks() if t.GetNetname() == net_name]
    segments = [t for t in tracks if isinstance(t, pcbnew.PCB_TRACK) and not isinstance(t, pcbnew.PCB_VIA)]
    vias = [t for t in tracks if isinstance(t, pcbnew.PCB_VIA)]
    
    total_len = sum(s.GetLength() for s in segments) / 1e6
    layers = set(s.GetLayerName() for s in segments)
    
    print(f"{net_name:15}: Len = {total_len:6.2f} mm | Layers: {','.join(layers)} | Vias: {len(vias)}")
