import json
from datetime import datetime

def log_event(event: str, meta=None):

    print(f"[EVENT] {event}")

    data = {
        "event": event,
        "meta": meta,
        "time": str(datetime.now())
    }

    with open("logs.jsonl", "a") as f:
        f.write(json.dumps(data) + "\n")