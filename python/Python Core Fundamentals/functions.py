# ─── Basic Function ──────────────────────────────────────────────────────────
def greet():
    print("Hello!")

greet()

# ─── Parameters & Return ─────────────────────────────────────────────────────
def add(a, b):
    return a + b

print(add(3, 4))            # 7

# ─── Default Arguments ───────────────────────────────────────────────────────
def greet_user(name, msg="Welcome"):
    print(f"{msg}, {name}!")

greet_user("Anurag")                # Welcome, Anurag!
greet_user("Anurag", "Hello")       # Hello, Anurag!

# ─── Keyword Arguments ───────────────────────────────────────────────────────
def profile(name, age, city):
    print(f"{name}, {age}, {city}")

profile(age=25, city="Delhi", name="Anurag")

# ─── *args (variable positional) ─────────────────────────────────────────────
def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4))    # 10

# ─── **kwargs (variable keyword) ─────────────────────────────────────────────
def show_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_info(name="Anurag", age=25, city="Delhi")

# ─── Multiple Return Values ───────────────────────────────────────────────────
def min_max(nums):
    return min(nums), max(nums)

low, high = min_max([3, 1, 9, 2])
print(low, high)            # 1 9

# ─── Nested Function ─────────────────────────────────────────────────────────
def outer():
    def inner():
        print("inner function")
    inner()

outer()

# ─── Recursive Function ──────────────────────────────────────────────────────
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))         # 120

# ─── Type Hints ──────────────────────────────────────────────────────────────
def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(3, 4))       # 12
