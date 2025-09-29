import yaml
from typing import Dict


def load_config(config_path: str) -> Dict:
    """讀取 YAML 設定檔，回傳配置資料"""
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config
