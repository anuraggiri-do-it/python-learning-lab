# ═══════════════════════════════════════════════════════════════
#         VARIABLES & SIMPLE DATA TYPES
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS A VARIABLE?
# ─────────────────────────────────────────────────────────────
# A variable = a name that points to a value in memory.
# Python variables are LABELS, not boxes.
#
# ANALOGY: Sticky note on an object 🏷️
#   The sticky note (variable name) points to the object (value).
#   Multiple notes can point to the same object.
#   Reassigning = moving the sticky note to a different object.
#
# Python is DYNAMICALLY TYPED:
#   No need to declare type — Python figures it out at runtime.
#   The variable itself has no type — the OBJECT has a type.


# ═══════════════════════════════════════════════════════════════
# PART 1: VARIABLES & ASSIGNMENT
# ═══════════════════════════════════════════════════════════════

x    = 10
name = 'Alice'
pi   = 3.14159
flag = True

# multiple assignment
a, b, c = 1, 2, 3           # unpack tuple
x = y = z = 0               # same value to multiple names

# swap without temp variable (Python-specific)
a, b = 10, 20
a, b = b, a
print(a, b)                 # 20 10

# augmented assignment
x  = 5
x += 3                      # x = x + 3  → 8
x -= 2                      # x = x - 2  → 6
x *= 4                      # x = x * 4  → 24
x //= 5                     # x = x // 5 → 4
x **= 2                     # x = x ** 2 → 16
x %= 5                      # x = x % 5  → 1

# walrus operator := (Python 3.8+) — assign AND use in one expression
import re
text = 'Hello World 123'
if m := re.search(r'\d+', text):
    print(f'Found number: {m.group()}')     # 123

# also useful in while loops
data = [1, 2, 3, 4, 5]
while chunk := data[:2]:
    print(chunk)
    data = data[2:]


# ═══════════════════════════════════════════════════════════════
# PART 2: int
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: Whole numbers on a number line ←—0—→
# Python ints have UNLIMITED precision (no overflow like C/Java)

age     = 25
negative = -10
big     = 1_000_000_000     # underscores for readability
binary  = 0b1010            # binary literal  → 10
octal   = 0o17              # octal literal   → 15
hexa    = 0xFF              # hex literal     → 255

