# ─── Variables ───────────────────────────────────────────────────────────────
x = 10
name = "Anurag"
pi = 3.14
is_active = True

# Multiple assignment
a, b, c = 1, 2, 3

# Same value
x = y = z = 0

# ─── int ─────────────────────────────────────────────────────────────────────
age = 25
negative = -10
big = 1_000_000          # readable large number

print(type(age))         # <class 'int'>
print(abs(negative))     # 10
print(bin(age))          # 0b11001  (binary)
print(age ** 2)          # 625      (power)

# ─── float ───────────────────────────────────────────────────────────────────
price = 9.99
scientific = 1.5e3       # 1500.0

print(type(price))       # <class 'float'>
print(round(price, 1))   # 10.0
print(int(price))        # 9  (truncates)

# ─── str ─────────────────────────────────────────────────────────────────────
first = "Hello"
last = 'World'
multi = """This is
a multiline string"""

# f-string (most used)
greeting = f"Hi, {name}! You are {age} years old."

print(first + " " + last)       # Hello World
print(first.upper())            # HELLO
print(first.lower())            # hello
print(first.replace("H", "J")) # Jello
print(len(first))               # 5
print(first[0])                 # H      (indexing)
print(first[1:4])               # ell    (slicing)
print("ell" in first)           # True
print(greeting)

# ─── bool ────────────────────────────────────────────────────────────────────
t = True
f = False

print(type(t))           # <class 'bool'>
print(int(t))            # 1
print(int(f))            # 0
print(t and f)           # False
print(t or f)            # True
print(not t)             # False

# ─── Type Conversion ─────────────────────────────────────────────────────────
print(int("42"))         # 42
print(float("3.14"))     # 3.14
print(str(100))          # '100'
print(bool(0))           # False
print(bool("hi"))        # True

# ─── type() & isinstance() ───────────────────────────────────────────────────
print(type(age))                    # <class 'int'>
print(isinstance(age, int))         # True
print(isinstance(price, float))     # True
print(isinstance(name, str))        # True
