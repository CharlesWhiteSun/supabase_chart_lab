import pytest

from python_voltage_monitor.readers.impl.plc_voltage_reader import PLCVoltageReader
from python_voltage_monitor.services.voltage_service import VoltageService


def test_plc_voltage_reader_single_value():
    reader = PLCVoltageReader()
    service = VoltageService(reader)

    # 模擬一筆資料
    voltage = reader.read_voltage()
    assert isinstance(voltage, float), "Voltage 應該要是 float"


def test_voltage_service_process_values():
    reader = PLCVoltageReader()
    service = VoltageService(reader)

    values = [220.1, 221.0, 219.9]
    result = service.process(values)

    assert isinstance(result, dict), "結果應該要是 dict"
    assert "average" in result, "應包含平均電壓"
    assert abs(result["average"] - sum(values)/len(values)) < 0.01
