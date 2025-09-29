from pyModbusTCP.client import ModbusClient

HOST = '192.168.16.84'
PORT = 502

def connect_plc():
    """建立與 PLC 的連線"""
    c = ModbusClient(host=HOST, port=PORT, unit_id=1, auto_open=True)
    if not c.is_open:
        if c.open():
            print("✅ 連線成功")
            print("-" * 40)
        else:
            print("❌ 無法連線到 PLC")
            print("-" * 40)
            return None
    return c
