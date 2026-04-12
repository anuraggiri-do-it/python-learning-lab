# ============================================================
#  FILE HANDLING & SERIALIZATION — Practice Questions
#  Topics: Text Files, CSV, JSON, Binary, Pickle
# ============================================================
import csv, json, pickle
from pathlib import Path
from collections import Counter

# ── EASY ─────────────────────────────────────────────────────

# E1. Write a list of numbers to a file (one per line),
#     then read it back as a list of ints.
def numbers_roundtrip(nums: list, filename="nums.txt") -> list:
    Path(filename).write_text("\n".join(map(str, nums)))
    return list(map(int, Path(filename).read_text().splitlines()))

# E2. Count the number of lines in a text file.
def count_lines(filename: str) -> int:
    with open(filename) as f:
        return sum(1 for _ in f)

# E3. Read a JSON file and return the value for a given key.
def get_json_key(filename: str, key: str):
    with open(filename) as f:
        return json.load(f).get(key)

# E4. Write a list of dicts to CSV and read it back.
def csv_roundtrip(data: list, filename="tmp.csv") -> list:
    if not data: return []
    with open(filename, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=data[0].keys())
        w.writeheader(); w.writerows(data)
    with open(filename) as f:
        return list(csv.DictReader(f))

# E5. Pickle a dict and unpickle it.
def pickle_roundtrip(obj, filename="tmp.pkl"):
    with open(filename, "wb") as f: pickle.dump(obj, f)
    with open(filename, "rb") as f: return pickle.load(f)


# ── MEDIUM ───────────────────────────────────────────────────

# M1. Log writer: append timestamped messages to a log file.
from datetime import datetime
def log(message: str, filename="app.log") -> None:
    with open(filename, "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {message}\n")

# M2. CSV → JSON converter.
def csv_to_json(csv_file: str, json_file: str) -> None:
    with open(csv_file) as f:
        data = list(csv.DictReader(f))
    with open(json_file, "w") as f:
        json.dump(data, f, indent=2)

# M3. JSON → CSV converter.
def json_to_csv(json_file: str, csv_file: str) -> None:
    with open(json_file) as f:
        data = json.load(f)
    if not data: return
    with open(csv_file, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=data[0].keys())
        w.writeheader(); w.writerows(data)

# M4. Find the most common word in a text file.
def most_common_word(filename: str) -> str:
    with open(filename) as f:
        words = f.read().lower().split()
    return Counter(words).most_common(1)[0][0]

# M5. Split a large CSV into chunks of N rows each.
def split_csv(filename: str, chunk_size: int) -> None:
    with open(filename) as f:
        reader = csv.DictReader(f)
        chunk, idx = [], 0
        for row in reader:
            chunk.append(row)
            if len(chunk) == chunk_size:
                _write_chunk(chunk, reader.fieldnames, idx)
                chunk, idx = [], idx + 1
        if chunk:
            _write_chunk(chunk, reader.fieldnames, idx)

def _write_chunk(rows, fields, idx):
    with open(f"chunk_{idx}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)

# M6. Update a specific key in a JSON file.
def update_json(filename: str, key: str, value) -> None:
    with open(filename) as f:
        data = json.load(f)
    data[key] = value
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


# ── HARD ─────────────────────────────────────────────────────

# H1. Implement a simple key-value store backed by a JSON file.
class JsonStore:
    def __init__(self, path="store.json"):
        self.path = Path(path)
        if not self.path.exists():
            self.path.write_text("{}")

    def _load(self): return json.loads(self.path.read_text())
    def _save(self, d): self.path.write_text(json.dumps(d, indent=2))

    def set(self, key, value): d = self._load(); d[key] = value; self._save(d)
    def get(self, key, default=None): return self._load().get(key, default)
    def delete(self, key): d = self._load(); d.pop(key, None); self._save(d)
    def all(self): return self._load()


# H2. CSV aggregator — compute sum/avg of a numeric column.
def aggregate_csv(filename: str, column: str) -> dict:
    with open(filename) as f:
        values = [float(r[column]) for r in csv.DictReader(f)]
    return {"count": len(values), "sum": sum(values),
            "avg": sum(values) / len(values) if values else 0}


# H3. Serialize a class with __getstate__ / __setstate__ for pickle.
class Config:
    def __init__(self, settings: dict):
        self.settings = settings
        self._cache   = {}          # transient — don't pickle

    def __getstate__(self):
        return {"settings": self.settings}   # exclude _cache

    def __setstate__(self, state):
        self.settings = state["settings"]
        self._cache   = {}                   # reinitialize


# H4. Watch a file for new lines (tail -f style).
import time
def tail(filename: str, interval: float = 0.5, max_reads: int = 5):
    """Yields new lines appended to a file."""
    with open(filename) as f:
        f.seek(0, 2)    # seek to end
        for _ in range(max_reads):
            line = f.readline()
            if line:
                yield line.strip()
            else:
                time.sleep(interval)


# H5. Binary file diff — return byte positions where two files differ.
def binary_diff(file1: str, file2: str) -> list:
    diffs = []
    with open(file1, "rb") as f1, open(file2, "rb") as f2:
        pos = 0
        while True:
            b1, b2 = f1.read(1), f2.read(1)
            if not b1 and not b2: break
            if b1 != b2:
                diffs.append(pos)
            pos += 1
    return diffs


# ── Quick smoke-test ─────────────────────────────────────────
if __name__ == "__main__":
    # E1
    print(numbers_roundtrip([1, 2, 3, 4, 5]))

    # E5
    print(pickle_roundtrip({"a": 1, "b": [2, 3]}))

    # H1
    store = JsonStore("test_store.json")
    store.set("lang", "Python")
    store.set("version", 3.12)
    print(store.all())
    store.delete("version")
    print(store.get("lang"))

    # H3
    cfg = Config({"debug": True, "port": 8080})
    blob = pickle.dumps(cfg)
    cfg2 = pickle.loads(blob)
    print(cfg2.settings, cfg2._cache)

    # Cleanup
    for f in ["nums.txt", "tmp.csv", "tmp.pkl", "app.log",
              "store.json", "test_store.json"]:
        Path(f).unlink(missing_ok=True)
