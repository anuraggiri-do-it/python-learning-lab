# ═══════════════════════════════════════════════════════════════
#         OOP — INHERITANCE
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS INHERITANCE?
# ─────────────────────────────────────────────────────────────
# Inheritance = a child class automatically gets all attributes
# and methods of its parent class.
#
# ANALOGY: Family traits 👨‍👩‍👧
#   Parent class = parent (has eyes, nose, DNA)
#   Child class  = child  (inherits traits + has own unique traits)
#   super()      = "call mom/dad's version of this"
#
# WHY USE IT?
#   DRY — write common code once in parent, reuse in all children
#   IS-A relationship — Dog IS-A Animal, Car IS-A Vehicle
#
# TYPES:
#   Single       → one parent
#   Multi-level  → grandparent → parent → child
#   Multiple     → two parents
#   Hierarchical → one parent, many children


# ═══════════════════════════════════════════════════════════════
# PART 1: SINGLE INHERITANCE
# ═══════════════════════════════════════════════════════════════

class Animal:
    def __init__(self, name, species):
        self.name    = name
        self.species = species
        self.alive   = True

    def breathe(self):
        print(f'{self.name} is breathing')

    def eat(self, food):
        print(f'{self.name} eats {food}')

    def describe(self):
        print(f'{self.name} ({self.species})')

    def __str__(self):
        return f'Animal({self.name}, {self.species})'


class Dog(Animal):                          # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name, 'Canis lupus familiaris')  # call parent __init__
        self.breed = breed
        self.tricks = []

    def bark(self):                         # Dog-specific method
        print(f'{self.name} says: Woof!')

    def learn_trick(self, trick):
        self.tricks.append(trick)
        print(f'{self.name} learned: {trick}')

    def describe(self):                     # OVERRIDE parent method
        super().describe()                  # call parent version first
        print(f'  Breed: {self.breed}, Tricks: {self.tricks}')


dog = Dog('Rex', 'Labrador')
dog.breathe()                               # inherited from Animal
dog.eat('bone')                             # inherited from Animal
dog.bark()                                  # Dog-specific
dog.learn_trick('sit')
dog.describe()                              # overridden — calls both

print(isinstance(dog, Dog))                 # True
print(isinstance(dog, Animal))              # True — Dog IS-A Animal
print(issubclass(Dog, Animal))              # True


# ═══════════════════════════════════════════════════════════════
# PART 2: MULTI-LEVEL INHERITANCE
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: Grandparent → Parent → Child 👴→👨→👦
# Each level adds more specific behaviour

class Vehicle:
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year

    def start(self):
        print(f'{self.make} {self.model} engine started')

    def stop(self):
        print(f'{self.make} {self.model} engine stopped')


class Car(Vehicle):                         # Car IS-A Vehicle
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def honk(self):
        print(f'{self.make} {self.model}: Beep beep!')


class ElectricCar(Car):                     # ElectricCar IS-A Car IS-A Vehicle
    def __init__(self, make, model, year, doors, battery_kwh):
        super().__init__(make, model, year, doors)
        self.battery_kwh = battery_kwh
        self.charge      = 100

    def charge_battery(self):
        self.charge = 100
        print(f'{self.make} {self.model} fully charged ({self.battery_kwh} kWh)')

    def start(self):                        # override Vehicle.start()
        print(f'{self.make} {self.model} silently starts (electric)')


tesla = ElectricCar('Tesla', 'Model 3', 2024, 4, 75)
tesla.start()                               # overridden
tesla.honk()                                # from Car
tesla.stop()                                # from Vehicle
tesla.charge_battery()                      # ElectricCar-specific

print(isinstance(tesla, ElectricCar))       # True
print(isinstance(tesla, Car))               # True
print(isinstance(tesla, Vehicle))           # True


# ═══════════════════════════════════════════════════════════════
# PART 3: MULTIPLE INHERITANCE
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: A child inheriting traits from BOTH parents 👨+👩→👧
# Python supports inheriting from multiple parent classes

class Flyable:
    def fly(self):
        print(f'{self.__class__.__name__} is flying')

    def land(self):
        print(f'{self.__class__.__name__} has landed')


class Swimmable:
    def swim(self):
        print(f'{self.__class__.__name__} is swimming')

    def dive(self):
        print(f'{self.__class__.__name__} is diving')


