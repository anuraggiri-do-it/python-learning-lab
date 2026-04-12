"""
Auto-updates README.md by scanning the repo structure.
Replaces content between <!-- AUTO:section --> ... <!-- END:section --> markers.
"""

import os
import re
from pathlib import Path

ROOT = Path(__file__).parent

# ── Helpers ───────────────────────────────────────────────────────────────────

def count_py_files(folder: Path) -> int:
    return sum(1 for f in folder.rglob("*.py") if not f.name.startswith("."))

def list_py_files(folder: Path) -> list[str]:
    return sorted(
        f.name for f in folder.rglob("*")
        if f.suffix.lower() in (".py", ".PY") and not f.name.startswith(".")
    )

def replace_section(content: str, tag: str, new_body: str) -> str:
    pattern = rf"(<!-- AUTO:{tag} -->).*?(<!-- END:{tag} -->)"
    replacement = rf"\1\n{new_body}\n\2"
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

# ── Section builders ──────────────────────────────────────────────────────────

def build_progress() -> str:
    sections = {
        "Sliding Window":      ROOT / "data_structure/pattern/sliding_window",
        "Slow & Fast Pointer": ROOT / "data_structure/pattern/slow and fast pointer",
        "Kadane's Algorithm":  ROOT / "data_structure/pattern/Kadane pattern",
        "Prefix Sum":          ROOT / "data_structure/pattern/prefix _sum",
        "Two Pointer":         ROOT / "data_structure/pattern/two_pointer",
        "Algorithms":          ROOT / "data_structure/algos",
        "Python Core":         ROOT / "python/Python Core Fundamentals",
        "OOP":                 ROOT / "python/Object-Oriented Programming (OOP)",
        "Built-in DS":         ROOT / "python/Built-in Data Structures",
        "File Handling":       ROOT / "python/File Handling & Serialization",
        "Error Handling":      ROOT / "python/Error Handling & Debugging",
        "Data Analysis":       ROOT / "python/Data Analysis & Manipulation",
        "Numerical Computing": ROOT / "python/Numerical Computing (AI Foundation)",
        "Visualization":       ROOT / "virtualization",
    }

    rows = ["| Module | Files | Status |", "|---|---|---|"]
    for name, path in sections.items():
        if not path.exists():
            rows.append(f"| {name} | — | ⬜ Not Started |")
            continue
        count = count_py_files(path)
        if count == 0:
            status = "⬜ Not Started"
        elif name in ("Two Pointer", "Algorithms"):
            status = "🔄 In Progress"
        else:
            status = f"✅ Complete ({count} files)"
        rows.append(f"| {name} | {count} | {status} |")

    return "\n".join(rows)


def build_dsa_sliding_window() -> str:
    folder = ROOT / "data_structure/pattern/sliding_window"
    files = list_py_files(folder)
    if not files:
        return "_No files yet._"
    rows = ["| # | File |", "|---|---|"]
    for i, f in enumerate(files, 1):
        rows.append(f"| {i} | `{f}` |")
    rows.append(f"\n> **{len(files)} problems** · Pattern: Expand right → shrink left → O(n)")
    return "\n".join(rows)


def build_dsa_slow_fast() -> str:
    folder = ROOT / "data_structure/pattern/slow and fast pointer"
    files = list_py_files(folder)
    if not files:
        return "_No files yet._"
    rows = ["| # | File |", "|---|---|"]
    for i, f in enumerate(files, 1):
        rows.append(f"| {i} | `{f}` |")
    rows.append(f"\n> **{len(files)} problems** · Pattern: Two pointers at different speeds.")
    return "\n".join(rows)


def build_dsa_kadane() -> str:
    folder = ROOT / "data_structure/pattern/Kadane pattern"
    files = list_py_files(folder)
    if not files:
        return "_No files yet._"
    rows = ["| # | File |", "|---|---|"]
    for i, f in enumerate(files, 1):
        rows.append(f"| {i} | `{f}` |")
    rows.append(f"\n> **{len(files)} problems** · Core: `current = max(arr[i], current + arr[i])`")
    return "\n".join(rows)


def build_dsa_prefix() -> str:
    folder = ROOT / "data_structure/pattern/prefix _sum"
    files = list_py_files(folder)
    if not files:
        return "_No files yet._"
    rows = ["| # | File |", "|---|---|"]
    for i, f in enumerate(files, 1):
        rows.append(f"| {i} | `{f}` |")
    rows.append(f"\n> **{len(files)} problems** · Pattern: `prefix[i] = prefix[i-1] + arr[i]`")
    return "\n".join(rows)


def build_python_core() -> str:
    base = ROOT / "python"
    sections = [
        ("Python Core Fundamentals",          "python/Python Core Fundamentals"),
        ("Object-Oriented Programming (OOP)", "python/Object-Oriented Programming (OOP)"),
        ("Built-in Data Structures",          "python/Built-in Data Structures"),
        ("Pythonic Thinking",                 "python/Pythonic Thinking"),
        ("File Handling & Serialization",     "python/File Handling & Serialization"),
        ("Error Handling & Debugging",        "python/Error Handling & Debugging"),
        ("Data Analysis & Manipulation",      "python/Data Analysis & Manipulation"),
        ("Numerical Computing",               "python/Numerical Computing (AI Foundation)"),
        ("Modules & Environments",            "python/Modules, Packages & Environments"),
    ]
    rows = ["| Module | Files |", "|---|---|"]
    for name, rel in sections:
        path = ROOT / rel
        files = list_py_files(path) if path.exists() else []
        file_str = " · ".join(f"`{f}`" for f in files) if files else "_empty_"
        rows.append(f"| **{name}** | {file_str} |")
    return "\n".join(rows)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    readme = ROOT / "README.md"
    content = readme.read_text(encoding="utf-8")

    content = replace_section(content, "progress",         build_progress())
    content = replace_section(content, "sliding-window",   build_dsa_sliding_window())
    content = replace_section(content, "slow-fast",        build_dsa_slow_fast())
    content = replace_section(content, "kadane",           build_dsa_kadane())
    content = replace_section(content, "prefix-sum",       build_dsa_prefix())
    content = replace_section(content, "python-core",      build_python_core())

    readme.write_text(content, encoding="utf-8")
    print("✅ README.md updated successfully.")


if __name__ == "__main__":
    main()
