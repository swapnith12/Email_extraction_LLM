import json
import time

def safe_json_loads(text: str) -> dict:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("No JSON found")
    return json.loads(text[start:end + 1])

def retry(fn, retries=3, delay=2):
    for i in range(retries):
        try:
            return fn()
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(delay * (2 ** i))
