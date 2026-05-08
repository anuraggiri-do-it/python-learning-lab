# ═══════════════════════════════════════════════════════════════
#         PYTHON SYNTAX, INDENTATION & PEP 8
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS PEP 8?
# ─────────────────────────────────────────────────────────────
# PEP 8 = Python Enhancement Proposal 8
# The official style guide for Python code.
# Written by Guido van Rossum (Python's creator).
#
# ANALOGY: Grammar rules for writing 📝
#   Code runs the same with or without PEP 8.
#   But PEP 8 makes code READABLE — like proper grammar makes
#   writing understandable. Other developers (and future you)
#   will thank you.
#
# RULE OF THUMB: "Code is read more often than it is written."


# ═══════════════════════════════════════════════════════════════
# PART 1: INDENTATION
# ═══════════════════════════════════════════════════════════════
#
# Python uses INDENTATION to define code blocks.
# Unlike C/Java which use {} braces.
#
# RULE: Use 4 SPACES per indentation level (NOT tabs)
# ANALOGY: Outline structure 📋
#   Level 1 = main point
#       Level 2 = sub-point (4 spaces in)
#           Level 3 = sub-sub-point (8 spaces in)

if True:
    print('level 1')        # 4 spaces
    if True:
        print('level 2')    # 8 spaces
        if True:
            print('level 3')# 12 spaces

# IndentationError — most common beginner mistake
# if True:
# print('wrong')    ← IndentationError: expected an indented block

# mixing tabs and spaces → TabError (always use spaces)


# ═══════════════════════════════════════════════════════════════
# PART 2: NAMING CONVENTIONS
# ═══════════════════════════════════════════════════════════════
#
#   Type              Convention      Example
#   ─────────────────────────────────────────────────────────
#   variable          snake_case      user_name, total_price
#   function          snake_case      get_user(), calculate_tax()
#   constant          UPPER_SNAKE     MAX_SIZE, PI, BASE_URL
#   class             PascalCase      UserProfile, HttpRequest
#   module/file       snake_case      data_utils.py, user_model.py
#   package/folder    snake_case      my_package/
#   private var       _single_under   _internal, _cache
#   name mangling     __double_under  __private (class attribute)
#   dunder/magic      __both_sides__  __init__, __str__, __len__

# variables and functions — snake_case
user_name    = 'Alice'
total_price  = 99.99
is_logged_in = True

def calculate_tax(price, rate=0.18):
    return price * rate

def get_full_name(first, last):
    return f'{first} {last}'

# constants — UPPER_SNAKE_CASE
MAX_RETRIES  = 3
PI           = 3.14159
BASE_URL     = 'https://api.example.com'
DEFAULT_PORT = 8080

# classes — PascalCase
class UserProfile:
    pass

class HttpRequestHandler:
    pass

class DatabaseConnection:
    pass

# private convention
class BankAccount:
    def __init__(self, balance):
        self._balance  = balance    # _single: "internal use" hint
        self.__pin     = 1234       # __double: name-mangled (harder to access)

    def _validate(self):            # _single: internal method
        pass


# ═══════════════════════════════════════════════════════════════
# PART 3: LINE LENGTH & LINE BREAKS
# ═══════════════════════════════════════════════════════════════
#
# PEP 8 RULE: max 79 characters per line (72 for docstrings)
# Modern projects often use 88-100 (Black formatter default)
#
# BREAK LONG LINES using:
#   1. Parentheses (preferred)
#   2. Backslash \ (avoid if possible)

# long function call — break with parentheses
result = (
    calculate_tax(total_price)
    + calculate_tax(total_price, rate=0.05)
    + 10
)

# long import
from os.path import (
    join,
    exists,
    dirname,
    basename,
)

# long string
message = (
    'This is a very long message that would exceed '
    'the 79 character line limit if written on one line.'
)

# long condition — wrap in parentheses
user_name = 'Alice'
is_logged_in = True
MAX_RETRIES = 3
retry_count = 1

if (
    user_name is not None
    and is_logged_in
    and retry_count < MAX_RETRIES
):
    print('Proceed')

# backslash (avoid — fragile, breaks if trailing space)
# result = 1 + 2 + \
#          3 + 4


# ═══════════════════════════════════════════════════════════════
# PART 4: BLANK LINES
# ═══════════════════════════════════════════════════════════════
#
# 2 blank lines → before and after top-level functions and classes
# 1 blank line  → between methods inside a class
# 0 blank lines → inside a function (use sparingly for readability)

def function_one():
    pass


def function_two():         # 2 blank lines before
    pass


class MyClass:

    def method_one(self):
        pass

    def method_two(self):   # 1 blank line between methods
        pass


# ═══════════════════════════════════════════════════════════════
# PART 5: SPACES AROUND OPERATORS
# ═══════════════════════════════════════════════════════════════

