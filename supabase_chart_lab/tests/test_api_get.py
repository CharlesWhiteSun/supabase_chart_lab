import requests

BASE_URL = "http://127.0.0.1:9000"

def test_get_plc_status():
    url = f"{BASE_URL}/plc"
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0

    print("✅ GET /plc 測試成功，回傳資料：", data)
