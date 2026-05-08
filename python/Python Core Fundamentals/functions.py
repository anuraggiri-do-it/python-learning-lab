# ═══════════════════════════════════════════════════════════════
#         FUNCTIONS — Reusable Blocks of Code
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS A FUNCTION?
# ─────────────────────────────────────────────────────────────
# A function = a named, reusable block of code.
# Define once → call many times → avoids repetition (DRY principle).
#
# ANALOGY: Coffee machine ☕
#   Function = coffee machine
#   Parameters = coffee type, sugar, milk (inputs)
#   Return value = the cup of coffee (output)
#   Calling the function = pressing the button
#   You don't care HOW it makes coffee — just give inputs, get output
#
# DRY = Don't Repeat Yourself
#   Without functions → copy-paste same code everywhere
#   With functions    → write once, call anywhere


# ═══════════════════════════════════════════════════════════════
# PART 1: BASICS
# ═══════════════════════════════════════════════════════════════

# define
def greet():
    print('Hello!')

# call
greet()                     # Hello!

# with parameters and return
def add(a, b):
    return a + b

print(add(3, 4))            # 7
result = add(10, 20)        # store return value
print(result)               # 30

# without return → returns None implicitly
def say_hi(name):
    print(f'Hi, {name}!')

val = say_hi('Alice')
print(val)                  # None


# ═══════════════════════════════════════════════════════════════
# PART 2: ARGUMENT TYPES
# ═══════════════════════════════════════════════════════════════
#
# Python has 4 types of arguments:
#   1. Positional   → matched by position
#   2. Keyword      → matched by name
#   3. Default      → has a fallback value
#   4. *args/**kwargs → variable number

# ── positional ───────────────────────────────────────────────
def profile(name, age, city):
    print(f'{name}, {age}, {city}')

profile('Alice', 30, 'Delhi')           # positional — order matters

# ── keyword ──────────────────────────────────────────────────
profile(age=30, city='Delhi', name='Alice')  # order doesn't matter

# ── default arguments ────────────────────────────────────────
# RULE: defaults must come AFTER non-defaults
def greet_user(name, msg='Welcome'):
    print(f'{msg}, {name}!')

greet_user('Alice')                     # Welcome, Alice!
greet_user('Alice', 'Hello')            # Hello, Alice!

# ⚠️ MUTABLE DEFAULT ARGUMENT BUG
# BAD — list is created ONCE and shared across all calls
def bad_append(item, lst=[]):
    lst.append(item)
    return lst

print(bad_append(1))    # [1]
print(bad_append(2))    # [1, 2]  ← BUG: list persists between calls!

# GOOD — use None as default, create fresh list inside
def good_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(good_append(1))   # [1]
print(good_append(2))   # [2]  ← correct

# ── *args — variable positional arguments ────────────────────
# ANALOGY: Bag that holds any number of items 🎒
# *args collects extra positional args into a TUPLE

def total(*nums):
    return sum(nums)

print(total(1, 2, 3))       # 6
print(total(1, 2, 3, 4, 5)) # 15

def first_and_rest(first, *rest):
    print(f'First: {first}')
    print(f'Rest: {rest}')

first_and_rest(1, 2, 3, 4)  # First: 1, Rest: (2, 3, 4)

# ── **kwargs — variable keyword arguments ────────────────────
# **kwargs collects extra keyword args into a DICT

def show_info(**details):
    for key, value in details.items():
        print(f'{key}: {value}')

show_info(name='Alice', age=30, city='Delhi')

# combining all argument types
# ORDER: positional → *args → keyword-only → **kwargs
def combined(a, b, *args, sep='-', **kwargs):
    print(a, b, args, sep, kwargs)

combined(1, 2, 3, 4, sep='|', x=10, y=20)
# 1 2 (3, 4) | {'x': 10, 'y': 20}

# ── unpacking into function calls ────────────────────────────
def add3(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add3(*nums))          # unpack list → positional args

info = {'a': 1, 'b': 2, 'c': 3}
print(add3(**info))         # unpack dict → keyword args


# ═══════════════════════════════════════════════════════════════
# PART 3: RETURN VALUES
# ═══════════════════════════════════════════════════════════════

# multiple return values (returns a tuple)
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 9, 2, 7])
print(lo, hi)               # 1 9

# early return
def divide(a, b):
    if b == 0:
        return None         # early exit
    return a / b

print(divide(10, 2))        # 5.0
print(divide(10, 0))        # None

# return dict for named results
def stats(nums):
    return {
        'mean':   sum(nums) / len(nums),
        'min':    min(nums),
        'max':    max(nums),
        'count':  len(nums),
    }

result = stats([1, 2, 3, 4, 5])
print(result['mean'])       # 3.0