print(type(age))            # <class 'int'>
print(abs(negative))        # 10
print(bin(age))             # 0b11001
print(oct(age))             # 0o31
print(hex(age))             # 0x19
print(age ** 2)             # 625
print(age // 7)             # 3   (floor division)
print(age % 7)              # 4   (remainder)
print(divmod(age, 7))       # (3, 4)  — quotient and remainder together

# int has unlimited precision
print(2 ** 100)             # 1267650600228229401496703205376

# int methods
print(int('42'))            # 42   — from string
print(int('1010', 2))       # 10   — binary string to int
print(int('FF', 16))        # 255  — hex string to int
print(int(3.9))             # 3    — truncates (not rounds)


# ═══════════════════════════════════════════════════════════════
# PART 3: float
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: Numbers with a decimal point 📏
# Stored as IEEE 754 double precision (64-bit)
# WARNING: floating point is NOT exact

price      = 9.99
scientific = 1.5e3          # 1500.0
tiny       = 2.5e-4         # 0.00025

print(type(price))          # <class 'float'>
print(round(price, 1))      # 10.0
print(int(price))           # 9    (truncates)
print(float(42))            # 42.0

# floating point precision issue
print(0.1 + 0.2)            # 0.30000000000000004  ← NOT 0.3!
print(0.1 + 0.2 == 0.3)     # False  ← never compare floats with ==

import math
print(math.isclose(0.1 + 0.2, 0.3))    # True  ← correct way
print(round(0.1 + 0.2, 10) == 0.3)     # True

# special float values
print(float('inf'))         # infinity
print(float('-inf'))        # negative infinity
print(float('nan'))         # Not a Number
print(math.isinf(float('inf')))  # True
print(math.isnan(float('nan')))  # True

# useful math functions
print(math.floor(3.9))      # 3   — round down
print(math.ceil(3.1))       # 4   — round up
print(math.trunc(3.9))      # 3   — truncate toward zero
print(round(3.5))           # 4   — banker's rounding (round half to even)
print(round(2.5))           # 2   ← banker's rounding!

# decimal module for exact decimal arithmetic
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # 0.3  ← exact!


# ═══════════════════════════════════════════════════════════════
# PART 4: str
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: A sequence of characters in a box 📦
# Strings are IMMUTABLE — you can't change them, only create new ones

# creation
single   = 'Hello'
double   = "World"
multi    = """This is
a multiline string"""
raw      = r'C:\Users\name'     # raw string — backslash not escape
byte_str = b'bytes'             # bytes literal

# f-strings (Python 3.6+) — most powerful
name  = 'Alice'
score = 95.678
print(f'Name: {name}')                  # Name: Alice
print(f'Score: {score:.2f}')            # Score: 95.68
print(f'Score: {score:>10.2f}')         # right-align in 10 chars
print(f'{name!r}')                      # 'Alice'  ← repr format
print(f'{name!u}' if False else f'{name.upper()}')  # ALICE
print(f'2 + 2 = {2 + 2}')              # 2 + 2 = 4  ← expressions work

# string methods
s = '  Hello, World!  '
print(s.strip())            # 'Hello, World!'  — remove whitespace
print(s.lstrip())           # 'Hello, World!  '
print(s.rstrip())           # '  Hello, World!'
print(s.lower())            # '  hello, world!  '
print(s.upper())            # '  HELLO, WORLD!  '
print(s.title())            # '  Hello, World!  '
print(s.replace('World', 'Python'))
print(s.find('World'))      # 9   — index of first match (-1 if not found)
print(s.count('l'))         # 3
print(s.startswith('  H'))  # True
print(s.endswith('!  '))    # True
print(s.split(','))         # ['  Hello', ' World!  ']
print('|'.join(['a', 'b', 'c']))  # 'a|b|c'
print(s.strip().isalpha())  # False (has comma and space)
print('hello'.isalpha())    # True
print('123'.isdigit())      # True
print('abc123'.isalnum())   # True

# indexing and slicing
s = 'Python'
print(s[0])                 # P
print(s[-1])                # n
print(s[1:4])               # yth
print(s[::-1])              # nohtyP  (reversed)
print(s[::2])               # Pto     (every 2nd)

# string is immutable
# s[0] = 'J'                # TypeError!
s = 'J' + s[1:]             # create new string instead

# string formatting styles
name, age = 'Alice', 30
print('%s is %d years old' % (name, age))       # old style
print('{} is {} years old'.format(name, age))   # .format()
print(f'{name} is {age} years old')             # f-string (preferred)


# ═══════════════════════════════════════════════════════════════
# PART 5: bool
# ═══════════════════════════════════════════════════════════════
#
# bool is a subclass of int: True == 1, False == 0
# FALSY: 0, 0.0, '', [], {}, set(), None, False
# TRUTHY: everything else

t = True
f = False

print(type(t))              # <class 'bool'>
print(isinstance(t, int))   # True  ← bool IS-A int
print(int(t), int(f))       # 1 0
print(True + True)          # 2  ← bool arithmetic works
print(True * 5)             # 5

# logical operators
print(True and False)       # False
print(True or  False)       # True
print(not True)             # False

# short-circuit evaluation
# and → stops at first False
# or  → stops at first True
x = None
y = x or 'default'          # 'default'  ← x is falsy, returns y
z = x and 'value'           # None       ← x is falsy, returns x
print(y, z)

# truthiness of different types
print(bool(0))              # False
print(bool(0.0))            # False
print(bool(''))             # False
print(bool([]))             # False
print(bool(None))           # False
print(bool(42))             # True
print(bool('hi'))           # True
print(bool([1]))            # True


# ═══════════════════════════════════════════════════════════════
# PART 6: None
# ═══════════════════════════════════════════════════════════════
#
# None = the absence of a value (like null in other languages)
# There is only ONE None object in Python (singleton)

result = None
print(type(None))           # <class 'NoneType'>
print(result is None)       # True  ← always use 'is' not ==
print(result is not None)   # False

# common uses
def find(lst, target):
    for i, v in enumerate(lst):
        if v == target:
            return i
    return None             # explicit "not found"

idx = find([1, 2, 3], 5)
if idx is None:
    print('Not found')


# ═══════════════════════════════════════════════════════════════
# PART 7: TYPE CONVERSION
# ═══════════════════════════════════════════════════════════════

# implicit (Python does it automatically)
print(1 + 2.0)              # 3.0  ← int promoted to float

# explicit (you do it manually)
print(int('42'))            # 42
print(int(3.9))             # 3    (truncates, not rounds)
print(float('3.14'))        # 3.14
print(float(True))          # 1.0
print(str(100))             # '100'
print(str(3.14))            # '3.14'
print(bool(0))              # False
print(bool(''))             # False
print(bool('0'))            # True  ← non-empty string is truthy!
print(list('abc'))          # ['a', 'b', 'c']
print(tuple([1, 2, 3]))     # (1, 2, 3)

# safe conversion with error handling
def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(safe_int('42'))       # 42
print(safe_int('abc'))      # 0
print(safe_int(None))       # 0


# ═══════════════════════════════════════════════════════════════
# PART 8: IDENTITY vs EQUALITY
# ═══════════════════════════════════════════════════════════════
#
# ==  → checks VALUE equality (do they have the same value?)
# is  → checks IDENTITY (are they the SAME object in memory?)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)               # True  ← same value
print(a is b)               # False ← different objects
print(a is c)               # True  ← same object (c points to a)

# small int caching — Python caches -5 to 256
x = 256
y = 256
print(x is y)               # True  ← cached

x = 257
y = 257
print(x is y)               # False ← not cached (implementation detail)

# RULE: use == for value comparison, is only for None/True/False
print(None is None)         # True  ← correct
print(True is True)         # True  ← correct


# ═══════════════════════════════════════════════════════════════
# QUICK REFERENCE
# ═══════════════════════════════════════════════════════════════
#
#   int    → whole numbers, unlimited precision
#   float  → decimals, IEEE 754, use math.isclose() for comparison
#   str    → immutable sequence of chars, f-strings preferred
#   bool   → True/False, subclass of int
#   None   → absence of value, singleton, use 'is' not ==
#
#   ==  → value equality     is  → identity (same object)
#   int(), float(), str(), bool() → explicit type conversion
#   Decimal → exact decimal arithmetic (no float errors)
