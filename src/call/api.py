import requests
import datetime

BASE_URL = "http://127.0.0.1:9000"

def get_plc():
    """呼叫 GET /plc API"""
    try:
        url = f"{BASE_URL}/plc"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ GET /plc 失敗: {e}")
        return None

def post_plc(device_id: str, voltage: float, current: float, timestamp: str = None):
    """呼叫 POST /plc API"""
    try:
        url = f"{BASE_URL}/plc"
        if not timestamp:
            timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")

        payload = {
            "device_id": device_id,
            "voltage": voltage,
            "current": current,
            "timestamp": timestamp
        }

        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ POST /plc 失敗: {e}")
        return None
