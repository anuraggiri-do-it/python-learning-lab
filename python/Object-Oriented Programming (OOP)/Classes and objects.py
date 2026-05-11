# ═══════════════════════════════════════════════════════════════
#         OOP — CLASSES & OBJECTS
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS A CLASS?
# ─────────────────────────────────────────────────────────────
# A class = a blueprint / template for creating objects.
# An object = a specific instance created from that blueprint.
#
# ANALOGY: Cookie cutter vs cookies 🍪
#   Class  = the cookie cutter (shape, design — defined once)
#   Object = each cookie made from it (real, exists in memory)
#   You can make 1000 cookies from one cutter — each is independent.
#
# FOUR PILLARS OF OOP:
#   Encapsulation  → bundle data + methods, hide internals
#   Inheritance    → child class reuses parent class
#   Polymorphism   → same method name, different behaviour
#   Abstraction    → hide complexity, show only interface


# ═══════════════════════════════════════════════════════════════
# PART 1: BASIC CLASS & OBJECT
# ═══════════════════════════════════════════════════════════════

class Dog:
    # __init__ = constructor — called automatically when object is created
    # self     = reference to the current object (like 'this' in Java/JS)
    def __init__(self, name, breed, age):
        self.name  = name       # instance attribute — unique per object
        self.breed = breed
        self.age   = age

    def bark(self):
        print(f'{self.name} says: Woof!')

    def describe(self):
        print(f'{self.name} | {self.breed} | {self.age} years old')

    def birthday(self):
        self.age += 1
        print(f'Happy birthday {self.name}! Now {self.age} years old.')


# creating objects (instances)
dog1 = Dog('Rex',   'Labrador', 3)
dog2 = Dog('Bella', 'Poodle',   5)
dog3 = Dog('Max',   'Husky',    2)

dog1.bark()
dog2.describe()
dog3.birthday()

# each object has its OWN copy of attributes
dog1.name = 'Rex Jr.'       # only changes dog1, not dog2 or dog3
print(dog1.name)            # Rex Jr.
print(dog2.name)            # Bella  ← unchanged


# ═══════════════════════════════════════════════════════════════
# PART 2: CLASS VARIABLES vs INSTANCE VARIABLES
# ═══════════════════════════════════════════════════════════════
#
# Instance variable → belongs to ONE object  (self.x)
# Class variable    → shared by ALL objects  (ClassName.x)
#
# ANALOGY: School 🏫
#   Class variable    = school name (same for all students)
#   Instance variable = student name (unique per student)

class Student:
    school    = 'Python Academy'    # class variable — shared by ALL
    _count    = 0                   # class variable — tracks total students

    def __init__(self, name, grade):
        self.name  = name           # instance variable — unique per student
        self.grade = grade
        Student._count += 1         # increment shared counter

    def study(self, subject):
        print(f'{self.name} is studying {subject} at {Student.school}')

    @classmethod
    def get_count(cls):
        return cls._count

    def __str__(self):
        return f'{self.name} (Grade {self.grade}) — {Student.school}'


s1 = Student('Alice', 10)
s2 = Student('Bob',   11)
s3 = Student('Carol', 10)

print(s1.school)                    # Python Academy  ← class variable
print(Student.school)               # Python Academy  ← same value
print(Student.get_count())          # 3

# changing class variable affects ALL instances
Student.school = 'Advanced Python Academy'
print(s1.school)                    # Advanced Python Academy
print(s2.school)                    # Advanced Python Academy

# but if you set it on an instance, it creates an INSTANCE variable
s1.school = 'Special School'        # creates instance variable for s1 only
print(s1.school)                    # Special School  ← instance variable
print(s2.school)                    # Advanced Python Academy  ← class variable


# ═══════════════════════════════════════════════════════════════
# PART 3: METHODS — THREE TYPES
# ═══════════════════════════════════════════════════════════════
#
#   Instance method  → works on one object    (self)
#   Class method     → works on the class     (@classmethod, cls)
#   Static method    → utility, no state      (@staticmethod)

class BankAccount:
    _interest_rate = 0.05           # class variable

    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = balance
        self._transactions = []

    # ── instance method ──────────────────────────────────────
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit must be positive')
        self.balance += amount
        self._transactions.append(('deposit', amount))
        print(f'{self.owner}: deposited ${amount:.2f}. Balance: ${self.balance:.2f}')

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount
        self._transactions.append(('withdraw', amount))
        print(f'{self.owner}: withdrew ${amount:.2f}. Balance: ${self.balance:.2f}')

    def apply_interest(self):
        interest = self.balance * BankAccount._interest_rate
        self.deposit(interest)

    def statement(self):
        print(f'\n--- Statement for {self.owner} ---')
        for txn_type, amount in self._transactions:
            print(f'  {txn_type:>10}: ${amount:.2f}')
        print(f'  {"Balance":>10}: ${self.balance:.2f}')

    # ── class method ─────────────────────────────────────────
    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate

    @classmethod
    def set_interest_rate(cls, rate):
        if not 0 < rate < 1:
            raise ValueError('Rate must be between 0 and 1')
        cls._interest_rate = rate
        print(f'Interest rate updated to {rate:.1%}')

    @classmethod
    def from_dict(cls, data):           # alternative constructor
        return cls(data['owner'], data.get('balance', 0))

    # ── static method ────────────────────────────────────────
    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

    @staticmethod
    def currency_format(amount):
        return f'${amount:,.2f}'

    def __str__(self):
        return f'BankAccount({self.owner}, {self.currency_format(self.balance)})'

    def __repr__(self):
        return f'BankAccount({self.owner!r}, {self.balance})'


