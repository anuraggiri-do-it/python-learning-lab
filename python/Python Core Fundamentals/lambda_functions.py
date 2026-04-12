# ─── Basic Lambda ────────────────────────────────────────────────────────────
# syntax: lambda arguments: expression

square = lambda x: x ** 2
print(square(5))                        # 25

add = lambda a, b: a + b
print(add(3, 4))                        # 7

# ─── Lambda with Condition ───────────────────────────────────────────────────
even_odd = lambda x: "even" if x % 2 == 0 else "odd"
print(even_odd(4))                      # even
print(even_odd(7))                      # odd

# ─── Lambda with sorted() ────────────────────────────────────────────────────
names = ["Anurag", "Zara", "Mia", "Bob"]
print(sorted(names))                            # alphabetical
print(sorted(names, key=lambda x: len(x)))      # by length

students = [("Anurag", 85), ("Zara", 92), ("Mia", 78)]
print(sorted(students, key=lambda s: s[1]))     # by marks ascending
print(sorted(students, key=lambda s: s[1], reverse=True))  # descending

# ─── Lambda with map() ───────────────────────────────────────────────────────
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))
print(squares)                          # [1, 4, 9, 16, 25]

# ─── Lambda with filter() ────────────────────────────────────────────────────
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)                            # [2, 4]

# ─── Lambda with reduce() ────────────────────────────────────────────────────
from functools import reduce

product = reduce(lambda a, b: a * b, nums)
print(product)                          # 120

total = reduce(lambda a, b: a + b, nums)
print(total)                            # 15

# ─── Lambda in Dictionary ────────────────────────────────────────────────────
ops = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
}
print(ops["add"](10, 5))               # 15
print(ops["mul"](3, 4))               # 12
