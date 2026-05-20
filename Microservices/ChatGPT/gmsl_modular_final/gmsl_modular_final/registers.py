# registers.py
# simple simulated register map (8-bit registers)
_registers = {0x01: 0b00000000}

def read_register(addr=0x01):
    return _registers.get(addr, 0)

def set_tx_rate_bits(speed):
    """
    Update register 0x01 TX_RATE bits:
      - TX_RATE[0] -> bit 1
      - TX_RATE[1] -> bit 2
    For 3Gbps -> bit1=1, bit2=0
    For 6Gbps -> bit1=0, bit2=1
    Returns new value.
    """
    addr = 0x01
    v = _registers.get(addr, 0)
    if speed == "3Gbps":
        v = (v | (1 << 1)) & ~(1 << 2)
    elif speed == "6Gbps":
        v = (v & ~(1 << 1)) | (1 << 2)
    _registers[addr] = v
    return v
