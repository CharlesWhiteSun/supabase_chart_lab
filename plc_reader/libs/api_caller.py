import datetime
from concurrent.futures import ThreadPoolExecutor
from supabase_chart_lab.call.api import post_plc

# 建立 ThreadPoolExecutor，固定最大執行緒數
MAX_WORKERS = 3
executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

def worker(device_id, voltage, current):
    """實際呼叫 API 的工作者"""
    try:
        timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")
        result = post_plc(device_id, voltage, current, timestamp)
        print(f"🌐 [非同步] API 呼叫完成！回傳：{result}")
    except Exception as e:
        print(f"❌ [非同步] API 呼叫失敗: {e}")

def async_api_call(device_id="PLC-TEST", voltage=220.5, current=5.5):
    """
    將 API 呼叫任務提交給 ThreadPoolExecutor，
    Executor 內部會管理佇列與執行緒。
    """
    executor.submit(worker, device_id, voltage, current)
