# Simple register simulation module.
# register_map holds 8-bit registers keyed by address.
register_map = {0x01: 0b00000000}

def read_register_map():
    """Return the register map (used by UI to display value)."""
    return register_map

def set_tx_rate(rate):
    """
    Modify register 0x01 TX_RATE bits based on selected transmission rate.
    Bit numbering (0 = LSB):
     - TX_RATE[0] -> bit 1
     - TX_RATE[1] -> bit 2

    For "3Gbps": TX_RATE[0]=1, TX_RATE[1]=0
    For "6Gbps": TX_RATE[0]=0, TX_RATE[1]=1
    """
    if 0x01 not in register_map:
        register_map[0x01] = 0

    if rate == "3Gbps":
        # set bit1 = 1, bit2 = 0
        register_map[0x01] = (register_map[0x01] | (1 << 1)) & ~(1 << 2)
    elif rate == "6Gbps":
        # set bit1 = 0, bit2 = 1
        register_map[0x01] = (register_map[0x01] & ~(1 << 1)) | (1 << 2)
    else:
        return

    print(f"[REGISTER] 0x01 updated: {bin(register_map[0x01])}")
