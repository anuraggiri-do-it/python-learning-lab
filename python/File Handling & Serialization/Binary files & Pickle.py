# ============================================================
#  FILE HANDLING — Binary Files & Pickle Serialization
# ============================================================
import pickle
import struct
from pathlib import Path

# ── BINARY FILES ─────────────────────────────────────────────
# Use mode 'rb' / 'wb' / 'ab' for binary I/O.
# No encoding parameter — raw bytes.

# Write raw bytes
with open("data.bin", "wb") as f:
    f.write(b"\x00\xFF\x1A\x2B")       # bytes literal
    f.write(bytes([10, 20, 30, 40]))    # from list of ints

# Read raw bytes
with open("data.bin", "rb") as f:
    raw = f.read()          # bytes object
    print(raw)              # b'\x00\xff\x1a+\n\x14\x1e('
    print(list(raw))        # [0, 255, 26, 43, 10, 20, 30, 40]

# ── struct — pack/unpack fixed-width binary data ─────────────
# Useful for reading binary file formats (images, audio, etc.)
# Format chars: i=int(4B), f=float(4B), d=double(8B), s=char, ?=bool
packed = struct.pack("i f ?", 42, 3.14, True)   # → bytes
print(struct.unpack("i f ?", packed))            # → (42, 3.14, True)

# ── PICKLE — serialize ANY Python object ─────────────────────
# pickle.dump  → write object to file
# pickle.load  → read object from file
# pickle.dumps → serialize to bytes
# pickle.loads → deserialize from bytes

class Student:
    def __init__(self, name, grade):
        self.name  = name
        self.grade = grade
    def __repr__(self):
        return f"Student({self.name}, {self.grade})"

s = Student("Alice", "A")

# Serialize to file
with open("student.pkl", "wb") as f:
    pickle.dump(s, f)

# Deserialize from file
with open("student.pkl", "rb") as f:
    loaded = pickle.load(f)
print(loaded)   # Student(Alice, A)

# Serialize to bytes (useful for caching, network transfer)
blob  = pickle.dumps([1, 2, {"key": "val"}])
obj   = pickle.loads(blob)
print(obj)

# ── PICKLE PROTOCOL VERSIONS ─────────────────────────────────
# protocol=0  → ASCII (oldest, human-readable)
# protocol=2  → Python 2 compatible
# protocol=4  → Python 3.4+ (large objects)
# protocol=5  → Python 3.8+ (out-of-band buffers)
# pickle.HIGHEST_PROTOCOL → always use latest
with open("fast.pkl", "wb") as f:
    pickle.dump(s, f, protocol=pickle.HIGHEST_PROTOCOL)

# ── SECURITY WARNING ─────────────────────────────────────────
# NEVER unpickle data from untrusted sources.
# Pickle can execute arbitrary code during deserialization.
# Use JSON for data exchange; use pickle only for internal caching.

# ── shelve — persistent dict backed by pickle ────────────────
import shelve

with shelve.open("mydb") as db:
    db["user"]   = {"name": "Bob", "age": 25}
    db["scores"] = [90, 85, 92]

with shelve.open("mydb") as db:
    print(db["user"])       # {'name': 'Bob', 'age': 25}
    print(list(db.keys()))  # ['user', 'scores']

# ============================================================
#  PRACTICE QUESTIONS
# ============================================================

# Q1. Write a function to pickle any object to a file and unpickle it.
def save_pickle(filename: str, obj) -> None:
    with open(filename, "wb") as f:
        pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)

def load_pickle(filename: str):
    with open(filename, "rb") as f:
        return pickle.load(f)


# Q2. Serialize a list of Student objects to a pickle file.
def save_students(filename: str, students: list) -> None:
    save_pickle(filename, students)

def load_students(filename: str) -> list:
    return load_pickle(filename)


# Q3. Copy a binary file byte-by-byte using a buffer.
def copy_binary(src: str, dst: str, chunk: int = 4096) -> None:
    with open(src, "rb") as s, open(dst, "wb") as d:
        while buf := s.read(chunk):
            d.write(buf)


# Q4. Use struct to write and read 3 integers to a binary file.
def write_ints(filename: str, nums: list) -> None:
    with open(filename, "wb") as f:
        f.write(struct.pack(f"{len(nums)}i", *nums))

def read_ints(filename: str, count: int) -> tuple:
    with open(filename, "rb") as f:
        return struct.unpack(f"{count}i", f.read(count * 4))


# Q5. Implement a simple file-based cache using shelve.
def cache_result(key: str, value, db_path: str = "cache") -> None:
    with shelve.open(db_path) as db:
        db[key] = value

def get_cached(key: str, db_path: str = "cache"):
    with shelve.open(db_path) as db:
        return db.get(key)


# ── Quick smoke-test ─────────────────────────────────────────
if __name__ == "__main__":
    students = [Student("Alice", "A"), Student("Bob", "B+")]
    save_students("students.pkl", students)
    print(load_students("students.pkl"))

    write_ints("nums.bin", [10, 20, 30])
    print(read_ints("nums.bin", 3))   # (10, 20, 30)

    cache_result("pi", 3.14159)
    print(get_cached("pi"))           # 3.14159

    for f in ["data.bin", "student.pkl", "fast.pkl",
              "students.pkl", "nums.bin"]:
        Path(f).unlink(missing_ok=True)
    for ext in ["", ".db", ".dir", ".bak"]:
        Path("mydb" + ext).unlink(missing_ok=True)
        Path("cache" + ext).unlink(missing_ok=True)
