from src.app.config import load_config
from src.app.device_reader import read_multiple_devices


if __name__ == "__main__":
    config_path = "config.yml"
    config = load_config(config_path)

    duration = config.get("duration", 10)
    print(f"Start reading data for {duration} seconds...")

    all_data = read_multiple_devices(config, duration)
    print(f"\nCollected {len(all_data)} data points.")
