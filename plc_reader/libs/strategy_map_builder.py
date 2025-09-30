from typing import Dict, Tuple
from python_voltage_monitor.readers.interfaces import ICurrentProcessingStrategy


class StrategyMapBuilder:
    def __init__(self):
        self._map: Dict[str, Tuple[ICurrentProcessingStrategy, ICurrentProcessingStrategy]] = {}

    def add_device(
        self,
        device_id: str,
        voltage_strategy: ICurrentProcessingStrategy,
        current_strategy: ICurrentProcessingStrategy
    ) -> "StrategyMapBuilder":
        """
        新增裝置的電壓與電流策略

        :param device_id: 裝置 ID
        :param voltage_strategy: 電壓策略物件
        :param current_strategy: 電流策略物件
        :return: self（方便鏈式調用）
        """
        self._map[device_id] = (voltage_strategy, current_strategy)
        return self

    def build(self) -> Dict[str, Tuple[ICurrentProcessingStrategy, ICurrentProcessingStrategy]]:
        return self._map
