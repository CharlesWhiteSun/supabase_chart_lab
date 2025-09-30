def analyze_light_data(light_sec, coils_y):
    """分析秒數與燈號內容，回傳 dict"""
    result = {
        "green_sec": None,
        "yellow_sec": None,
        "red_sec": None,
        "current_light": None,
        "errors": [],
        
        "voltage": None,
        "current": None
    }

    if light_sec:
        result["green_sec"] = light_sec[0] / 10
        result["yellow_sec"] = light_sec[1] / 10
        result["red_sec"] = light_sec[2] / 10

        result["voltage"] = 220 # 模擬電壓
        result["current"] = 5   # 模擬電流
    else:
        result["errors"].append("⚠️ PLC 資料讀取失敗")

    if coils_y:
        if coils_y[0]:
            result["current_light"] = "綠燈"
        elif coils_y[1]:
            result["current_light"] = "黃燈"
        elif coils_y[2]:
            result["current_light"] = "紅燈"
        else:
            result["current_light"] = "無輸出"
    else:
        result["errors"].append("⚠️ PLC Y 輸出讀取失敗")

    return result

def print_light_data(data):
    """將分析結果印出"""
    if data["green_sec"] is not None:
        print(f"綠燈: {data['green_sec']} 秒, 黃燈: {data['yellow_sec']} 秒, 紅燈: {data['red_sec']} 秒, 電壓: {data['voltage']} V, 電流: {data['current']} A")

    if data["current_light"]:
        print(f"目前燈號: {data['current_light']}")

    if data["errors"]:
        for err in data["errors"]:
            print(err)

    print("-" * 40)
