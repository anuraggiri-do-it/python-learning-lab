# ============================================================
# Python Sets — Basic to Advanced
# ============================================================


# ── 1. CREATION ─────────────────────────────────────────────
empty       = set()             # NOT {} — that creates an empty dict
nums        = {1, 2, 3, 4, 5}
mixed       = {1, "hello", 3.14, True}
from_list   = set([1, 2, 2, 3, 3])     # {1, 2, 3} — duplicates removed
from_str    = set("hello")             # {'h', 'e', 'l', 'o'}


# ── 2. UNORDERED & NO DUPLICATES ────────────────────────────
s = {3, 1, 4, 1, 5, 9, 2, 6, 5}
print(s)            # order not guaranteed, duplicates removed
print(len(s))       # 7


# ── 3. MEMBERSHIP TEST ──────────────────────────────────────
fruits = {"apple", "banana", "cherry"}

print("apple" in fruits)        # True  → O(1)
print("grape" not in fruits)    # True


# ── 4. ADDING & REMOVING ELEMENTS ───────────────────────────
s = {1, 2, 3}

s.add(4)            # add single element
s.update([5, 6, 7]) # add multiple elements

s.remove(3)         # raises KeyError if not found
s.discard(99)       # safe remove — no error if missing
popped = s.pop()    # remove & return an arbitrary element
s.clear()           # empty the set


# ── 5. SET OPERATIONS ────────────────────────────────────────
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union — all elements from both
print(a | b)            # {1, 2, 3, 4, 5, 6}
print(a.union(b))

# Intersection — common elements
print(a & b)            # {3, 4}
print(a.intersection(b))

# Difference — in a but not b
print(a - b)            # {1, 2}
print(a.difference(b))

# Symmetric Difference — in either but not both
print(a ^ b)            # {1, 2, 5, 6}
print(a.symmetric_difference(b))


# ── 6. IN-PLACE SET OPERATIONS ──────────────────────────────
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a |= b              # union in-place
a &= b              # intersection in-place
a -= b              # difference in-place
a ^= b              # symmetric difference in-place


# ── 7. SUBSET & SUPERSET ────────────────────────────────────
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))        # True  — a ⊆ b
print(a <= b)               # True  — same as issubset
print(a < b)                # True  — proper subset (a ≠ b)

print(b.issuperset(a))      # True  — b ⊇ a
print(b >= a)               # True

print(a.isdisjoint({5, 6})) # True  — no common elements


# ── 8. ITERATION ─────────────────────────────────────────────
colors = {"red", "green", "blue"}

for color in colors:
    print(color)            # order not guaranteed

# sorted iteration
for color in sorted(colors):
    print(color)


# ── 9. SET COMPREHENSIONS ────────────────────────────────────
squares     = {x**2 for x in range(1, 6)}          # {1, 4, 9, 16, 25}
even_sq     = {x**2 for x in range(10) if x % 2 == 0}
unique_lens = {len(w) for w in ["hi", "hello", "hey", "world"]}


# ── 10. FROZENSET — IMMUTABLE SET ───────────────────────────
fs = frozenset([1, 2, 3, 2, 1])    # frozenset({1, 2, 3})

# frozenset is hashable → can be used as dict key or set element
d = {frozenset({1, 2}): "pair"}
nested_set = {frozenset({1, 2}), frozenset({3, 4})}

# supports all read operations but NOT add/remove/update
print(1 in fs)
print(fs | {4, 5})          # returns new frozenset


# ── 11. COMMON USE CASES ─────────────────────────────────────
# Remove duplicates from a list (order not preserved)
lst    = [3, 1, 4, 1, 5, 9, 2, 6, 5]
unique = list(set(lst))

# Fast membership lookup vs list
big_set  = set(range(1_000_000))
print(999_999 in big_set)   # O(1)

# Find common / unique items between two collections
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common  = set(list_a) & set(list_b)     # {4, 5}
only_a  = set(list_a) - set(list_b)     # {1, 2, 3}


# ── 12. SET vs LIST vs DICT KEYS ────────────────────────────
# set   → unordered, mutable,   no duplicates, O(1) lookup
# list  → ordered,   mutable,   allows duplicates, O(n) lookup
# dict  → ordered,   mutable,   unique keys, O(1) key lookup

# Elements must be HASHABLE to be in a set
# valid:   {1, "hello", (1,2), frozenset()}
# invalid: {[1,2]}  ← TypeError: unhashable type: 'list'


# ── 13. PERFORMANCE NOTES ───────────────────────────────────
# add / discard / remove  → O(1) average
# in                      → O(1) average
# union / intersection    → O(len(a) + len(b))
# issubset                → O(len(a))
