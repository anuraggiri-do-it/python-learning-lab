# ═══════════════════════════════════════════════════════════════
#         OOP — POLYMORPHISM
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS POLYMORPHISM?
# ─────────────────────────────────────────────────────────────
# Poly = many, Morph = forms
# Same interface → different behaviour depending on the object.
#
# ANALOGY: Remote control 📺
#   One remote (same interface: volume+, volume-, channel+)
#   Works on Samsung TV, LG TV, Sony TV — each responds differently
#   You don't need a different remote for each brand.
#
# THREE FORMS IN PYTHON:
#   1. Method Overriding  → child redefines parent's method
#   2. Duck Typing        → "if it has the method, it works"
#   3. Operator Overloading → redefine what +, -, ==, < do


# ═══════════════════════════════════════════════════════════════
# PART 1: METHOD OVERRIDING
# ═══════════════════════════════════════════════════════════════
#
# Child class provides its own version of a parent method.
# Same method name → different behaviour per class.

class Shape:
    def __init__(self, color='black'):
        self.color = color

    def area(self):
        raise NotImplementedError('Subclass must implement area()')

    def perimeter(self):
        raise NotImplementedError('Subclass must implement perimeter()')

    def describe(self):
        print(f'{self.__class__.__name__} | color={self.color} | '
              f'area={self.area():.2f} | perimeter={self.perimeter():.2f}')


