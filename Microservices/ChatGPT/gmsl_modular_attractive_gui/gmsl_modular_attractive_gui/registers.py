# Register simulation module for the GUI
register_map = {0x01: 0b00000000}

def read_register(addr=0x01):
    return register_map.get(addr, 0)

def set_tx_rate(rate):
    """Set TX_RATE bits in register 0x01 based on rate.
    bit1 -> TX_RATE[0]
    bit2 -> TX_RATE[1]
    """
    if 0x01 not in register_map:
        register_map[0x01] = 0
    if rate == '3Gbps':
        register_map[0x01] = (register_map[0x01] | (1 << 1)) & ~(1 << 2)
    elif rate == '6Gbps':
        register_map[0x01] = (register_map[0x01] & ~(1 << 1)) | (1 << 2)
    return register_map[0x01]
