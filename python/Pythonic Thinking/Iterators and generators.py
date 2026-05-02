# ═══════════════════════════════════════════════════════════════
#              ITERATORS & GENERATORS IN PYTHON
# ═══════════════════════════════════════════════════════════════
#
# ─────────────────────────────────────────────────────────────
# PART 1: ITERABLES vs ITERATORS
# ─────────────────────────────────────────────────────────────
#
# ITERABLE  → object you CAN loop over (list, tuple, str, dict)
#             has __iter__() method → returns an iterator
#
# ITERATOR  → object that DOES the looping
#             has __iter__() AND __next__() methods
#             remembers WHERE it is in the sequence
#             raises StopIteration when done
#
# ANALOGY: Book vs Bookmark 📚
#   Iterable  = the book       (you can read it)
#   Iterator  = the bookmark   (tracks your current page)
#   next()    = turn the page
#   You can make many bookmarks for one book (multiple iterators).
#
# HOW for loop works under the hood:
#   for x in [1, 2, 3]:
#   ↓ Python does this:
#   _iter = iter([1, 2, 3])      # calls __iter__()
#   while True:
#       try:
#           x = next(_iter)      # calls __next__()
#       except StopIteration:
#           break

nums = [1, 2, 3]
it   = iter(nums)          # create iterator from iterable

print(next(it))            # 1
print(next(it))            # 2
print(next(it))            # 3
# print(next(it))          # StopIteration ← uncomment to see error


# ─────────────────────────────────────────────────────────────
# PART 2: CUSTOM ITERATOR (using class)
# ─────────────────────────────────────────────────────────────
#
# Build your own iterator by implementing:
#   __iter__  → returns self
#   __next__  → returns next value or raises StopIteration
#
# ANALOGY: Vending machine 🎰
#   Each press of button (next()) gives you the next item.
#   When empty → machine says "sold out" (StopIteration).

class CountUp:
    def __init__(self, start, end):
        self.current = start
        self.end     = end

    def __iter__(self):
        return self          # iterator returns itself

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value        = self.current
        self.current += 1
        return value


counter = CountUp(1, 5)
for num in counter:
    print(num, end=' ')    # 1 2 3 4 5
print()

# can also use next() manually
counter2 = CountUp(10, 12)
print(next(counter2))      # 10
print(next(counter2))      # 11
print(next(counter2))      # 12


# ─────────────────────────────────────────────────────────────
# PART 3: GENERATORS (function with yield)
# ─────────────────────────────────────────────────────────────
#
# A generator is a SIMPLER way to create an iterator.
# Use yield instead of return → function pauses and resumes.
#
# ANALOGY: Netflix streaming 🎬 vs downloading
#   Regular function = download entire movie first, then watch
#   Generator        = stream → watch frame by frame, on demand
#                      only loads what you need RIGHT NOW
#
# KEY DIFFERENCE from regular function:
#   Regular function → runs fully, returns one value, forgets state
#   Generator        → pauses at yield, REMEMBERS state, resumes on next()
#
# HOW yield works:
#   1. Call generator function → returns a generator object (doesn't run yet)
#   2. Call next() → runs until yield → pauses → returns yielded value
#   3. Call next() again → resumes from where it paused
#   4. Function ends → StopIteration raised automatically

def count_up(start, end):
    current = start
    while current <= end:
        yield current        # pause here, send value out
        current += 1         # resume here on next next()


gen = count_up(1, 5)
print(type(gen))             # <class 'generator'>
print(next(gen))             # 1
print(next(gen))             # 2

for num in count_up(1, 5):
    print(num, end=' ')      # 1 2 3 4 5
print()


# ─────────────────────────────────────────────────────────────
# PART 4: WHY GENERATORS? — MEMORY EFFICIENCY
# ─────────────────────────────────────────────────────────────
#
# List builds ALL values in memory at once.
# Generator builds ONE value at a time → lazy evaluation.
#
# ANALOGY: Printing a book 📖
#   List      = print all 1000 pages before reading any
#   Generator = print one page, read it, print next page
#
# Example: range(1_000_000)
#   list(range(1_000_000)) → 8 MB in memory
#   range(1_000_000)       → 48 bytes (generator-like object)

import sys

