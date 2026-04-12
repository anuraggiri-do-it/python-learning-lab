# ============================================================
# Python Tuples — Basic to Advanced
# ============================================================


# ── 1. CREATION ─────────────────────────────────────────────
empty       = ()
single      = (42,)             # trailing comma is REQUIRED for single item
single_bad  = (42)              # ← this is just int 42, NOT a tuple
coords      = (10, 20)
mixed       = (1, "hello", 3.14, True, None)
nested      = ((1, 2), (3, 4))
from_list   = tuple([1, 2, 3])
from_range  = tuple(range(1, 6))    # (1, 2, 3, 4, 5)
no_parens   = 1, 2, 3               # packing — parens optional


# ── 2. INDEXING & SLICING ────────────────────────────────────
t = (10, 20, 30, 40, 50)

print(t[0])         # 10
print(t[-1])        # 50
print(t[1:3])       # (20, 30)
print(t[::-1])      # reversed → (50, 40, 30, 20, 10)
print(t[::2])       # every 2nd → (10, 30, 50)


# ── 3. IMMUTABILITY ──────────────────────────────────────────
t = (1, 2, 3)
# t[0] = 99       # ← TypeError: 'tuple' object does not support item assignment

# BUT if a tuple contains a mutable object, that object can change
t_with_list = (1, [2, 3], 4)
t_with_list[1].append(99)   # valid → (1, [2, 3, 99], 4)


# ── 4. BASIC OPERATIONS ──────────────────────────────────────
a = (1, 2, 3)
b = (4, 5, 6)

print(a + b)        # concatenation → (1,2,3,4,5,6)
print(a * 2)        # repetition    → (1,2,3,1,2,3)
print(3 in a)       # membership    → True
print(len(a))       # length        → 3


# ── 5. TUPLE METHODS ─────────────────────────────────────────
t = (3, 1, 4, 1, 5, 9, 1)

print(t.count(1))   # count occurrences → 3
print(t.index(4))   # first index of value → 2
# t.index(99)       # ← ValueError if not found


# ── 6. UNPACKING ─────────────────────────────────────────────
x, y, z = (10, 20, 30)

# starred unpacking
first, *middle, last = (1, 2, 3, 4, 5)
# first=1, middle=[2,3,4], last=5

# swap variables (uses tuple packing/unpacking)
a, b = 5, 10
a, b = b, a         # a=10, b=5

# nested unpacking
(x1, y1), (x2, y2) = (1, 2), (3, 4)


# ── 7. ITERATION ─────────────────────────────────────────────
colors = ("red", "green", "blue")

for color in colors:
    print(color)

for i, color in enumerate(colors):
    print(i, color)

# zip
sizes = ("S", "M", "L")
for color, size in zip(colors, sizes):
    print(color, size)


# ── 8. TUPLE AS DICTIONARY KEY ───────────────────────────────
# Tuples are hashable (if all elements are hashable) → can be dict keys
grid = {}
grid[(0, 0)] = "start"
grid[(3, 4)] = "end"

# Lists cannot be dict keys (unhashable)
# {[0, 0]: "start"}  ← TypeError


# ── 9. NAMED TUPLES ──────────────────────────────────────────
from collections import namedtuple

Point   = namedtuple("Point", ["x", "y"])
Person  = namedtuple("Person", ["name", "age"])

p = Point(3, 4)
print(p.x, p.y)         # access by name
print(p[0], p[1])       # still accessible by index

alice = Person("Alice", 30)
print(alice.name, alice.age)

# _replace returns a NEW tuple with changed fields (immutable)
p2 = p._replace(x=10)

# convert to dict
print(alice._asdict())  # {'name': 'Alice', 'age': 30}


# ── 10. TUPLE vs LIST — WHEN TO USE WHICH ───────────────────
# Use TUPLE when:
#   - data should not change (coordinates, RGB, DB records)
#   - used as dict key or set element
#   - returning multiple values from a function
#   - slight memory/performance advantage over list

# Use LIST when:
#   - collection needs to grow/shrink
#   - items need to be modified

import sys
lst = [1, 2, 3, 4, 5]
tup = (1, 2, 3, 4, 5)
print(sys.getsizeof(lst))   # larger
print(sys.getsizeof(tup))   # smaller


# ── 11. RETURNING MULTIPLE VALUES FROM FUNCTIONS ─────────────
def min_max(nums):
    return min(nums), max(nums)     # returns a tuple

lo, hi = min_max([3, 1, 4, 1, 5, 9])
print(lo, hi)   # 1 9


# ── 12. TUPLE COMPREHENSION? → GENERATOR ────────────────────
# There is NO tuple comprehension — () with expression gives a generator
gen  = (x**2 for x in range(5))    # generator object
tup  = tuple(x**2 for x in range(5))   # convert to tuple → (0,1,4,9,16)


# ── 13. SORTING TUPLES ───────────────────────────────────────
points = [(3, 1), (1, 4), (2, 2), (1, 1)]

sorted_points = sorted(points)              # sorts by first element, then second
by_second     = sorted(points, key=lambda p: p[1])
by_sum        = sorted(points, key=lambda p: p[0] + p[1])


# ── 14. ADVANCED — PERFORMANCE & INTERNALS ──────────────────
# Tuples are stored more compactly than lists
# CPython caches small tuples (length 0–20) for reuse → faster creation
# Tuple iteration is slightly faster than list iteration

# Tuple hashing
t = (1, 2, 3)
print(hash(t))          # valid — tuples are hashable
s = {(0,0), (1,1)}      # tuples in a set

# Unpacking in loops (common pattern)
pairs = [(1, "one"), (2, "two"), (3, "three")]
for num, word in pairs:
    print(num, word)
