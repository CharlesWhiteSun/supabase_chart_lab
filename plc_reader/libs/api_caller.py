import threading
import time
from supabase_chart_lab.call.api import post_plc
import datetime

def async_api_call():
    """非同步呼叫 API"""
    def worker():
        timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")
        device_id = "PLC-TEST"
        voltage = 220.5
        current = 5.5

        result = post_plc(device_id, voltage, current, timestamp)
        print("🌐 [非同步] API 呼叫完成！回傳：", result)

    thread = threading.Thread(target=worker)
    thread.daemon = True  # 主程式退出時自動結束
    thread.start()