# ── assignment ───────────────────────────────────────────────
x = 5           # correct
y = x * 2 + 1   # correct
# z=5           ← wrong (no spaces)

# ── comparison ───────────────────────────────────────────────
if x == 5:      # correct
    pass
# if x==5:      ← wrong

# ── default arguments — NO spaces around = ───────────────────
def connect(host, port=8080, timeout=30):   # correct
    pass
# def connect(host, port = 8080):           ← wrong

# ── augmented assignment ─────────────────────────────────────
x += 1          # correct
x -= 1
x *= 2

# ── slice — no spaces ────────────────────────────────────────
lst = [1, 2, 3, 4, 5]
print(lst[1:3])     # correct
# print(lst[1 : 3]) ← wrong


# ═══════════════════════════════════════════════════════════════
# PART 6: IMPORTS
# ═══════════════════════════════════════════════════════════════
#
# RULES:
#   1. One import per line
#   2. At the top of the file
#   3. Order: standard library → third-party → local
#   4. Blank line between each group

# CORRECT ORDER:
import os           # 1. standard library
import sys
import json

# import numpy as np    # 2. third-party (blank line before)
# import pandas as pd

# from mymodule import helper  # 3. local (blank line before)

# WRONG:
# import os, sys        ← multiple on one line
# from os import *      ← wildcard (pollutes namespace)

# absolute imports preferred over relative
import os.path                          # absolute
# from . import utils                   # relative (ok inside packages)


# ═══════════════════════════════════════════════════════════════
# PART 7: COMMENTS
# ═══════════════════════════════════════════════════════════════
#
# RULES:
#   - Comments should explain WHY, not WHAT (code shows what)
#   - Keep comments up to date with code
#   - Start with capital letter, end with period
#   - Inline comments: 2 spaces before #, 1 space after

# GOOD comment — explains WHY
x = x + 1  # Compensate for off-by-one in legacy API

# BAD comment — explains WHAT (obvious from code)
x = x + 1  # Add 1 to x

# block comment — full sentence
# Calculate the discount based on membership tier.
# Gold members get 20%, Silver 10%, Bronze 5%.
discount = 0.20

# inline comment
total = 100 * 1.18  # Include 18% GST


# ═══════════════════════════════════════════════════════════════
# PART 8: COMPARISONS — PYTHONIC STYLE
# ═══════════════════════════════════════════════════════════════

name  = None
items = []
value = 0

# None checks — use 'is' not ==
if name is None:            # correct
    pass
if name is not None:        # correct
# if name == None:          ← wrong (use 'is')
    pass

# empty checks — use truthiness
if not items:               # correct (empty list is falsy)
    pass
if items:                   # correct (non-empty is truthy)
    pass
# if len(items) == 0:       ← verbose, avoid

# boolean checks — don't compare to True/False
flag = True
if flag:                    # correct
    pass
# if flag == True:          ← wrong
# if flag is True:          ← also wrong

# type checks — use isinstance (handles subclasses)
if isinstance(value, int):  # correct
    pass
# if type(value) == int:    ← wrong (misses subclasses)

# chained comparisons
x = 5
if 0 < x < 10:              # Pythonic
    pass
# if x > 0 and x < 10:     ← verbose


# ═══════════════════════════════════════════════════════════════
# PART 9: COMMON PEP 8 VIOLATIONS TO AVOID
# ═══════════════════════════════════════════════════════════════
#
#   ❌  x=5                    ✅  x = 5
#   ❌  def f( x, y ):         ✅  def f(x, y):
#   ❌  import os, sys         ✅  import os \n import sys
#   ❌  from os import *       ✅  from os import path, getcwd
#   ❌  if x == True:          ✅  if x:
#   ❌  if x == None:          ✅  if x is None:
#   ❌  if len(lst) == 0:      ✅  if not lst:
#   ❌  l, O, I as var names   ✅  use descriptive names (l looks like 1)
#   ❌  trailing whitespace    ✅  clean line endings
#   ❌  no blank line at EOF   ✅  always end file with newline


# ═══════════════════════════════════════════════════════════════
# PART 10: TOOLS THAT ENFORCE PEP 8 AUTOMATICALLY
# ═══════════════════════════════════════════════════════════════
#
#   flake8  → linter, reports PEP 8 violations
#             pip install flake8
#             flake8 myfile.py
#
#   black   → auto-formatter, rewrites code to PEP 8
#             pip install black
#             black myfile.py
#
#   isort   → sorts imports automatically
#             pip install isort
#             isort myfile.py
#
#   pylint  → comprehensive linter (style + logic errors)
#             pip install pylint
#             pylint myfile.py
#
#   mypy    → type checker (validates type hints)
#             pip install mypy
#             mypy myfile.py
#
# RECOMMENDED: use black + isort + flake8 together
# Most IDEs (VS Code, PyCharm) run these automatically on save.
