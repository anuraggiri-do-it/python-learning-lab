# ═══════════════════════════════════════════════════════════════
#         MODULES, PACKAGES & THE IMPORT SYSTEM
# ═══════════════════════════════════════════════════════════════
#
# ─────────────────────────────────────────────────────────────
# WHAT IS A MODULE?
# ─────────────────────────────────────────────────────────────
# A module = any .py file
# It can contain functions, classes, variables, runnable code.
#
# ANALOGY: Toolbox 🧰
#   Module   = a toolbox (math.py, os.py, random.py)
#   import   = open the toolbox
#   function = pick a specific tool from it
#
# WHAT IS A PACKAGE?
#   Package = a folder of modules with an __init__.py file
#   Lets you organize related modules together
#
# ANALOGY: Workshop cabinet 🗄️
#   Package  = cabinet with labeled drawers
#   Module   = each drawer (contains tools)
#   __init__ = the label on the cabinet door

# ═══════════════════════════════════════════════════════════════
# PART 1: IMPORT STYLES
# ═══════════════════════════════════════════════════════════════

# ── style 1: import entire module ────────────────────────────
import math

print(math.pi)           # 3.14159...
print(math.sqrt(16))     # 4.0             
print(math.factorial(5)) # 120

# ── style 2: import specific names ───────────────────────────
from math import sqrt, pi, floor

print(sqrt(25))          # 5.0  → no math. prefix needed
print(pi)                # 3.14159...
print(floor(3.9))        # 3

# ── style 3: import with alias ───────────────────────────────
import numpy as np                  # industry standard alias
import pandas as pd                 # industry standard alias
import matplotlib.pyplot as plt             # industry standard alias

# alias shortens long names you type repeatedly
# np.array() instead of numpy.array()

# ── style 4: import specific name with alias ─────────────────
from datetime import datetime as dt

now = dt.now()
print(now)               # current date and time

# ── style 5: import all (avoid this) ─────────────────────────
# from math import *     ← BAD PRACTICE
# pollutes namespace → you don't know where names came from
# can silently overwrite your own variables


# ═══════════════════════════════════════════════════════════════
# PART 2: HOW  PYTHON FINDS MODULES (sys.path)
# ═══════════════════════════════════════════════════════════════
#
# When you write `import something`, Python searches in order:
#   1. sys.modules cache  → already imported? use cached version
#   2. Built-in modules   → math, os, sys (compiled into Python)
#   3. sys.path list      → directories Python searches
#      a. current directory (script's folder)
#      b. PYTHONPATH env variable
#      c. standard library
#      d. site-packages (pip installed packages)
#
# ANALOGY: Finding a book in a library 📚
#   1. Check your desk (cache)
#   2. Check built-in shelf (standard library)
#   3. Walk through each aisle in order (sys.path)

import sys

print(sys.path)          # list of directories Python searches
print(sys.modules.keys()) # all currently cached modules

# add custom path at runtime
# sys.path.append('/path/to/my/modules')


# ═══════════════════════════════════════════════════════════════
# PART 3: STANDARD LIBRARY — MOST USEFUL MODULES
# ═══════════════════════════════════════════════════════════════

# ── os — operating system interface ──────────────────────────
import os

print(os.getcwd())                    # current working directory
print(os.listdir('.'))                # list files in current dir
print(os.path.exists('test.txt'))     # check if file exists
print(os.path.join('folder', 'file.txt'))  # safe path joining
print(os.path.basename('/a/b/c.py')) # 'c.py'
print(os.path.dirname('/a/b/c.py'))  # '/a/b'
print(os.path.splitext('file.py'))   # ('file', '.py')

# os.makedirs('new_folder', exist_ok=True)  # create directory
# os.rename('old.txt', 'new.txt')           # rename file
# os.remove('file.txt')                     # delete file

# ── sys — interpreter info ────────────────────────────────────
import sys

print(sys.version)       # Python version string
print(sys.platform)      # 'win32', 'linux', 'darwin'
print(sys.argv)          # command line arguments list
                         # sys.argv[0] = script name
                         # sys.argv[1] = first argument

# sys.exit(0)            # exit program (0 = success, 1 = error)

# ── datetime — dates and times ───────────────────────────────
from datetime import datetime, date, timedelta

today     = date.today()
now       = datetime.now()
birthday  = date(2000, 6, 15)

print(today)                          # 2024-01-15
print(now.strftime("%d/%m/%Y %H:%M")) # formatted string
print(datetime.strptime("15/01/2024", "%d/%m/%Y"))  # parse string → datetime

delta = timedelta(days=30)
print(today + delta)                  # 30 days from today
print((today - birthday).days)        # days since birthday

# ── random — random numbers ───────────────────────────────────
import random

