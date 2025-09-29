import time
from typing import Dict, List
from src.app.device_generator import generate_device_data


def read_multiple_devices(config: Dict, duration: float) -> List[Dict]:
    """
    讀取多個設備的數值
    """
    results = []
    start_time = time.time()
    while time.time() - start_time < duration:
        for device in config["devices"]:
            data = generate_device_data(
                device_id=device["id"],
                voltage_range=device["voltage_range"],
                current_range=device["current_range"],
                delay=device.get("delay", 0)
            )
            print(f"Generated: {data}")
            results.append(data)
    return results
