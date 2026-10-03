import pcbnew

def wire_board():
    pcb_path = "d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb"
    board = pcbnew.LoadBoard(pcb_path)
    
    net_map = {
        'J1': {'1': '+5V', '2': 'USB_HOST_DM', '3': 'USB_HOST_DP', '4': 'GND', 'S1': 'GND', 'S2': 'GND', 'S3': 'GND', 'S4': 'GND', 'SH': 'GND'},
        'F1': {'1': '+5V', '2': '+5V_FUSED'},
        'U7': {'1': 'USB_HOST_DM', '2': 'GND', '3': 'USB_HOST_DP', '4': 'USB_HOST_DP', '5': '+5V_FUSED', '6': 'USB_HOST_DM'},
        'C13': {'1': '+5V_FUSED', '2': 'GND'},
        'C3': {'1': '+5V_FUSED', '2': 'GND'},
        'U6': {'1': '+5V_FUSED', '2': 'GND', '3': '+5V_FUSED', '5': '+3V3'},
        'C14': {'1': '+5V_FUSED', '2': 'GND'},
        'C15': {'1': '+3V3', '2': 'GND'},
        'U3': {
            '3': 'HUB_XI', '4': 'HUB_XO', '9': 'HUB_PORT2_DM', '10': 'HUB_PORT2_DP',
            '11': 'HUB_PORT1_DM', '12': 'HUB_PORT1_DP', '14': 'USB_HOST_DM', '15': 'USB_HOST_DP',
            '18': 'GND', '19': '+5V_FUSED', '20': 'HUB_V33', '25': 'GND'
        },
        'Y2': {'1': 'HUB_XI', '2': 'GND', '3': 'HUB_XO', '4': 'GND'},
        'C4': {'1': '+5V_FUSED', '2': 'GND'},
        'C11': {'1': 'HUB_V33', '2': 'GND'},
        'C5': {'1': 'HUB_V33', '2': 'GND'},
        'R1': {'1': 'HUB_PORT1_DP', '2': 'MCU_USB_DP'},
        'R2': {'1': 'HUB_PORT1_DM', '2': 'MCU_USB_DM'},
        'SW1': {'1': 'GND', '2': 'USER_BTN', '3': 'GND', '4': 'USER_BTN'},
        'U1': {
            '1': '+3V3', '10': '+3V3', '22': '+3V3', '33': '+3V3', '42': '+3V3', '49': '+3V3',
            '44': '+3V3', '48': '+3V3', '43': '+3V3',
            '23': '+1V1', '50': '+1V1', '45': '+1V1',
            '57': 'GND', '20': 'MCU_XI', '21': 'MCU_XO',
            '46': 'MCU_USB_DM', '47': 'MCU_USB_DP',
            '51': 'QSPI_SS', '52': 'QSPI_SD3', '53': 'QSPI_SD0', '54': 'QSPI_SD2', '55': 'QSPI_SD1', '56': 'QSPI_SCLK',
            '26': 'RUN', '37': 'USER_BTN', '27': 'RGB_DIN', '24': 'PWR_EN', '25': 'DATA_OE_N'
        },
        'Y1': {'1': 'MCU_XI', '2': 'GND', '3': 'MCU_XO', '4': 'GND'},
        'C1': {'1': 'MCU_XI', '2': 'GND'},
        'C2': {'1': 'MCU_XO', '2': 'GND'},
        'U2': {'1': 'QSPI_SS', '2': 'QSPI_SD1', '3': 'QSPI_SD2', '4': 'GND', '5': 'QSPI_SD0', '6': 'QSPI_SCLK', '7': 'QSPI_SD3', '8': '+3V3'},
        'D1': {'1': '+3V3', '2': 'RGB_DOUT', '3': 'GND', '4': 'RGB_DIN'},
        'TP1': {'1': 'QSPI_SS'},
        'TP2': {'1': 'RUN'},
        'TP3': {'1': 'GND'},
        'U4': {'1': '+5V_FUSED', '2': 'GND', '3': 'PWR_EN', '5': 'VBUS_SW', '6': 'VBUS_SW'},
        'R5': {'1': '+5V_FUSED', '2': 'PWR_EN'},
        'U5': {'1': 'GND', '2': 'SW_DP', '4': 'HUB_PORT2_DP', '8': 'GND', '12': 'HUB_PORT2_DM', '14': 'SW_DM', '15': 'DATA_OE_N', '16': '+5V_FUSED'},
        'R6': {'1': 'DATA_OE_N', '2': 'GND'},
        'C17': {'1': 'VBUS_SW', '2': 'GND'},
        'J2': {'1': 'VBUS_SW', '2': 'SW_DM', '3': 'SW_DP', '4': 'GND', 'S1': 'GND', 'S2': 'GND', 'S3': 'GND', 'S4': 'GND', 'SH': 'GND'}
    }

    def get_net(name):
        net = board.FindNet(name)
        if not net:
            net = pcbnew.NETINFO_ITEM(board, name)
            board.Add(net)
        return net

    # Assign nets
    for ref, pins in net_map.items():
        fp = board.FindFootprintByReference(ref)
        if not fp:
            print(f"Warning: Footprint {ref} not found.")
            continue
        for pad in fp.Pads():
            pad_num = pad.GetPadName()
            if pad_num in pins:
                net_name = pins[pad_num]
                pad.SetNet(get_net(net_name))
            elif pad_num == 'SH' or pad_num.startswith('S'):
                if ref in ['J1', 'J2']:
                    pad.SetNet(get_net('GND'))

    pcbnew.SaveBoard(pcb_path, board)
    print("Electrical netlist successfully injected!")

if __name__ == '__main__':
    wire_board()