random.seed(42)                       # reproducible results
print(random.randint(1, 10))          # random int [1, 10]
print(random.random())                # float [0.0, 1.0)
print(random.choice(['a', 'b', 'c'])) # random element
print(random.sample(range(10), 3))    # 3 unique random elements
items = [1, 2, 3, 4, 5]
random.shuffle(items)                 # shuffle in place
print(items)

# ── collections — specialized containers ─────────────────────
from collections import Counter, defaultdict, OrderedDict, deque, namedtuple

# Counter → count occurrences
words   = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = Counter(words)
print(counter)                        # Counter({'apple': 3, 'banana': 2, ...})
print(counter.most_common(2))         # [('apple', 3), ('banana', 2)]

# defaultdict → dict with default value for missing keys
dd = defaultdict(list)
dd['fruits'].append('apple')          # no KeyError even though 'fruits' didn't exist
dd['fruits'].append('banana')
print(dd)

# deque → double-ended queue (fast append/pop from both ends)
dq = deque([1, 2, 3])
dq.appendleft(0)                      # O(1) add to front
dq.append(4)                          # O(1) add to back
dq.popleft()                          # O(1) remove from front
print(dq)                             # deque([1, 2, 3, 4])

# namedtuple → tuple with named fields (lightweight class)
Point = namedtuple('Point', ['x', 'y'])
p     = Point(3, 4)
print(p.x, p.y)                       # 3 4
print(p[0], p[1])                     # 3 4  ← still works as tuple

# ── itertools — iterator tools ────────────────────────────────
import itertools

# combinations → all unique pairs
print(list(itertools.combinations([1, 2, 3], 2)))  # [(1,2),(1,3),(2,3)]

# permutations → all ordered arrangements
print(list(itertools.permutations([1, 2, 3], 2)))  # [(1,2),(1,3),(2,1)...]

# product → cartesian product (nested loops)
print(list(itertools.product([0, 1], repeat=2)))   # [(0,0),(0,1),(1,0),(1,1)]

# chain → flatten iterables
print(list(itertools.chain([1, 2], [3, 4], [5])))  # [1,2,3,4,5]

# groupby → group consecutive elements
data = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))

# ── functools — higher-order functions ────────────────────────
from functools import reduce, lru_cache, partial

# reduce → apply function cumulatively
total = reduce(lambda acc, x: acc + x, [1, 2, 3, 4, 5])
print(total)                          # 15

# lru_cache → memoize expensive function calls
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(50))                        # instant, cached results

# partial → fix some arguments of a function
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube   = partial(power, exp=3)
print(square(5))                      # 25
print(cube(3))                        # 27

# ── pathlib — modern file paths ───────────────────────────────
from pathlib import Path

p = Path('.')                         # current directory
print(p.resolve())                    # absolute path
print(list(p.glob('*.py')))           # all .py files in current dir
print(list(p.rglob('*.py')))          # all .py files recursively

new_path = Path('folder') / 'sub' / 'file.txt'  # safe path joining
print(new_path)                       # folder\sub\file.txt

# p.mkdir(parents=True, exist_ok=True)  # create directory tree
# p.write_text('hello')                 # write file
# p.read_text()                         # read file

# ── json — JSON handling ──────────────────────────────────────
import json

data = {'name': 'Alice', 'age': 30, 'skills': ['Python', 'ML']}

json_str = json.dumps(data, indent=2)  # dict → JSON string
print(json_str)

parsed   = json.loads(json_str)        # JSON string → dict
print(parsed['name'])                  # Alice

# json.dump(data, file)                # write to file
# json.load(file)                      # read from file

# ── re — regular expressions ─────────────────────────────────
import re

text = "My email is user@example.com and phone is 123-456-7890"

email = re.search(r'[\w.]+@[\w.]+', text)
print(email.group())                  # user@example.com

phones = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print(phones)                         # ['123-456-7890']

cleaned = re.sub(r'\d', '*', "abc123")
print(cleaned)                        # abc***


# ═══════════════════════════════════════════════════════════════
# PART 4: __name__ == "__main__"
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS IT?
#   Every module has a __name__ variable.
#   When run directly  → __name__ == "__main__"
#   When imported      → __name__ == module's filename
#
# ANALOGY: Employee badge 🪪
#   When you're the boss (run directly) → badge says "MAIN"
#   When you're a helper (imported)     → badge says your name
#
# WHY USE IT?
#   Lets you write code that runs ONLY when the file is executed
#   directly, NOT when it's imported by another file.
#   Prevents test/demo code from running on import.

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

if __name__ == "__main__":
    # this block runs ONLY when you run this file directly
    # it does NOT run when another file imports this module
    print(greet("World"))
    print(add(2, 3))


