import datetime
from concurrent.futures import ThreadPoolExecutor
from src.call.api import post_plc
from plc_reader.libs.interfaces import IResultHandler

MAX_WORKERS = 3
executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

class APIResultHandler(IResultHandler):
    def handle(self, device_id: str, voltage: float, current: float) -> None:
        executor.submit(self.worker, device_id, voltage, current)

    def worker(self, device_id: str, voltage: float, current: float):
        try:
            timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")
            result = post_plc(device_id, voltage, current, timestamp)
            print(f"🌐 [非同步] API 呼叫完成！回傳：{result}")
        except Exception as e:
            print(f"❌ [非同步] API 呼叫失敗: {e}")
