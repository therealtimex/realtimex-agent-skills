import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    config_path = Path(__file__).with_name("config.json")
    config = json.loads(config_path.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc)
    payload = {
        "utc_iso": now.isoformat().replace("+00:00", "Z"),
        "weekday": now.strftime("%A"),
        "precision": config["precision"],
        "timezone": config["timezone"],
    }
    print(json.dumps(payload, separators=(",", ":")))


if __name__ == "__main__":
    main()
