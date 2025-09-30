import time
import signal
import sys

from plc_reader.libs.client_connector import connect_plc
from plc_reader.libs.signal_reader import read_light_data
from plc_reader.libs.signal_analyzer import analyze_light_data, print_light_data
from plc_reader.libs.interfaces import IResultHandler
from plc_reader.libs.strategy_executor import StrategyExecutor
from plc_reader.libs.impl.api_result_handler import APIResultHandler
from plc_reader.libs.impl.csv_result_handler import CSVResultHandler
from plc_reader.libs.strategy_map_builder import StrategyMapBuilder

from python_voltage_monitor.readers.impl.current_jump_strategy import CurrentJumpStrategy
from python_voltage_monitor.readers.impl.current_smooth_change_strategy import CurrentSmoothChangeStrategy, Direction
from python_voltage_monitor.readers.impl.plc_voltage_reader import PLCVoltageReader
from python_voltage_monitor.services.voltage_service import VoltageReaderService

running = True

def signal_handler(sig, frame):
    global running
    print("\n🛑 停止程式，正在關閉連線...")
    running = False

def main(result_handler: IResultHandler):
    global running
    c = connect_plc()
    if not c:
        sys.exit(1)

    device_strategy_map = (
        StrategyMapBuilder()
        .add_device(
            "PLC-001", # 正常組
            voltage_strategy=CurrentJumpStrategy(lower_bound=-0.97, upper_bound=0.99, interval_sec=0, round_digits=2),
            current_strategy=CurrentJumpStrategy(lower_bound=-0.38, upper_bound=0.41, interval_sec=0, round_digits=2),
        )
        .add_device(
            "PLC-006", # 異常組-跳動策略
            voltage_strategy=CurrentJumpStrategy(lower_bound=30, upper_bound=40, interval_sec=60, round_digits=2),
            current_strategy=CurrentJumpStrategy(lower_bound=10, upper_bound=15, interval_sec=60, round_digits=2)
        )
        .add_device(
            "PLC-008", # 異常組-平滑策略
            voltage_strategy=CurrentSmoothChangeStrategy(step=2.5, jitter=0.5, count=10, round_digits=2, start_delay_sec=25, direction=Direction.DOWN),
            current_strategy=CurrentSmoothChangeStrategy(step=2.0, jitter=0.3, count=10, round_digits=2, start_delay_sec=30, direction=Direction.DOWN)
        )
        .add_device(
            "PLC-010", # 異常組-平滑策略
            voltage_strategy=CurrentSmoothChangeStrategy(step=4.5, jitter=0.6, count=8, round_digits=2, start_delay_sec=45, direction=Direction.UP),
            current_strategy=CurrentSmoothChangeStrategy(step=3.2, jitter=0.4, count=8, round_digits=2, start_delay_sec=45, direction=Direction.UP)
        )
        .build()
    )

    executor = StrategyExecutor(
        device_strategy_map=device_strategy_map,
        allow_types=(float, int),
        result_handler=result_handler
    )

    while running:
        light_sec, coils_y = read_light_data(c)
        result = analyze_light_data(light_sec, coils_y)
        # print_light_data(result)
        
        voltage = result.get("voltage", 220.0)
        current = result.get("current", 5.0)
        executor.execute_for_devices(voltage, current)

        time.sleep(1)

    if c.is_open:
        c.close()
        print("*" * 60)
        print("🔌 已關閉 PLC 連線")
        print("*" * 60)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    print("*" * 60)
    print("🚦 PLC 紅綠燈監控啟動，按 Ctrl+C 可退出")
    print("*" * 60)
    
    main(CSVResultHandler()) # 可換 APIResultHandler
    sys.exit(0)
