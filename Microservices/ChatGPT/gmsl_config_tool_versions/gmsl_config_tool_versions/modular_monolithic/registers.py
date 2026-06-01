# Simple register simulation module.
register_map = {0x01: 0b00000000}

def read_register_map():
    return register_map

def set_tx_rate(rate):
    if 0x01 not in register_map:
        register_map[0x01] = 0

    if rate == "3Gbps":
        register_map[0x01] = (register_map[0x01] | (1 << 1)) & ~(1 << 2)
    elif rate == "6Gbps":
        register_map[0x01] = (register_map[0x01] & ~(1 << 1)) | (1 << 2)
    else:
        return

    print(f"[REGISTER] 0x01 updated: {bin(register_map[0x01])}")
