def address_to_str(address: int) -> str:
    return f"0x{address:0>16x}"


def address_to_int(address: str) -> int:
    return int(address, base=16)
