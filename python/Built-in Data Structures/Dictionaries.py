# ============================================================
# Python Dictionaries — Basic to Advanced
# ============================================================


# ── 1. CREATION ─────────────────────────────────────────────
empty       = {}
person      = {"name": "Alice", "age": 30, "city": "NYC"}
from_keys   = dict.fromkeys(["a", "b", "c"], 0)    # {'a':0,'b':0,'c':0}
from_pairs  = dict([("x", 1), ("y", 2)])
from_kwargs = dict(name="Bob", age=25)
nested      = {"user": {"id": 1, "roles": ["admin", "user"]}}


# ── 2. ACCESSING VALUES ──────────────────────────────────────
d = {"name": "Alice", "age": 30}

print(d["name"])            # Alice — KeyError if missing
print(d.get("age"))         # 30
print(d.get("email", "N/A"))# N/A — default if key missing


# ── 3. ADDING & UPDATING ─────────────────────────────────────
d["email"] = "alice@example.com"    # add new key
d["age"]   = 31                     # update existing key
d.update({"city": "NYC", "age": 32})# update multiple keys at once
d.update(country="US")              # keyword-style update


# ── 4. REMOVING ELEMENTS ─────────────────────────────────────
d = {"a": 1, "b": 2, "c": 3, "d": 4}

val     = d.pop("a")           # remove & return value → 1
val_def = d.pop("z", None)     # safe pop — no KeyError
last    = d.popitem()          # remove & return last inserted (key, val)
del d["b"]                     # delete by key
d.clear()                      # empty the dict


# ── 5. MEMBERSHIP & LENGTH ───────────────────────────────────
d = {"x": 10, "y": 20}

print("x" in d)         # True  — checks KEYS only, O(1)
print("z" not in d)     # True
print(len(d))           # 2


# ── 6. VIEWS — keys / values / items ────────────────────────
d = {"a": 1, "b": 2, "c": 3}

print(d.keys())         # dict_keys(['a', 'b', 'c'])
print(d.values())       # dict_values([1, 2, 3])
print(d.items())        # dict_items([('a',1),('b',2),('c',3)])

# Views are LIVE — they reflect changes to the dict
keys_view = d.keys()
d["d"] = 4
print(keys_view)        # dict_keys(['a', 'b', 'c', 'd'])


# ── 7. ITERATION ─────────────────────────────────────────────
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

for key in scores:                      # iterate keys
    print(key)

for val in scores.values():             # iterate values
    print(val)

for name, score in scores.items():      # iterate key-value pairs
    print(f"{name}: {score}")

# sorted iteration
for name in sorted(scores):
    print(name, scores[name])


# ── 8. DICT COMPREHENSIONS ───────────────────────────────────
squares     = {x: x**2 for x in range(1, 6)}           # {1:1, 2:4, ...}
filtered    = {k: v for k, v in squares.items() if v > 5}
inverted    = {v: k for k, v in {"a": 1, "b": 2}.items()}
word_len    = {w: len(w) for w in ["apple", "banana", "cherry"]}


# ── 9. MERGING DICTS ─────────────────────────────────────────
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}

merged_update = {**a, **b}      # {x:1, y:99, z:3} — b wins on conflict
merged_or     = a | b           # Python 3.9+ — same result
a |= b                          # Python 3.9+ — in-place merge


# ── 10. SETDEFAULT & DEFAULT VALUES ─────────────────────────
d = {}

d.setdefault("count", 0)        # sets key only if missing → 0
d.setdefault("count", 99)       # key exists, no change → still 0

# defaultdict — auto-initializes missing keys
from collections import defaultdict

word_count  = defaultdict(int)
char_groups = defaultdict(list)

for word in ["apple", "banana", "apple", "cherry"]:
    word_count[word] += 1           # no KeyError on first access

for word in ["apple", "ant", "banana", "bear"]:
    char_groups[word[0]].append(word)   # {'a': ['apple','ant'], ...}


# ── 11. ORDERED DICT ─────────────────────────────────────────
from collections import OrderedDict

od = OrderedDict()
od["first"]  = 1
od["second"] = 2
od["third"]  = 3

od.move_to_end("first")         # move key to end
od.move_to_end("third", last=False)  # move key to front

# Note: regular dicts preserve insertion order since Python 3.7
# OrderedDict is useful when order-equality matters:
d1 = OrderedDict([("a", 1), ("b", 2)])
d2 = OrderedDict([("b", 2), ("a", 1)])
print(d1 == d2)     # False — order matters for OrderedDict


# ── 12. COUNTER ──────────────────────────────────────────────
from collections import Counter

c = Counter("mississippi")          # {'s':4,'i':4,'p':2,'m':1}
c2 = Counter(["apple", "banana", "apple", "cherry", "banana", "apple"])

print(c.most_common(2))             # [('s', 4), ('i', 4)]
print(c["s"])                       # 4
print(c["z"])                       # 0 — no KeyError

# arithmetic on Counters
a = Counter({"x": 3, "y": 2})
b = Counter({"x": 1, "y": 4})
print(a + b)    # Counter({'y':6,'x':4})
print(a - b)    # Counter({'x':2})  — drops zero/negative


# ── 13. NESTED DICTS ─────────────────────────────────────────
users = {
    "alice": {"age": 30, "scores": [95, 88]},
    "bob":   {"age": 25, "scores": [70, 82]},
}

print(users["alice"]["scores"][0])      # 95

# safe nested access
print(users.get("charlie", {}).get("age", "unknown"))   # unknown

# update nested value
users["alice"]["age"] = 31


# ── 14. COPYING — SHALLOW vs DEEP ───────────────────────────
import copy

original = {"a": [1, 2, 3], "b": 4}
shallow  = original.copy()         # inner list still shared
deep     = copy.deepcopy(original) # fully independent

shallow["a"].append(99)     # also changes original["a"]
deep["a"].append(99)        # does NOT affect original


# ── 15. DICT AS SWITCH / DISPATCH TABLE ─────────────────────
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b

ops = {"+": add, "-": sub, "*": mul}
print(ops["+"](3, 4))   # 7 — cleaner than if/elif chains


# ── 16. USEFUL BUILT-INS WITH DICTS ─────────────────────────
d = {"b": 2, "a": 1, "c": 3}

sorted_by_key = dict(sorted(d.items()))                     # {'a':1,'b':2,'c':3}
sorted_by_val = dict(sorted(d.items(), key=lambda x: x[1])) # {'a':1,'b':2,'c':3}
max_key       = max(d, key=d.get)                           # key with max value → 'c'
min_key       = min(d, key=d.get)                           # key with min value → 'a'


# ── 17. PERFORMANCE NOTES ────────────────────────────────────
# get / set / delete / in  → O(1) average
# Iteration               → O(n)
# copy()                  → O(n)
# Dicts use hash tables — keys must be HASHABLE
# valid keys:   str, int, float, tuple, frozenset
# invalid keys: list, dict, set  ← TypeError: unhashable type