class Duck(Animal, Flyable, Swimmable):     # inherits from 3 classes
    def __init__(self, name):
        super().__init__(name, 'Anas platyrhynchos')

    def quack(self):
        print(f'{self.name} says: Quack!')


donald = Duck('Donald')
donald.breathe()                            # from Animal
donald.fly()                                # from Flyable
donald.swim()                               # from Swimmable
donald.quack()                              # Duck-specific


# ═══════════════════════════════════════════════════════════════
# PART 4: MRO — Method Resolution Order
# ═══════════════════════════════════════════════════════════════
#
# When multiple parents have the same method, Python uses MRO
# to decide which one to call.
# MRO follows C3 Linearization algorithm — left to right, depth first.
#
# ANALOGY: Queue at a help desk 🎫
#   Python checks each class in MRO order and uses the FIRST match found.

print(Duck.__mro__)
# (<class 'Duck'>, <class 'Animal'>, <class 'Flyable'>, <class 'Swimmable'>, ...)

print(Duck.mro())   # same as __mro__ but as a list

# Diamond problem — Python handles it with MRO
class A:
    def hello(self):
        print('Hello from A')

class B(A):
    def hello(self):
        print('Hello from B')

class C(A):
    def hello(self):
        print('Hello from C')

class D(B, C):      # inherits from both B and C
    pass

d = D()
d.hello()           # Hello from B  ← MRO: D → B → C → A
print(D.mro())      # [D, B, C, A, object]


# ═══════════════════════════════════════════════════════════════
# PART 5: super() IN DEPTH
# ═══════════════════════════════════════════════════════════════
#
# super() returns a proxy object that delegates method calls
# to the NEXT class in MRO — not necessarily the direct parent.

class Base:
    def __init__(self):
        print('Base.__init__')

class Left(Base):
    def __init__(self):
        print('Left.__init__')
        super().__init__()          # calls next in MRO

class Right(Base):
    def __init__(self):
        print('Right.__init__')
        super().__init__()          # calls next in MRO

class Child(Left, Right):
    def __init__(self):
        print('Child.__init__')
        super().__init__()          # follows MRO: Child→Left→Right→Base

print('\nMRO chain:')
Child()
# Child.__init__
# Left.__init__
# Right.__init__
# Base.__init__   ← called ONCE (not twice) — MRO prevents duplication


# ═══════════════════════════════════════════════════════════════
# PART 6: MIXIN PATTERN
# ═══════════════════════════════════════════════════════════════
#
# Mixin = a class that provides methods to be mixed into other classes
# Not meant to be instantiated alone — just adds functionality
#
# ANALOGY: Plugin 🔌
#   Mixin = a plugin you add to any class to give it extra powers

class LogMixin:
    """Adds logging capability to any class."""
    def log(self, message):
        print(f'[{self.__class__.__name__}] {message}')

class SerializeMixin:
    """Adds dict serialization to any class."""
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items()
                if not k.startswith('_')}

class User(LogMixin, SerializeMixin):
    def __init__(self, name, email):
        self.name  = name
        self.email = email

    def login(self):
        self.log(f'{self.name} logged in')  # from LogMixin

class Product(LogMixin, SerializeMixin):
    def __init__(self, name, price):
        self.name  = name
        self.price = price

    def sell(self):
        self.log(f'{self.name} sold for {self.price}')  # from LogMixin


user = User('Alice', 'alice@example.com')
user.login()
print(user.to_dict())                       # from SerializeMixin

product = Product('Laptop', 999)
product.sell()
print(product.to_dict())


# ═══════════════════════════════════════════════════════════════
# QUICK REFERENCE
# ═══════════════════════════════════════════════════════════════
#
#   class Child(Parent):          → single inheritance
#   class Child(P1, P2):          → multiple inheritance
#   super().__init__(...)         → call parent constructor
#   super().method()              → call parent method
#   isinstance(obj, Class)        → True if obj is instance of Class
#   issubclass(Child, Parent)     → True if Child inherits from Parent
#   Child.__mro__                 → method resolution order tuple
#   Child.mro()                   → method resolution order list
#
#   IS-A  → use inheritance   (Dog IS-A Animal)
#   HAS-A → use composition   (Car HAS-A Engine)
