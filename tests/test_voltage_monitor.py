from python_voltage_monitor.readers.impl.plc_voltage_reader import PLCVoltageReader
from python_voltage_monitor.services.voltage_service import VoltageReaderService


def test_plc_voltage_reader_single_value():
    reader = PLCVoltageReader()
    service = VoltageReaderService(reader)

    voltage = reader.read(220.5)[0]  # 因為 read() 回傳 tuple，需要取第一個元素
    assert isinstance(voltage, float), "Voltage 應該要是 float"


def test_voltage_service_process_values():
    reader = PLCVoltageReader()
    service = VoltageReaderService(reader)

    values = [220.1, 221.0, 219.9]
    readings = service.collect(values)  # collect() 回傳 tuple

    assert isinstance(readings, tuple), "結果應該要是 tuple"
    assert all(isinstance(v, float) for v in readings), "所有值都應該是 float"
    assert readings == tuple(values), "回傳的值應與輸入一致"

    # 手動計算平均值，並檢查
    average = sum(readings) / len(readings)
    assert abs(average - sum(values) / len(values)) < 0.01, "平均值計算錯誤"
