from datetime import datetime, timezone

print(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
