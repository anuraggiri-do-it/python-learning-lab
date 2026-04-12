# ============================================================
#  SERIALIZATION — JSON (JavaScript Object Notation)
# ============================================================
import json
from pathlib import Path

# ── PYTHON ↔ JSON TYPE MAPPING ───────────────────────────────
# Python          JSON
# dict      →     object  {}
# list/tuple→     array   []
# str       →     string  ""
# int/float →     number
# True/False→     true/false
# None      →     null

# ── SERIALIZATION (Python → JSON string) ─────────────────────
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92], "active": True}

json_str = json.dumps(data)                         # compact string
json_pretty = json.dumps(data, indent=4)            # human-readable
json_sorted = json.dumps(data, indent=4, sort_keys=True)

print(json_str)
print(json_pretty)

# ── DESERIALIZATION (JSON string → Python) ───────────────────
parsed = json.loads(json_str)
print(parsed["name"])   # Alice
print(type(parsed))     # <class 'dict'>

# ── FILE I/O ─────────────────────────────────────────────────
# Write to file
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

# Read from file
with open("data.json", encoding="utf-8") as f:
    loaded = json.load(f)

# ── CUSTOM SERIALIZATION ─────────────────────────────────────
from datetime import datetime, date

# Problem: datetime is not JSON-serializable by default
# Solution 1: custom default function
def json_default(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

event = {"title": "Meeting", "date": date(2025, 7, 1)}
print(json.dumps(event, default=json_default))

# Solution 2: JSONEncoder subclass
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)

print(json.dumps(event, cls=CustomEncoder))

# ── COMMON PITFALLS ──────────────────────────────────────────
# 1. json.dumps vs json.dump  — dumps → string, dump → file
# 2. json.loads vs json.load  — loads → from string, load → from file
# 3. Tuple becomes list after round-trip (JSON has no tuple type)
# 4. Dict keys are always strings in JSON
# 5. Sets are NOT serializable — convert to list first

# ── NESTED / COMPLEX JSON ────────────────────────────────────
nested = {
    "users": [
        {"id": 1, "tags": ["admin", "user"]},
        {"id": 2, "tags": ["user"]},
    ]
}
print(nested["users"][0]["tags"][0])  # admin

# ============================================================
#  PRACTICE QUESTIONS
# ============================================================

# Q1. Save any Python dict to a JSON file and load it back.
def save_json(filename: str, obj: dict) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)

def load_json(filename: str) -> dict:
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


# Q2. Merge two JSON files into one (dicts).
def merge_json(file1: str, file2: str, output: str) -> None:
    d1, d2 = load_json(file1), load_json(file2)
    save_json(output, {**d1, **d2})


# Q3. Pretty-print a JSON string with sorted keys.
def pretty(json_str: str) -> str:
    return json.dumps(json.loads(json_str), indent=4, sort_keys=True)


# Q4. Extract all values for a given key from a list of JSON objects.
def extract_field(records: list, key: str) -> list:
    return [r[key] for r in records if key in r]


# Q5. Serialize a list of objects that contain date fields.
def serialize_with_dates(records: list) -> str:
    return json.dumps(records, default=json_default, indent=2)


# ── Quick smoke-test ─────────────────────────────────────────
if __name__ == "__main__":
    save_json("a.json", {"x": 1, "y": 2})
    save_json("b.json", {"y": 99, "z": 3})
    merge_json("a.json", "b.json", "merged.json")
    print(load_json("merged.json"))

    records = [{"name": "Alice", "joined": date(2024, 1, 15)},
               {"name": "Bob",   "joined": date(2023, 6, 1)}]
    print(serialize_with_dates(records))

    for f in ["data.json", "a.json", "b.json", "merged.json"]:
        Path(f).unlink(missing_ok=True)
