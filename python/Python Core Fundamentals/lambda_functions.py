# ═══════════════════════════════════════════════════════════════
#         LAMBDA FUNCTIONS — Anonymous Functions
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS A LAMBDA?
# ─────────────────────────────────────────────────────────────
# A lambda is a small, anonymous (nameless) function defined
# in a single expression. No def, no return, no name needed.
#
# SYNTAX:  lambda arguments: expression
#
# ANALOGY: Post-it note vs printed document 📝
#   Regular function = printed, filed, reusable document
#   Lambda           = quick post-it note — write once, use once
#                      no need to name it or file it away
#
# WHEN TO USE:
#   ✅ Short, throwaway functions (sort keys, map/filter)
#   ✅ Passed directly as argument to another function
#   ✅ One-liner logic that doesn't need a name
#   ❌ Complex logic (use def instead)
#   ❌ When you need docstrings or multiple statements


# ═══════════════════════════════════════════════════════════════
# PART 1: BASICS
# ═══════════════════════════════════════════════════════════════

# regular function
def square(x):
    return x ** 2

# equivalent lambda
square_l = lambda x: x ** 2

print(square(5))    # 25
print(square_l(5))  # 25

# multiple arguments
add  = lambda a, b: a + b
mul  = lambda a, b, c: a * b * c
print(add(3, 4))    # 7
print(mul(2, 3, 4)) # 24

# no arguments
greet = lambda: 'Hello, World!'
print(greet())      # Hello, World!

# default arguments
power = lambda base, exp=2: base ** exp
print(power(3))     # 9   (exp defaults to 2)
print(power(3, 3))  # 27

# conditional expression (ternary)
even_odd  = lambda x: 'even' if x % 2 == 0 else 'odd'
clamp     = lambda x, lo, hi: lo if x < lo else (hi if x > hi else x)
print(even_odd(4))          # even
print(clamp(15, 0, 10))     # 10


# ═══════════════════════════════════════════════════════════════
# PART 2: LAMBDA WITH sorted()
# ═══════════════════════════════════════════════════════════════
#
# sorted(iterable, key=func) — key= is where lambdas shine
# The key function is called on each element to get sort value

names = ['Anurag', 'Zara', 'Mia', 'Bob', 'Charlie']

print(sorted(names))                                # alphabetical
print(sorted(names, key=lambda x: len(x)))          # by length
print(sorted(names, key=lambda x: x[-1]))           # by last char
print(sorted(names, key=lambda x: x.lower()))       # case-insensitive

# sort list of tuples
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('Diana', 92)]
print(sorted(students, key=lambda s: s[1]))                     # by score asc
print(sorted(students, key=lambda s: s[1], reverse=True))       # by score desc
print(sorted(students, key=lambda s: (-s[1], s[0])))            # score desc, name asc

# sort list of dicts
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob',   'age': 25},
    {'name': 'Carol', 'age': 35},
]
print(sorted(people, key=lambda p: p['age']))           # by age
print(sorted(people, key=lambda p: p['name']))          # by name

# in-place sort
students_list = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
students_list.sort(key=lambda s: s[1])
print(students_list)


# ═══════════════════════════════════════════════════════════════
# PART 3: LAMBDA WITH map()
# ═══════════════════════════════════════════════════════════════
#
# map(func, iterable) → applies func to every element
# ANALOGY: Stamp machine 🔖 — stamps every item passing through

nums    = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))
print(squares)                              # [1, 4, 9, 16, 25]

doubled = list(map(lambda x: x * 2, nums))
print(doubled)                              # [2, 4, 6, 8, 10]

# map with multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)                                 # [11, 22, 33]

# transform strings
words = ['hello', 'world', 'python']
print(list(map(lambda w: w.capitalize(), words)))   # ['Hello','World','Python']
print(list(map(lambda w: w[::-1], words)))          # ['olleh','dlrow','nohtyp']

# NOTE: list comprehension is often more readable than map+lambda
# map version:  list(map(lambda x: x**2, nums))
# comp version: [x**2 for x in nums]  ← preferred


# ═══════════════════════════════════════════════════════════════
# PART 4: LAMBDA WITH filter()
# ═══════════════════════════════════════════════════════════════
#
# filter(func, iterable) → keeps elements where func returns True
# ANALOGY: Sieve 🪣 — only items that pass through the holes

nums  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)                                # [2, 4, 6, 8, 10]

odds  = list(filter(lambda x: x % 2 != 0, nums))
print(odds)                                 # [1, 3, 5, 7, 9]

# filter strings
words = ['apple', 'ant', 'banana', 'bear', 'cherry']
a_words = list(filter(lambda w: w.startswith('a'), words))
print(a_words)                              # ['apple', 'ant']

long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)                           # ['banana', 'cherry']

