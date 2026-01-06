from datetime import datetime, timezone

print(int(datetime.now(timezone.utc).timestamp()))
