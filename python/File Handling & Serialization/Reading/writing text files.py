# ============================================================
#  FILE HANDLING — Reading & Writing Text Files
# ============================================================

# ── OPEN MODES ───────────────────────────────────────────────
# 'r'   → read (default); error if file doesn't exist
# 'w'   → write; creates file or TRUNCATES existing
# 'a'   → append; creates file if missing
# 'x'   → exclusive create; error if file exists
# 'r+'  → read + write (no truncation)
# 'b'   → binary mode suffix  e.g. 'rb', 'wb'
# 't'   → text mode suffix (default)

# ── ALWAYS USE `with` (context manager) ──────────────────────
# Automatically closes the file even if an exception occurs.

# ── WRITING ──────────────────────────────────────────────────
with open("demo.txt", "w") as f:
    f.write("Hello, World!\n")          # write() — no auto newline
    f.writelines(["Line 2\n", "Line 3\n"])  # writelines() — list of strings

# ── READING ──────────────────────────────────────────────────
with open("demo.txt", "r") as f:
    content = f.read()          # entire file as one string
    # f.readline()              # one line at a time
    # f.readlines()             # list of all lines (with \n)

# Iterate line-by-line (memory efficient for large files)
with open("demo.txt") as f:
    for line in f:
        print(line.strip())     # strip() removes trailing \n

# ── APPENDING ────────────────────────────────────────────────
with open("demo.txt", "a") as f:
    f.write("Appended line\n")

# ── FILE POINTER ─────────────────────────────────────────────
with open("demo.txt", "r+") as f:
    f.seek(0)           # move pointer to byte position 0
    print(f.tell())     # current pointer position → 0
    f.write("Hi!")      # overwrites first 3 bytes

# ── ENCODING ─────────────────────────────────────────────────
# Always specify encoding for portability
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("नमस्ते\n")   # works with utf-8

# ── os / pathlib helpers ─────────────────────────────────────
import os
print(os.path.exists("demo.txt"))   # True / False
print(os.path.getsize("demo.txt"))  # size in bytes
os.remove("demo.txt")               # delete file

from pathlib import Path
p = Path("notes.txt")
p.write_text("Hello via pathlib\n", encoding="utf-8")
print(p.read_text(encoding="utf-8"))
p.unlink()  # delete

# ============================================================
#  PRACTICE QUESTIONS
# ============================================================

# Q1. Write a function that writes a list of strings to a file
#     (one per line) and returns the number of lines written.
def write_lines(filename: str, lines: list) -> int:
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(line + "\n" for line in lines)
    return len(lines)


# Q2. Write a function that reads a file and returns a dict
#     {line_number: line_content} (1-indexed, stripped).
def read_as_dict(filename: str) -> dict:
    with open(filename, encoding="utf-8") as f:
        return {i + 1: line.strip() for i, line in enumerate(f)}


# Q3. Write a function that counts word frequency in a text file.
from collections import Counter
def word_frequency(filename: str) -> dict:
    with open(filename, encoding="utf-8") as f:
        words = f.read().lower().split()
    return dict(Counter(words))


# Q4. Write a function that merges multiple files into one.
def merge_files(output: str, *inputs: str) -> None:
    with open(output, "w", encoding="utf-8") as out:
        for path in inputs:
            with open(path, encoding="utf-8") as inp:
                out.write(inp.read())


# Q5. Write a function that replaces every occurrence of a word
#     in a file (in-place).
def replace_in_file(filename: str, old: str, new: str) -> None:
    p = Path(filename)
    p.write_text(p.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")


# ── Quick smoke-test ─────────────────────────────────────────
if __name__ == "__main__":
    write_lines("test.txt", ["apple", "banana", "cherry"])
    print(read_as_dict("test.txt"))
    print(word_frequency("test.txt"))
    replace_in_file("test.txt", "banana", "mango")
    print(Path("test.txt").read_text())
    Path("test.txt").unlink()