# filter None values
data = [1, None, 3, None, 5, None]
clean = list(filter(None, data))            # None itself as filter removes falsy
print(clean)                                # [1, 3, 5]


# ═══════════════════════════════════════════════════════════════
# PART 5: LAMBDA WITH reduce()
# ═══════════════════════════════════════════════════════════════
#
# reduce(func, iterable) → applies func cumulatively
# ANALOGY: Snowball rolling downhill ⛄
#   Starts with first two elements, combines them,
#   then combines result with next element, and so on

from functools import reduce

nums    = [1, 2, 3, 4, 5]
total   = reduce(lambda acc, x: acc + x, nums)
product = reduce(lambda acc, x: acc * x, nums)
maximum = reduce(lambda a, b: a if a > b else b, nums)

print(total)    # 15
print(product)  # 120
print(maximum)  # 5

# with initial value
total_with_start = reduce(lambda acc, x: acc + x, nums, 100)
print(total_with_start)  # 115  (100 + 1+2+3+4+5)

# flatten list of lists
nested = [[1, 2], [3, 4], [5, 6]]
flat   = reduce(lambda acc, x: acc + x, nested)
print(flat)     # [1, 2, 3, 4, 5, 6]


# ═══════════════════════════════════════════════════════════════
# PART 6: LAMBDA IN DATA STRUCTURES
# ═══════════════════════════════════════════════════════════════

# dict of operations (dispatch table)
ops = {
    'add': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mul': lambda a, b: a * b,
    'div': lambda a, b: a / b if b != 0 else 'undefined',
    'pow': lambda a, b: a ** b,
}
print(ops['add'](10, 5))    # 15
print(ops['pow'](2, 8))     # 256

# list of transformations (pipeline)
transforms = [
    lambda x: x * 2,
    lambda x: x + 10,
    lambda x: x ** 2,
]
value = 3
for fn in transforms:
    value = fn(value)
print(value)                # ((3*2)+10)^2 = 256


# ═══════════════════════════════════════════════════════════════
# PART 7: IMMEDIATELY INVOKED LAMBDA (IIFE)
# ═══════════════════════════════════════════════════════════════
# Define and call in one expression — useful in functional patterns

result = (lambda x, y: x ** 2 + y ** 2)(3, 4)
print(result)               # 25


# ═══════════════════════════════════════════════════════════════
# PART 8: LAMBDA vs DEF — WHEN TO USE WHICH
# ═══════════════════════════════════════════════════════════════
#
#   Feature          lambda              def
#   ─────────────────────────────────────────────────────────
#   Syntax           one expression      multiple statements
#   Name             anonymous           named
#   Docstring        no                  yes
#   Reusability      low (throwaway)     high
#   Readability      good for short      better for complex
#   Debugging        harder (no name)    easier (named in traceback)
#   Return           implicit            explicit return
#
# RULE: if you're assigning lambda to a variable → use def instead
#
# BAD:
double = lambda x: x * 2       # pointless — just use def
#
# GOOD:
def double(x):
    return x * 2
#
# GOOD use of lambda (inline, throwaway):
nums = [3, 1, 4, 1, 5]
nums.sort(key=lambda x: -x)    # sort descending inline
print(nums)                     # [5, 4, 3, 1, 1]


# ═══════════════════════════════════════════════════════════════
# PART 9: PRACTICAL PATTERNS
# ═══════════════════════════════════════════════════════════════

# ── pattern 1: multi-key sort ────────────────────────────────
employees = [
    {'name': 'Alice', 'dept': 'Eng',  'salary': 90000},
    {'name': 'Bob',   'dept': 'Mkt',  'salary': 75000},
    {'name': 'Carol', 'dept': 'Eng',  'salary': 85000},
    {'name': 'Dave',  'dept': 'Mkt',  'salary': 80000},
]
# sort by dept asc, then salary desc within dept
sorted_emp = sorted(employees, key=lambda e: (e['dept'], -e['salary']))
for e in sorted_emp:
    print(e['dept'], e['name'], e['salary'])

# ── pattern 2: conditional transform ─────────────────────────
prices = [10.5, 20.0, 5.75, 15.25, 8.0]
discounted = list(map(lambda p: p * 0.9 if p > 10 else p, prices))
print(discounted)

# ── pattern 3: extract field from list of dicts ──────────────
names = list(map(lambda e: e['name'], employees))
print(names)                                # ['Alice','Bob','Carol','Dave']

# ── pattern 4: combine map + filter ──────────────────────────
nums = range(1, 21)
result = list(map(lambda x: x ** 2,
                  filter(lambda x: x % 3 == 0, nums)))
print(result)                               # [9, 36, 81, 144, 225, 324]
# squares of multiples of 3 up to 20