big_list = [x * x for x in range(10_000)]
big_gen  = (x * x for x in range(10_000))   # generator expression

print(sys.getsizeof(big_list))   # ~87624 bytes
print(sys.getsizeof(big_gen))    # 104 bytes ← tiny!


# ─────────────────────────────────────────────────────────────
# PART 5: GENERATOR EXPRESSIONS
# ─────────────────────────────────────────────────────────────
#
# Like list comprehension but with () instead of []
# Lazy → values computed only when needed
#
#   list comp  → [x*2 for x in range(5)]  → builds full list
#   gen expr   → (x*2 for x in range(5))  → builds nothing yet

squares_gen = (x * x for x in range(1, 6))

print(next(squares_gen))   # 1
print(next(squares_gen))   # 4

# use directly in functions that accept iterables
total = sum(x * x for x in range(1, 6))
print(total)               # 55


# ─────────────────────────────────────────────────────────────
# PART 6: REAL-WORLD GENERATOR PATTERNS
# ─────────────────────────────────────────────────────────────

# PATTERN 1: Infinite sequence (impossible with list)
# ANALOGY: Tap water 🚰 → flows forever, you take what you need
def infinite_counter(start=0):
    n = start
    while True:
        yield n
        n += 1

counter = infinite_counter(1)
print(next(counter))   # 1
print(next(counter))   # 2
print(next(counter))   # 3  ← can go forever


# PATTERN 2: Pipeline — chain generators together
# ANALOGY: Assembly line 🏭 → each station processes and passes on
def read_numbers(nums):
    for n in nums:
        yield n

def filter_even(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

def square(nums):
    for n in nums:
        yield n * n

data     = read_numbers([1, 2, 3, 4, 5, 6])
evens    = filter_even(data)
squared  = square(evens)

print(list(squared))   # [4, 16, 36]  ← only even squares, lazily computed


# PATTERN 3: Read large file line by line (memory safe)
# ANALOGY: Reading a scroll 📜 → unroll one line at a time
def read_large_file(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()   # one line at a time, never loads full file


# PATTERN 4: Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(10)])  # [0,1,1,2,3,5,8,13,21,34]


# ─────────────────────────────────────────────────────────────
# PART 7: yield from (delegating to sub-generator)
# ─────────────────────────────────────────────────────────────
#
# yield from → delegate iteration to another iterable/generator
# cleaner than looping and yielding one by one

def chain(*iterables):
    for it in iterables:
        yield from it   # delegate to each iterable


print(list(chain([1, 2], [3, 4], [5])))   # [1, 2, 3, 4, 5]


# ─────────────────────────────────────────────────────────────
# PART 8: ITERATOR vs GENERATOR — QUICK COMPARISON
# ─────────────────────────────────────────────────────────────
#
#   Feature          Iterator (class)     Generator (function)
#   ─────────────────────────────────────────────────────────
#   How to create    __iter__ + __next__  def + yield
#   Code length      verbose              concise
#   State tracking   manual (self.x)      automatic (local vars)
#   Memory           depends on impl      always lazy
#   Use when         complex logic        simple sequences
#
# ─────────────────────────────────────────────────────────────
# PART 9: BUILT-IN ITERATORS (pythonic tools)
# ─────────────────────────────────────────────────────────────

from itertools import islice, chain as ichain, count, cycle, takewhile

# islice → take first n items from any iterator (like slicing but lazy)
gen = (x * x for x in range(100))
print(list(islice(gen, 5)))        # [0, 1, 4, 9, 16]

# count → infinite counter
c = count(10, 2)                   # start=10, step=2
print(list(islice(c, 5)))          # [10, 12, 14, 16, 18]

# cycle → repeat iterable forever
cyc = cycle([1, 2, 3])
print(list(islice(cyc, 7)))        # [1, 2, 3, 1, 2, 3, 1]

# takewhile → yield while condition is True, stop on first False
print(list(takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6])))  # [1, 2, 3, 4]

# enumerate → iterator that yields (index, value) pairs
for i, val in enumerate(['a', 'b', 'c'], start=1):
    print(f"{i}: {val}")           # 1: a  2: b  3: c

# zip → iterator that pairs elements from multiple iterables
for a, b in zip([1, 2, 3], ['x', 'y', 'z']):
    print(a, b)                    # 1 x  2 y  3 z