class Circle(Shape):
    def __init__(self, radius, color='black'):
        super().__init__(color)
        self.radius = radius

    def area(self):                         # OVERRIDES Shape.area()
        return 3.14159 * self.radius ** 2

    def perimeter(self):                    # OVERRIDES Shape.perimeter()
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height, color='black'):
        super().__init__(color)
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c, color='black'):
        super().__init__(color)
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = (self.a + self.b + self.c) / 2  # Heron's formula
        return (s * (s-self.a) * (s-self.b) * (s-self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


# polymorphism in action — same function, any shape
def print_shape_info(shape):
    shape.describe()                        # calls the RIGHT describe/area/perimeter

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for shape in shapes:
    print_shape_info(shape)                 # same call → different output

# total area of all shapes — works regardless of type
total_area = sum(s.area() for s in shapes)
print(f'Total area: {total_area:.2f}')


# ═══════════════════════════════════════════════════════════════
# PART 2: DUCK TYPING
# ═══════════════════════════════════════════════════════════════
#
# "If it walks like a duck and quacks like a duck, it's a duck."
# Python doesn't check TYPE — only checks if the METHOD exists.
# No inheritance required — just have the right method.
#
# ANALOGY: USB port 🔌
#   Any device with a USB plug works — phone, keyboard, mouse.
#   The port doesn't care what brand it is — just needs the right shape.

class Dog:
    def speak(self):
        return 'Woof!'

class Cat:
    def speak(self):
        return 'Meow!'

class Robot:                                # not an Animal at all!
    def speak(self):
        return 'Beep boop!'

class Person:
    def speak(self):
        return 'Hello!'

# works on ANY object that has speak() — no inheritance needed
def make_noise(entity):
    print(f'{entity.__class__.__name__}: {entity.speak()}')

for obj in [Dog(), Cat(), Robot(), Person()]:
    make_noise(obj)                         # all work — duck typing

# Python built-ins use duck typing too
# len() works on list, str, dict, tuple, set — anything with __len__
print(len([1, 2, 3]))       # list
print(len('hello'))         # str
print(len({'a': 1}))        # dict


# ═══════════════════════════════════════════════════════════════
# PART 3: OPERATOR OVERLOADING
# ═══════════════════════════════════════════════════════════════
#
# Redefine what built-in operators do for your custom class.
# ANALOGY: Currency exchange 💱
#   + means "add money" for a Money class
#   == means "same amount and currency"
#   < means "less value"

class Vector:
    """2D vector with overloaded operators."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __add__(self, other):               # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):               # v1 - v2
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):              # v * 3
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):             # 3 * v  (reversed)
        return self.__mul__(scalar)

    def __truediv__(self, scalar):          # v / 2
        return Vector(self.x / scalar, self.y / scalar)

    def __eq__(self, other):                # v1 == v2
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):                # v1 < v2  (by magnitude)
        return self.magnitude() < other.magnitude()

    def __len__(self):                      # len(v) → int magnitude
        return int(self.magnitude())

    def __neg__(self):                      # -v
        return Vector(-self.x, -self.y)

    def __abs__(self):                      # abs(v) → magnitude
        return self.magnitude()

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def dot(self, other):                   # dot product
        return self.x * other.x + self.y * other.y


v1 = Vector(2, 3)
v2 = Vector(1, 4)

print(v1 + v2)          # Vector(3, 7)
print(v1 - v2)          # Vector(1, -1)
print(v1 * 3)           # Vector(6, 9)
print(3 * v1)           # Vector(6, 9)  ← __rmul__
print(v1 / 2)           # Vector(1.0, 1.5)
print(v1 == v2)         # False
print(v1 == Vector(2,3))# True
print(-v1)              # Vector(-2, -3)
print(abs(v1))          # 3.605...
print(v1 < v2)          # compare magnitudes


# ═══════════════════════════════════════════════════════════════
# PART 4: POLYMORPHISM WITH ABSTRACT BASE CLASSES
# ═══════════════════════════════════════════════════════════════
#
# Use ABC to ENFORCE that all subclasses implement required methods.
# Guarantees the polymorphic interface exists on every subclass.

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def receipt(self, amount):              # concrete — shared by all
        print(f'Receipt: {self.__class__.__name__} payment of ${amount:.2f}')


class CreditCard(Payment):
    def __init__(self, card_number):
        self.card_number = f'****{card_number[-4:]}'

    def pay(self, amount):
        print(f'Charged ${amount:.2f} to card {self.card_number}')

    def refund(self, amount):
        print(f'Refunded ${amount:.2f} to card {self.card_number}')


class PayPal(Payment):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f'PayPal: ${amount:.2f} sent from {self.email}')

    def refund(self, amount):
        print(f'PayPal: ${amount:.2f} refunded to {self.email}')


class Crypto(Payment):
    def __init__(self, wallet):
        self.wallet = wallet

    def pay(self, amount):
        print(f'Crypto: {amount} BTC sent from wallet {self.wallet[:8]}...')

    def refund(self, amount):
        print(f'Crypto: {amount} BTC refunded to wallet {self.wallet[:8]}...')


# process any payment type — fully polymorphic
def checkout(payment_method, amount):
    payment_method.pay(amount)
    payment_method.receipt(amount)

payments = [
    CreditCard('1234567890123456'),
    PayPal('alice@example.com'),
    Crypto('0xABCDEF1234567890'),
]

for method in payments:
    checkout(method, 99.99)
    print()


# ═══════════════════════════════════════════════════════════════
# PART 5: BUILT-IN POLYMORPHISM
# ═══════════════════════════════════════════════════════════════
#
# Python's built-in functions are polymorphic by design

# len() — works on any object with __len__
print(len([1, 2, 3]))           # 3
print(len('hello'))             # 5
print(len({'a': 1, 'b': 2}))   # 2

# str() — calls __str__ on any object
print(str(42))                  # '42'
print(str(3.14))                # '3.14'
print(str(v1))                  # 'Vector(2, 3)'

# + operator — different behaviour per type
print(1 + 2)                    # 3       (int addition)
print('a' + 'b')                # 'ab'    (string concat)
print([1] + [2])                # [1, 2]  (list concat)
print(v1 + v2)                  # Vector  (custom __add__)

# sorted() — works on any iterable with comparable elements
print(sorted([3, 1, 2]))
print(sorted('hello'))
print(sorted([v1, v2], key=lambda v: v.magnitude()))


# ═══════════════════════════════════════════════════════════════
# QUICK REFERENCE
# ═══════════════════════════════════════════════════════════════
#
#   Method Overriding  → child redefines parent method
#   Duck Typing        → any object with the right method works
#   Operator Overload  → __add__, __eq__, __lt__, __str__, __len__
#
#   DUNDER OPERATORS:
#     __add__    → +       __sub__    → -
#     __mul__    → *       __truediv__→ /
#     __eq__     → ==      __ne__     → !=
#     __lt__     → <       __gt__     → >
#     __le__     → <=      __ge__     → >=
#     __neg__    → -x      __abs__    → abs(x)
#     __len__    → len(x)  __str__    → str(x)
#     __repr__   → repr(x) __bool__   → bool(x)
