# ─── List Comprehension ──────────────────────────────────────────────────────
# syntax: [expression for item in iterable if condition]

squares = [x ** 2 for x in range(1, 6)]
print(squares)                              # [1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)                                # [0, 2, 4, 6, 8]

upper = [s.upper() for s in ["hello", "world"]]
print(upper)                                # ['HELLO', 'WORLD']

# nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)                               # [[1,2,3],[2,4,6],[3,6,9]]

# flatten nested list
flat = [x for row in matrix for x in row]
print(flat)                                 # [1, 2, 3, 2, 4, 6, 3, 6, 9]

# with condition + expression
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)                               # ['even', 'odd', 'even', 'odd', 'even']

# ─── Dict Comprehension ──────────────────────────────────────────────────────
# syntax: {key: value for item in iterable if condition}

squares_dict = {x: x ** 2 for x in range(1, 6)}
print(squares_dict)                         # {1:1, 2:4, 3:9, 4:16, 5:25}

# swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)                              # {1:'a', 2:'b', 3:'c'}

# filter dict
scores = {"Anurag": 85, "Zara": 92, "Mia": 45}
passed = {k: v for k, v in scores.items() if v >= 50}
print(passed)                               # {'Anurag': 85, 'Zara': 92}

# from two lists
keys = ["name", "age", "city"]
values = ["Anurag", 25, "Delhi"]
profile = {k: v for k, v in zip(keys, values)}
print(profile)                              # {'name':'Anurag','age':25,'city':'Delhi'}

# ─── Set Comprehension ───────────────────────────────────────────────────────
# syntax: {expression for item in iterable if condition}

unique_squares = {x ** 2 for x in [-2, -1, 0, 1, 2]}
print(unique_squares)                       # {0, 1, 4}  (no duplicates)

nums = [1, 2, 2, 3, 3, 4]
unique_evens = {x for x in nums if x % 2 == 0}
print(unique_evens)                         # {2, 4}

words = ["hello", "world", "hello", "python"]
unique_words = {w.lower() for w in words}
print(unique_words)                         # {'hello', 'world', 'python'}

# ─── Generator Expression (bonus — memory efficient) ─────────────────────────
# syntax: (expression for item in iterable)  — lazy evaluation
gen = (x ** 2 for x in range(5))
print(list(gen))                            # [0, 1, 4, 9, 16]
print(sum(x ** 2 for x in range(5)))        # 30
