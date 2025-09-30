from typing import Iterable, Dict, Type, Tuple
from python_voltage_monitor.readers.interfaces import ICurrentProcessingStrategy
from python_voltage_monitor.readers.impl.plc_voltage_reader import PLCVoltageReader
from python_voltage_monitor.services.voltage_service import VoltageReaderService
from plc_reader.libs.interfaces import IResultHandler


class StrategyExecutor:
    def __init__(
        self,
        device_strategy_map: Dict[str, Tuple[ICurrentProcessingStrategy, ICurrentProcessingStrategy]],
        allow_types: Iterable[Type],
        result_handler: IResultHandler
    ):
        """
        device_strategy_map: 裝置 ID → (voltage_strategy, current_strategy)
        allow_types: 允許的數值型別
        result_handler: 結果處理器
        """
        self.device_strategy_map = device_strategy_map
        self.allow_types = allow_types
        self.result_handler = result_handler

    def execute_for_devices(
        self,
        voltage: float,
        current: float
    ) -> None:
        for device_id, (voltage_strategy, current_strategy) in self.device_strategy_map.items():
            # voltage 處理
            voltage_reader = PLCVoltageReader(allow_types=self.allow_types, strategy=voltage_strategy)
            voltage_service = VoltageReaderService(voltage_reader)
            processed_voltage = voltage_service.collect([voltage])[0]

            # current 處理
            current_reader = PLCVoltageReader(allow_types=self.allow_types, strategy=current_strategy)
            current_service = VoltageReaderService(current_reader)
            processed_current = current_service.collect([current])[0]

            # 處理結果
            self.result_handler.handle(device_id, processed_voltage, processed_current)
