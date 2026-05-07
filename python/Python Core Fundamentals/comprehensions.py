# ═══════════════════════════════════════════════════════════════
#         COMPREHENSIONS — Pythonic One-Liners
# ═══════════════════════════════════════════════════════════════
#
# WHAT ARE COMPREHENSIONS?
# ─────────────────────────────────────────────────────────────
# A concise way to build collections from iterables.
# Replaces verbose for-loops with a single readable expression.
#
# ANALOGY: Assembly line 🏭
#   Regular loop = worker picks each item, processes, puts in box
#   Comprehension = automated conveyor belt — filter + transform
#                   in one smooth motion
#
# FOUR TYPES:
#   [...]  → list comprehension   → returns list
#   {...}  → dict comprehension   → returns dict
#   {...}  → set comprehension    → returns set
#   (...)  → generator expression → returns lazy iterator


# ═══════════════════════════════════════════════════════════════
# PART 1: LIST COMPREHENSION
# ═══════════════════════════════════════════════════════════════
#
# SYNTAX: [expression for item in iterable if condition]
#
# READ IT RIGHT TO LEFT:
#   "for each item in iterable, if condition, give me expression"

# basic
squares = [x ** 2 for x in range(1, 6)]
print(squares)                              # [1, 4, 9, 16, 25]

# with filter
evens = [x for x in range(10) if x % 2 == 0]
print(evens)                                # [0, 2, 4, 6, 8]

# transform strings
upper = [s.upper() for s in ['hello', 'world']]
print(upper)                                # ['HELLO', 'WORLD']

# conditional expression (ternary) inside
labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(labels)                               # ['even','odd','even','odd','even']

# from another list
words   = ['apple', 'banana', 'cherry', 'date']
lengths = [len(w) for w in words]
print(lengths)                              # [5, 6, 6, 4]

long_words = [w for w in words if len(w) > 5]
print(long_words)                           # ['banana', 'cherry']

# ── nested list comprehension ────────────────────────────────
# ANALOGY: Nested for-loops collapsed into one line

# multiplication table
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)                               # [[1,2,3],[2,4,6],[3,6,9]]

# flatten nested list
flat = [x for row in matrix for x in row]
print(flat)                                 # [1,2,3,2,4,6,3,6,9]

# cartesian product (all pairs)
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b'] if x != 2]
print(pairs)                                # [(1,'a'),(1,'b'),(3,'a'),(3,'b')]

# ── vs regular loop ──────────────────────────────────────────
# LOOP version:
result = []
for x in range(5):
    if x % 2 == 0:
        result.append(x ** 2)

# COMPREHENSION version (same result, one line):
result = [x ** 2 for x in range(5) if x % 2 == 0]
print(result)                               # [0, 4, 16]


# ═══════════════════════════════════════════════════════════════
# PART 2: DICT COMPREHENSION
# ═══════════════════════════════════════════════════════════════
#
# SYNTAX: {key: value for item in iterable if condition}

# basic
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(squares_dict)                         # {1:1, 2:4, 3:9, 4:16, 5:25}

# invert a dict (swap keys and values)
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted)                             # {1:'a', 2:'b', 3:'c'}

# filter dict — keep only passing scores
scores = {'Alice': 85, 'Bob': 45, 'Charlie': 92, 'Diana': 38}
passed = {name: score for name, score in scores.items() if score >= 50}
print(passed)                               # {'Alice':85, 'Charlie':92}

# build dict from two lists
keys   = ['name', 'age', 'city']
values = ['Alice', 25, 'Delhi']
profile = {k: v for k, v in zip(keys, values)}
print(profile)                              # {'name':'Alice','age':25,'city':'Delhi'}

# transform values
upper_scores = {k: v * 1.1 for k, v in scores.items()}  # 10% bonus
print(upper_scores)

# nested dict comprehension
matrix_dict = {i: {j: i * j for j in range(1, 4)} for i in range(1, 4)}
print(matrix_dict)
# {1: {1:1, 2:2, 3:3}, 2: {1:2, 2:4, 3:6}, 3: {1:3, 2:6, 3:9}}


# ═══════════════════════════════════════════════════════════════
# PART 3: SET COMPREHENSION
# ═══════════════════════════════════════════════════════════════
#
# SYNTAX: {expression for item in iterable if condition}
# Same as list comprehension but with {} → result has NO duplicates

unique_squares = {x ** 2 for x in [-2, -1, 0, 1, 2]}
print(unique_squares)                       # {0, 1, 4}  (no duplicates)

nums = [1, 2, 2, 3, 3, 4, 4, 4]
unique_evens = {x for x in nums if x % 2 == 0}
print(unique_evens)                         # {2, 4}

# remove duplicates while transforming
words = ['Hello', 'WORLD', 'hello', 'Python', 'PYTHON']
unique_lower = {w.lower() for w in words}
print(unique_lower)                         # {'hello', 'world', 'python'}

