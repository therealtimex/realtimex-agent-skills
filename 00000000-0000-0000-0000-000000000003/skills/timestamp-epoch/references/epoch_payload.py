import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    config_path = Path(__file__).with_name("config.json")
    config = json.loads(config_path.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc)
    payload = {
        "epoch_seconds": int(now.timestamp()),
        "window_seconds": config["window_seconds"],
        "expires_at": int(now.timestamp()) + int(config["window_seconds"]),
    }
    print(json.dumps(payload, separators=(",", ":")))


if __name__ == "__main__":
    main()
