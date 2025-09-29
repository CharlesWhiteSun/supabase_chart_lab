ADDRESS = 0x1000        # Holding Register 起始地址
NUMBERS = 3             # 讀取數量
PLC_Type = "12SE"       # "12SE" or "26SE"
COILS_Y_12SE = 0x513    # Y23, Y24, Y25
COILS_Y_26SE = 0x506    # Y6, Y7, Y10

def read_light_data(c) -> tuple:
    """
    讀取 PLC 的秒數與輸出燈號 bit
    
    Args:
        c (ModbusClient): 已連線的 ModbusClient 物件
    Returns:
        tuple: 包含秒數列表與燈號狀態列表
    """
    light_sec = c.read_holding_registers(ADDRESS, NUMBERS)

    if PLC_Type == "12SE":
        coils_y = c.read_coils(COILS_Y_12SE, NUMBERS)  # Y23, Y24, Y25
    else:
        coils_y = c.read_coils(COILS_Y_26SE, NUMBERS)  # Y6, Y7, Y10

    return light_sec, coils_y
