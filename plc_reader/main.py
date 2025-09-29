import time
import signal
import sys

from plc_reader.libs.client_connector import connect_plc
from plc_reader.libs.signal_reader import read_light_data
from plc_reader.libs.signal_analyzer import analyze_light_data, print_light_data
from plc_reader.libs.api_caller import async_api_call

running = True

def signal_handler(sig, frame):
    global running
    print("\n🛑 停止程式，正在關閉連線...")
    running = False

def main():
    global running
    c = connect_plc()
    if not c:
        sys.exit(1)

    while running:
        light_sec, coils_y = read_light_data(c)
        result = analyze_light_data(light_sec, coils_y)
        print_light_data(result)
        async_api_call() # 非同步呼叫 API
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
    main()
    sys.exit(0)
