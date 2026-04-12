# ============================================================
# Python Lists — Basic to Advanced
# ============================================================


# ── 1. CREATION ─────────────────────────────────────────────
empty = []
nums = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]
from_range = list(range(1, 6))          # [1, 2, 3, 4, 5]
repeated = [0] * 5                      # [0, 0, 0, 0, 0]


# ── 2. INDEXING & SLICING ────────────────────────────────────
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[0])        # apple
print(fruits[-1])       # elderberry
print(fruits[1:3])      # ['banana', 'cherry']
print(fruits[::-1])     # reversed
print(fruits[::2])      # every 2nd element


# ── 3. BASIC OPERATIONS ──────────────────────────────────────
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)            # concatenation → [1,2,3,4,5,6]
print(a * 2)            # repetition    → [1,2,3,1,2,3]
print(3 in a)           # membership    → True
print(len(a))           # length        → 3


# ── 4. MUTABILITY ────────────────────────────────────────────
nums = [10, 20, 30]
nums[1] = 99            # modify by index → [10, 99, 30]
nums[0:2] = [1, 2]      # slice assignment → [1, 2, 30]


# ── 5. COMMON METHODS ────────────────────────────────────────
lst = [3, 1, 4, 1, 5, 9, 2, 6]

lst.append(7)           # add to end
lst.insert(0, 0)        # insert at index
lst.extend([8, 9])      # add multiple items

lst.remove(1)           # remove first occurrence of value
popped = lst.pop()      # remove & return last item
popped_idx = lst.pop(0) # remove & return item at index

lst.sort()              # sort in-place
lst.reverse()           # reverse in-place
lst.clear()             # empty the list

lst = [3, 1, 4, 1, 5]
print(lst.index(4))     # index of value → 2
print(lst.count(1))     # count occurrences → 2
copy = lst.copy()       # shallow copy


# ── 6. ITERATION ─────────────────────────────────────────────
colors = ["red", "green", "blue"]

for color in colors:
    print(color)

for i, color in enumerate(colors):
    print(i, color)

# zip two lists
sizes = ["S", "M", "L"]
for color, size in zip(colors, sizes):
    print(color, size)


# ── 7. LIST COMPREHENSIONS ───────────────────────────────────
squares = [x**2 for x in range(1, 6)]              # [1,4,9,16,25]
evens   = [x for x in range(10) if x % 2 == 0]    # [0,2,4,6,8]
flat    = [n for row in nested for n in row]       # flatten nested
matrix  = [[i * j for j in range(1, 4)] for i in range(1, 4)]


# ── 8. SORTING ───────────────────────────────────────────────
words = ["banana", "apple", "cherry", "date"]

sorted_asc  = sorted(words)                        # new list, ascending
sorted_desc = sorted(words, reverse=True)          # descending
sorted_len  = sorted(words, key=len)               # by length

# sort list of dicts
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
people.sort(key=lambda p: p["age"])


# ── 9. COPYING — SHALLOW vs DEEP ────────────────────────────
import copy

original = [[1, 2], [3, 4]]
shallow  = original.copy()          # inner lists still shared
deep     = copy.deepcopy(original)  # fully independent

shallow[0][0] = 99   # also changes original[0][0]
deep[0][0]    = 99   # does NOT affect original


# ── 10. UNPACKING ────────────────────────────────────────────
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5

a, b, c = [10, 20, 30]


# ── 11. USEFUL BUILT-INS WITH LISTS ─────────────────────────
nums = [3, 1, 4, 1, 5, 9]

print(min(nums))            # 1
print(max(nums))            # 9
print(sum(nums))            # 23
print(any(x > 8 for x in nums))    # True
print(all(x > 0 for x in nums))    # True

# map / filter
doubled  = list(map(lambda x: x * 2, nums))
filtered = list(filter(lambda x: x > 3, nums))


# ── 12. STACK & QUEUE USING LIST ────────────────────────────
# Stack (LIFO)
stack = []
stack.append(1)
stack.append(2)
stack.pop()             # → 2

# Queue (FIFO) — use deque for O(1) popleft
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
queue.popleft()         # → 1


# ── 13. LIST vs TUPLE vs SET ─────────────────────────────────
lst   = [1, 2, 2, 3]    # ordered, mutable, allows duplicates
tup   = (1, 2, 2, 3)    # ordered, immutable, allows duplicates
st    = {1, 2, 2, 3}    # unordered, mutable, NO duplicates → {1,2,3}

unique = list(set(lst))  # remove duplicates from list


# ── 14. ADVANCED — PERFORMANCE NOTES ────────────────────────
# append()  → O(1) amortized
# insert(0) → O(n)  ← avoid for large lists; use deque
# in        → O(n)  ← use set for O(1) lookup
# sort()    → O(n log n)

# For large numeric data prefer numpy arrays over lists
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
