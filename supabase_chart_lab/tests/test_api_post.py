import requests
import datetime

BASE_URL = "http://127.0.0.1:9000"

def test_post_plc_status():
    url = f"{BASE_URL}/plc"
    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S%z")

    payload = {
        "device_id": "PLC-TEST",
        "voltage": 220.5,
        "current": 5.5,
        "timestamp": timestamp,
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "status" in data
    assert data["status"] == "success"

    print("✅ POST /plc 測試成功，status:", data["status"])
