# ─── Python Syntax & Indentation ─────────────────────────────────────────────

# Indentation: 4 spaces (PEP8 standard)
if True:
    print("indented block")   # correct
    if True:
        print("nested block") # nested indentation

# ─── PEP8 Naming Conventions ─────────────────────────────────────────────────
my_variable = 10             # snake_case  → variables, functions
MY_CONSTANT = 3.14           # UPPER_CASE  → constants
class MyClass:               # PascalCase  → classes
    pass

# ─── Line Length (max 79 chars) ──────────────────────────────────────────────
result = (1 + 2 +
          3 + 4)             # break long lines with parentheses

# ─── Blank Lines ─────────────────────────────────────────────────────────────
# 2 blank lines before/after top-level functions and classes
# 1 blank line between methods inside a class

def greet():
    pass


def farewell():
    pass


# ─── Spaces Around Operators ─────────────────────────────────────────────────
x = 5 + 3       # correct
y = x*2 + 1     # avoid — add spaces around operators

# ─── Imports (one per line, at top) ──────────────────────────────────────────
import os
import sys
# not: import os, sys

# ─── Semicolons & Multiple Statements ────────────────────────────────────────
# Avoid: x = 1; y = 2
x = 1
y = 2

# ─── Comparison ──────────────────────────────────────────────────────────────
name = None
if name is None:             # use 'is' for None
    print("no name")

items = []
if not items:                # use 'not' for empty check
    print("empty list")