# ═══════════════════════════════════════════════════════════════
# PART 5: VIRTUAL ENVIRONMENTS
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS A VIRTUAL ENVIRONMENT?
#   An isolated Python environment with its own packages.
#   Each project gets its own packages, no conflicts.
#
# ANALOGY: Separate apartments 🏠
#   Global Python = shared house (everyone's packages mixed)
#   Virtual env   = your own apartment (your packages only)
#   Project A needs numpy 1.0, Project B needs numpy 2.0 → no conflict
#
# COMMANDS:
# ─────────────────────────────────────────────────────────────
#
#   CREATE:
#   python -m venv .venv
#
#   ACTIVATE:
#   Windows:  .venv\Scripts\activate
#   Mac/Linux: source .venv/bin/activate
#
#   DEACTIVATE:
#   deactivate
#
#   INSTALL PACKAGES:
#   pip install numpy pandas matplotlib
#
#   SAVE DEPENDENCIES:
#   pip freeze > requirements.txt
#
#   INSTALL FROM requirements.txt:
#   pip install -r requirements.txt
#
#   LIST INSTALLED:
#   pip list
#
#   SHOW PACKAGE INFO:
#   pip show numpy
#
# ─────────────────────────────────────────────────────────────
# WHAT IS requirements.txt?
#   A file listing all packages + versions your project needs.
#   Anyone can recreate your exact environment with:
#   pip install -r requirements.txt
#
# ANALOGY: Recipe card 🍳
#   requirements.txt = ingredient list with exact amounts
#   pip install -r = go buy exactly those ingredients


# ═══════════════════════════════════════════════════════════════
# PART 6: CREATING YOUR OWN MODULE & PACKAGE
# ═══════════════════════════════════════════════════════════════
#
# MODULE: just save any .py file and import it
#
#   mymath.py:
#   ───────────────────────
#   def add(a, b):
#       return a + b
#
#   def multiply(a, b):
#       return a * b
#   ───────────────────────
#
#   main.py:
#   ───────────────────────
#   import mymath
#   print(mymath.add(2, 3))       # 5
#   print(mymath.multiply(2, 3))  # 6
#   ───────────────────────
#
# PACKAGE: folder with __init__.py
#
#   mypackage/
#   ├── __init__.py       ← makes it a package (can be empty)
#   ├── math_utils.py
#   └── string_utils.py
#
#   main.py:
#   ───────────────────────
#   from mypackage import math_utils
#   from mypackage.string_utils import reverse
#   ───────────────────────
#
# __init__.py controls what gets exported when you do:
#   from mypackage import *
#
#   __init__.py:
#   ───────────────────────
#   from .math_utils import add, multiply
#   __all__ = ['add', 'multiply']
#   ───────────────────────


# ═══════════════════════════════════════════════════════════════
# PART 7: IMPORT SYSTEM INTERNALS
# ═══════════════════════════════════════════════════════════════
#
# WHAT HAPPENS when you write `import math`?
#
#   Step 1: Check sys.modules cache
#           Already imported? → return cached object immediately
#
#   Step 2: Find the module
#           Search sys.path directories in order
#
#   Step 3: Load & compile
#           Read .py file → compile to bytecode (.pyc in __pycache__)
#           .pyc = faster reload next time (skip compilation)
#
#   Step 4: Execute
#           Run the module's top-level code
#           Build the module object
#
#   Step 5: Cache
#           Store in sys.modules for future imports
#
# ANALOGY: First time vs repeat visit to a restaurant 🍽️
#   First import  = cook the meal from scratch (compile + execute)
#   Next import   = serve from cache (sys.modules) → instant
#
# __pycache__ folder:
#   Python stores compiled .pyc files here
#   Speeds up subsequent imports
#   Safe to delete (Python recreates it)

import importlib

# force reload a module (useful during development)
import math as math_module
importlib.reload(math_module)

# check where a module is located
print(math.__file__)              # path to math module
print(os.__file__)                # path to os module


# ═══════════════════════════════════════════════════════════════
# PART 8: RELATIVE vs ABSOLUTE IMPORTS
# ═══════════════════════════════════════════════════════════════
#
# ABSOLUTE import → full path from project root (preferred)
#   from mypackage.utils import helper
#
# RELATIVE import → relative to current file (use inside packages)
#   from . import utils          ← same package
#   from .. import config        ← parent package
#   from .utils import helper    ← specific from same package
#
# ANALOGY: Giving directions 🗺️
#   Absolute = "Go to 123 Main Street, New York"
#   Relative = "Turn left, then second right from here"
#
# RULE: use absolute imports in scripts, relative inside packages


# ═══════════════════════════════════════════════════════════════
# QUICK REFERENCE
# ═══════════════════════════════════════════════════════════════
#
#   import module                → access via module.name
#   from module import name      → access directly as name
#   from module import name as x → access as x
#   import module as m           → access via m.name
#
#   __name__ == "__main__"       → only runs when executed directly
#   sys.path                     → where Python looks for modules
#   sys.modules                  → cache of imported modules
#   pip freeze > requirements.txt → save dependencies
#   pip install -r requirements.txt → restore dependencies
