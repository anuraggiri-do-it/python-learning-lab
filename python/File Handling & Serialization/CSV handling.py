# ============================================================
#  FILE HANDLING — CSV (Comma-Separated Values)
# ============================================================
import csv
from pathlib import Path

# ── WHY csv MODULE? ──────────────────────────────────────────
# Handles quoting, commas inside fields, newlines inside fields
# automatically — don't parse CSV manually with split(',').

# ── WRITING CSV ──────────────────────────────────────────────
rows = [
    ["Name",  "Age", "City"],
    ["Alice",  30,   "Delhi"],
    ["Bob",    25,   "Mumbai"],
    ["Carol",  28,   "Pune"],
]

with open("people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)          # write all at once
    # writer.writerow(row)          # write one row

# ── READING CSV ──────────────────────────────────────────────
with open("people.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)           # skip / capture header
    for row in reader:
        print(row)                  # each row is a list of strings

# ── DictReader / DictWriter (recommended) ────────────────────
# DictReader → each row is an OrderedDict keyed by header names
with open("people.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["Name"], row["Age"])

# DictWriter → write dicts as rows
fields = ["Name", "Age", "City"]
data   = [{"Name": "Dave", "Age": 22, "City": "Kolkata"}]

with open("new.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(data)

# ── CUSTOM DELIMITER ─────────────────────────────────────────
# TSV (tab-separated)
with open("data.tsv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t").writerows(rows)

# ── DIALECT ──────────────────────────────────────────────────
# csv.excel (default), csv.unix, or register custom
csv.register_dialect("pipes", delimiter="|", quoting=csv.QUOTE_MINIMAL)

# ── IMPORTANT GOTCHAS ────────────────────────────────────────
# 1. Always open with newline="" on Windows to avoid blank rows.
# 2. All values read back are STRINGS — cast manually (int, float).
# 3. Use encoding="utf-8-sig" when opening Excel-generated CSVs
#    to strip the BOM character.

# ============================================================
#  PRACTICE QUESTIONS
# ============================================================

# Q1. Read people.csv and return a list of dicts.
def csv_to_list(filename: str) -> list:
    with open(filename, encoding="utf-8") as f:
        return list(csv.DictReader(f))


# Q2. Given a list of dicts, write them to a CSV file.
def list_to_csv(filename: str, data: list) -> None:
    if not data:
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=data[0].keys())
        w.writeheader()
        w.writerows(data)


# Q3. Filter rows where Age > threshold and save to new CSV.
def filter_csv(src: str, dst: str, age_threshold: int) -> None:
    with open(src, encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if int(r["Age"]) > age_threshold]
    list_to_csv(dst, rows)


# Q4. Count how many rows exist in a CSV (excluding header).
def count_rows(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        return sum(1 for _ in csv.reader(f)) - 1  # -1 for header


# Q5. Append a new row dict to an existing CSV.
def append_row(filename: str, row: dict) -> None:
    with open(filename, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=row.keys())
        w.writerow(row)


# ── Quick smoke-test ─────────────────────────────────────────
if __name__ == "__main__":
    data = csv_to_list("people.csv")
    print(data)
    filter_csv("people.csv", "filtered.csv", 26)
    print(count_rows("filtered.csv"))
    append_row("filtered.csv", {"Name": "Eve", "Age": 35, "City": "Chennai"})

    for f in ["people.csv", "new.csv", "data.tsv", "filtered.csv"]:
        Path(f).unlink(missing_ok=True)