# find unique word lengths
sentences = ['hi there', 'hello world', 'hey']
unique_lens = {len(w) for s in sentences for w in s.split()}
print(unique_lens)                          # {2, 3, 5}


# ═══════════════════════════════════════════════════════════════
# PART 4: GENERATOR EXPRESSION
# ═══════════════════════════════════════════════════════════════
#
# SYNTAX: (expression for item in iterable if condition)
# Looks like list comprehension with () but is LAZY — values
# computed one at a time only when needed.
#
# ANALOGY: Streaming vs downloading 🎬
#   List comprehension = download entire movie first
#   Generator expression = stream frame by frame on demand
#
# USE WHEN: large data, only need to iterate once, pass to sum/max/min

gen = (x ** 2 for x in range(5))
print(type(gen))                            # <class 'generator'>
print(next(gen))                            # 0
print(next(gen))                            # 1
print(list(gen))                            # [4, 9, 16]  ← remaining

# memory comparison
import sys
big_list = [x * x for x in range(10_000)]
big_gen  = (x * x for x in range(10_000))
print(sys.getsizeof(big_list))              # ~87624 bytes
print(sys.getsizeof(big_gen))              # 104 bytes

# use directly in functions — no extra [] needed
total   = sum(x ** 2 for x in range(100))
maximum = max(len(w) for w in ['apple', 'banana', 'cherry'])
exists  = any(x > 90 for x in [85, 92, 78])
all_pos = all(x > 0 for x in [1, 2, 3, 4])

print(total, maximum, exists, all_pos)      # 328350  6  True  True


# ═══════════════════════════════════════════════════════════════
# PART 5: ADVANCED PATTERNS
# ═══════════════════════════════════════════════════════════════

# ── pattern 1: flatten + filter in one ───────────────────────
data = [[1, -2, 3], [-4, 5, -6], [7, 8, -9]]
positives = [x for row in data for x in row if x > 0]
print(positives)                            # [1, 3, 5, 7, 8]

# ── pattern 2: transpose a matrix ────────────────────────────
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)                           # [[1,4,7],[2,5,8],[3,6,9]]

# ── pattern 3: group by first letter ─────────────────────────
from collections import defaultdict
words = ['apple', 'ant', 'banana', 'bear', 'cherry']
grouped = {letter: [w for w in words if w[0] == letter]
           for letter in set(w[0] for w in words)}
print(grouped)                              # {'a':['apple','ant'],'b':['banana','bear'],'c':['cherry']}

# ── pattern 4: dict from function results ────────────────────
import math
trig = {angle: round(math.sin(math.radians(angle)), 4)
        for angle in range(0, 91, 30)}
print(trig)                                 # {0:0.0, 30:0.5, 60:0.866, 90:1.0}

# ── pattern 5: conditional dict building ─────────────────────
data = [('Alice', 85), ('Bob', None), ('Charlie', 92), ('Diana', None)]
valid = {name: score for name, score in data if score is not None}
print(valid)                                # {'Alice':85, 'Charlie':92}

# ── pattern 6: nested list to dict ───────────────────────────
pairs = [['name', 'Alice'], ['age', 25], ['city', 'Delhi']]
d = {k: v for k, v in pairs}
print(d)                                    # {'name':'Alice','age':25,'city':'Delhi'}


# ═══════════════════════════════════════════════════════════════
# PART 6: WHEN NOT TO USE COMPREHENSIONS
# ═══════════════════════════════════════════════════════════════
#
# ✅ USE comprehension when:
#   - simple transform or filter
#   - result fits on one readable line
#   - building a new collection
#
# ❌ AVOID comprehension when:
#   - logic is complex (multiple conditions, nested logic)
#   - side effects needed (printing, writing to file)
#   - readability suffers
#   - you need to reuse the loop variable after

# BAD — too complex, hard to read
result = [x ** 2 if x % 2 == 0 else x ** 3 if x % 3 == 0 else x
          for x in range(20) if x > 5 and x < 15]

# GOOD — use a regular loop for complex logic
result = []
for x in range(20):
    if 5 < x < 15:
        if x % 2 == 0:
            result.append(x ** 2)
        elif x % 3 == 0:
            result.append(x ** 3)
        else:
            result.append(x)


# ═══════════════════════════════════════════════════════════════
# QUICK REFERENCE
# ═══════════════════════════════════════════════════════════════
#
#   [expr for x in it]              → list
#   [expr for x in it if cond]      → filtered list
#   [expr for x in it for y in it2] → nested (cartesian)
#
#   {k: v for x in it}              → dict
#   {expr for x in it}              → set (no duplicates)
#   (expr for x in it)              → generator (lazy)
#
#   sum/max/min/any/all(expr for x in it) → use generator directly