# ═══════════════════════════════════════════════════════════════
# PART 4: SCOPE — LEGB RULE
# ═══════════════════════════════════════════════════════════════
#
# Python looks up names in this order:
#   L → Local    (inside current function)
#   E → Enclosing (outer function, for nested functions)
#   G → Global   (module level)
#   B → Built-in (Python built-ins: len, print, range...)
#
# ANALOGY: Finding a book 📚
#   Check your desk (local) → check your room (enclosing)
#   → check the house library (global) → check public library (built-in)

x = 'global'

def outer():
    x = 'enclosing'

    def inner():
        x = 'local'
        print(x)        # local

    inner()
    print(x)            # enclosing

outer()
print(x)                # global

# global keyword — modify global variable inside function
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)          # 2

# nonlocal keyword — modify enclosing variable
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter_fn = make_counter()
print(counter_fn())     # 1
print(counter_fn())     # 2
print(counter_fn())     # 3


# ═══════════════════════════════════════════════════════════════
# PART 5: NESTED FUNCTIONS & CLOSURES
# ═══════════════════════════════════════════════════════════════
#
# CLOSURE = inner function that remembers variables from
#           its enclosing scope even after outer function returns
#
# ANALOGY: Backpack 🎒
#   Inner function packs the outer variable into its backpack.
#   Even after outer function is gone, inner still has the backpack.

def multiplier(factor):
    def multiply(x):
        return x * factor   # 'factor' is captured from outer scope
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))        # 10
print(triple(5))        # 15
print(double(10))       # 20


# ═══════════════════════════════════════════════════════════════
# PART 6: DECORATORS
# ═══════════════════════════════════════════════════════════════
#
# A decorator = a function that wraps another function
#               to add behavior before/after it runs
#
# ANALOGY: Gift wrapping 🎁
#   Original function = the gift
#   Decorator         = the wrapping paper + bow
#   The gift is still inside — decorator just adds presentation

import time
import functools

# basic decorator
def timer(func):
    @functools.wraps(func)          # preserves original function's name/docs
    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        end    = time.time()
        print(f'{func.__name__} took {end - start:.4f}s')
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

print(slow_sum(1_000_000))

# decorator with arguments
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say(msg):
    print(msg)

say('Hello')            # prints Hello 3 times

# stacking decorators (applied bottom-up)
def bold(func):
    def wrapper(*args, **kwargs):
        return f'**{func(*args, **kwargs)}**'
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f'_{func(*args, **kwargs)}_'
    return wrapper

@bold
@italic
def text(s):
    return s

print(text('hello'))    # **_hello_**


# ═══════════════════════════════════════════════════════════════
# PART 7: RECURSION
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: Russian nesting dolls 🪆
#   Each doll opens to reveal a smaller doll.
#   Base case = the smallest doll (no more dolls inside).
#   Without base case → infinite recursion → RecursionError
#
# EVERY recursive function needs:
#   1. Base case  → stops recursion
#   2. Recursive case → calls itself with smaller input

def factorial(n):
    if n == 0:              # base case
        return 1
    return n * factorial(n - 1)  # recursive case

print(factorial(5))         # 120

def fibonacci(n):
    if n <= 1:              # base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(8)])  # [0,1,1,2,3,5,8,13]

# recursion vs iteration — factorial
def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Python default recursion limit = 1000
import sys
print(sys.getrecursionlimit())  # 1000
# sys.setrecursionlimit(5000)   # increase if needed


# ═══════════════════════════════════════════════════════════════
# PART 8: TYPE HINTS
# ═══════════════════════════════════════════════════════════════
#
# Type hints = optional annotations that document expected types.
# Python does NOT enforce them at runtime — they're for readability
# and tools like mypy, IDEs, and linters.

from typing import Optional, Union, List, Dict, Tuple

def multiply(a: int, b: int) -> int:
    return a * b

def greet_typed(name: str, times: int = 1) -> str:
    return (f'Hello, {name}! ' * times).strip()

def process(data: List[int]) -> Dict[str, float]:
    return {'mean': sum(data) / len(data), 'max': float(max(data))}

def find(items: List[str], target: str) -> Optional[int]:
    for i, item in enumerate(items):
        if item == target:
            return i
    return None                 # Optional[int] = int or None

def flexible(x: Union[int, str]) -> str:
    return str(x)

print(multiply(3, 4))           # 12
print(greet_typed('Alice', 2))  # Hello, Alice! Hello, Alice!
print(process([1, 2, 3, 4, 5])) # {'mean': 3.0, 'max': 5.0}
print(find(['a', 'b', 'c'], 'b'))  # 1
print(find(['a', 'b', 'c'], 'z'))  # None