acc1 = BankAccount('Alice', 1000)
acc2 = BankAccount.from_dict({'owner': 'Bob', 'balance': 500})

acc1.deposit(200)
acc1.withdraw(150)
acc1.apply_interest()
acc1.statement()

print(BankAccount.get_interest_rate())      # 0.05
BankAccount.set_interest_rate(0.07)
print(BankAccount.validate_amount(100))     # True
print(BankAccount.currency_format(9999.5))  # $9,999.50


# ═══════════════════════════════════════════════════════════════
# PART 4: PROPERTIES — CONTROLLED ATTRIBUTE ACCESS
# ═══════════════════════════════════════════════════════════════
#
# @property turns a method into an attribute-style access.
# Lets you add validation/logic without changing the interface.
#
# ANALOGY: Smart thermostat 🌡️
#   You set a temperature — it validates and adjusts internally.
#   You read temperature — it returns the current value.
#   You never touch the internal sensor directly.

class Circle:
    def __init__(self, radius):
        self._radius = radius       # store in private var

    @property
    def radius(self):               # getter — read as attribute
        return self._radius

    @radius.setter
    def radius(self, value):        # setter — validate on write
        if value < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = value

    @radius.deleter
    def radius(self):               # deleter — called on del obj.radius
        print('Deleting radius')
        del self._radius

    @property
    def diameter(self):             # computed property — no setter needed
        return self._radius * 2

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

    def __str__(self):
        return f'Circle(r={self._radius}, area={self.area:.2f})'


c = Circle(5)
print(c.radius)         # 5        ← looks like attribute, calls getter
c.radius = 10           # calls setter with validation
print(c.diameter)       # 20       ← computed property
print(c.area)           # 314.159
print(c)

try:
    c.radius = -1       # raises ValueError
except ValueError as e:
    print(e)


# ═══════════════════════════════════════════════════════════════
# PART 5: DATACLASSES — LESS BOILERPLATE
# ═══════════════════════════════════════════════════════════════
#
# @dataclass auto-generates __init__, __repr__, __eq__ for you.
# Use when your class is mainly a data container.

from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0                  # default value

    def distance_to_origin(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5


@dataclass
class Inventory:
    name:     str
    quantity: int     = 0
    price:    float   = 0.0
    tags:     list    = field(default_factory=list)  # mutable default

    @property
    def total_value(self):
        return self.quantity * self.price


p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0)
p3 = Point(3.0, 4.0)

print(p1)               # Point(x=1.0, y=2.0, z=0.0)  ← auto __repr__
print(p1 == p2)         # True   ← auto __eq__
print(p1 == p3)         # False
print(p3.distance_to_origin())  # 5.0

item = Inventory('Laptop', 10, 999.99, ['electronics', 'sale'])
print(item)
print(item.total_value) # 9999.9


# ═══════════════════════════════════════════════════════════════
# PART 6: __dict__ & INTROSPECTION
# ═══════════════════════════════════════════════════════════════
#
# Python stores instance attributes in a __dict__ dictionary.
# Useful for debugging and serialization.

class Config:
    def __init__(self, host, port, debug=False):
        self.host  = host
        self.port  = port
        self.debug = debug


cfg = Config('localhost', 8080, True)

print(cfg.__dict__)                 # {'host': 'localhost', 'port': 8080, 'debug': True}
print(Config.__dict__.keys())       # class-level attributes and methods

# introspection
print(hasattr(cfg, 'host'))         # True
print(getattr(cfg, 'port'))         # 8080
setattr(cfg, 'port', 9090)         # same as cfg.port = 9090
print(cfg.port)                     # 9090
delattr(cfg, 'debug')               # same as del cfg.debug
print(hasattr(cfg, 'debug'))        # False

# dir() — all attributes and methods
print([x for x in dir(cfg) if not x.startswith('_')])


# ═══════════════════════════════════════════════════════════════
# QUICK REFERENCE
# ═══════════════════════════════════════════════════════════════
#
#   class MyClass:              → define class
#   def __init__(self, ...):    → constructor
#   self.x = x                  → instance variable
#   MyClass.x = x               → class variable
#   obj = MyClass(...)          → create object
#   obj.method()                → call instance method
#   MyClass.method()            → call class/static method
#   @property                   → getter
#   @x.setter                   → setter with validation
#   @classmethod                → receives cls
#   @staticmethod               → no self or cls
#   @dataclass                  → auto __init__, __repr__, __eq__
#   obj.__dict__                → instance attributes as dict
#   hasattr / getattr / setattr → dynamic attribute access
