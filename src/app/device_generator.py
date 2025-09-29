import random
import time
from typing import List, Dict
from datetime import datetime, timezone


def generate_device_data(device_id: str, voltage_range: List[float], current_range: List[float], delay: float) -> Dict:
    """
    為設備產生隨機電壓與電流數值
    """
    time.sleep(delay)
    voltage = round(random.uniform(*voltage_range), 2)
    current = round(random.uniform(*current_range), 2)

     # 產生 ISO 8601 格式時間戳
    timestamp = datetime.now(timezone.utc).isoformat()

    return {
        "device_id": device_id,
        "voltage": voltage,
        "current": current,
        "timestamp": timestamp
    }
