import csv
import datetime
import os
from plc_reader.libs.interfaces import IResultHandler

CSV_PATH = "csv/device_data.csv"

class CSVResultHandler(IResultHandler):
    def __init__(self, filepath: str = CSV_PATH):
        self.filepath = filepath
        folder = os.path.dirname(filepath)
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)

    def handle(self, device_id: str, voltage: float, current: float) -> None:
        timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")
        with open(self.filepath, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([device_id, voltage, current, timestamp])
        # print(f"📄 [CSV] 已寫入 {self.filepath}")
