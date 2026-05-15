# ═══════════════════════════════════════════════════════════════
#         OOP — ENCAPSULATION
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS ENCAPSULATION?
# ─────────────────────────────────────────────────────────────
# Encapsulation = bundling data (attributes) + behaviour (methods)
# into one unit (class), AND controlling access to internal details.
#
# TWO IDEAS IN ONE:
#   1. Bundling   → data and methods live together in a class
#   2. Hiding     → internal state is protected from outside misuse
#
# ANALOGY: Capsule pill 💊
#   The medicine (data) is sealed inside the capsule (class).
#   You swallow the capsule — you don't touch the medicine directly.
#   The capsule controls HOW the medicine is released.
#
# ACCESS LEVELS IN PYTHON:
#   public    →  name       → accessible everywhere
#   protected →  _name      → convention: "internal use" hint
#   private   →  __name     → name-mangled: _ClassName__name


# ═══════════════════════════════════════════════════════════════
# PART 1: ACCESS MODIFIERS
# ═══════════════════════════════════════════════════════════════

class Employee:
    company = 'TechCorp'                    # public class variable

    def __init__(self, name, salary, ssn):
        self.name      = name               # public   — anyone can read/write
        self._salary   = salary             # protected — internal use hint
        self.__ssn     = ssn                # private  — name-mangled

    def get_details(self):                  # public method
        return f'{self.name} at {self.company}'

    def _calculate_tax(self):               # protected method — internal
        return self._salary * 0.2

    def __validate_ssn(self):               # private method
        return len(str(self.__ssn)) == 9

    def summary(self):
        tax   = self._calculate_tax()
        valid = self.__validate_ssn()
        return f'{self.name} | Tax: ${tax:.0f} | SSN valid: {valid}'


emp = Employee('Alice', 90000, 123456789)

print(emp.name)             # Alice        ← public, direct access OK
print(emp._salary)          # 90000        ← works but convention says don't
# print(emp.__ssn)          # AttributeError ← private, blocked

# name mangling — Python renames __ssn to _Employee__ssn
print(emp._Employee__ssn)   # 123456789    ← accessible but strongly discouraged
print(emp.summary())


# ═══════════════════════════════════════════════════════════════
# PART 2: @property — CONTROLLED ATTRIBUTE ACCESS
# ═══════════════════════════════════════════════════════════════
#
# @property = getter that looks like an attribute
# @x.setter = setter with validation
# @x.deleter = called on del obj.x
#
# ANALOGY: Smart lock 🔐
#   You can read the lock status (getter)
#   You can set a new code only if it meets rules (setter)
#   You can't bypass the rules by accessing internals directly

class BankAccount:
    def __init__(self, owner, balance=0):
        self._owner   = owner
        self.__balance = balance
        self.__transactions = []

    @property
    def owner(self):                        # read-only property (no setter)
        return self._owner

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):              # validated setter
        if not isinstance(amount, (int, float)):
            raise TypeError('Balance must be a number')
        if amount < 0:
            raise ValueError('Balance cannot be negative')
        self.__balance = amount

    @property
    def transaction_count(self):            # computed property
        return len(self.__transactions)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit must be positive')
        self.__balance += amount
        self.__transactions.append(('deposit', amount))
        print(f'Deposited ${amount:.2f} | Balance: ${self.__balance:.2f}')

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be positive')
        if amount > self.__balance:
            raise ValueError('Insufficient funds')
        self.__balance -= amount
        self.__transactions.append(('withdraw', amount))
        print(f'Withdrew ${amount:.2f} | Balance: ${self.__balance:.2f}')

    def __str__(self):
        return f'BankAccount({self._owner}, ${self.__balance:.2f})'


acc = BankAccount('Alice', 1000)
acc.deposit(500)
acc.withdraw(200)

print(acc.balance)              # 1300.0   ← getter
print(acc.owner)                # Alice    ← read-only
print(acc.transaction_count)    # 2        ← computed

try:
    acc.balance = -500          # raises ValueError
except ValueError as e:
    print(e)

# acc.owner = 'Bob'             # AttributeError — no setter defined


# ═══════════════════════════════════════════════════════════════
# PART 3: ENCAPSULATION IN INHERITANCE
# ═══════════════════════════════════════════════════════════════
#
# protected (_name) → accessible in child classes (by convention)
# private (__name)  → NOT accessible in child classes (name-mangled)

class Animal:
    def __init__(self, name, health):
        self.name      = name               # public
        self._health   = health             # protected — child can use
        self.__dna     = 'ATCG...'          # private — child cannot use

    def _heal(self, amount):                # protected method
        self._health = min(100, self._health + amount)

    def status(self):
        return f'{self.name}: health={self._health}'


class Dog(Animal):
    def __init__(self, name, health, breed):
        super().__init__(name, health)
        self.breed = breed

    def eat(self, food):
        print(f'{self.name} eats {food}')
        self._heal(10)                      # can access protected method ✅
        # self.__dna                        # AttributeError — private blocked ❌

    def status(self):
        return f'{super().status()} | breed={self.breed}'


dog = Dog('Rex', 70, 'Labrador')
dog.eat('bone')
print(dog.status())             # Rex: health=80 | breed=Labrador
print(dog._health)              # 80  ← accessible (protected)


# ═══════════════════════════════════════════════════════════════
# PART 4: REAL-WORLD EXAMPLE — User Account
# ═══════════════════════════════════════════════════════════════

import hashlib

class UserAccount:
    _active_users = 0

    def __init__(self, username, email, password):
        self.username   = username
        self._email     = email
        self.__password = self.__hash(password)  # never store plain text
        self.__locked   = False
        self.__attempts = 0
        UserAccount._active_users += 1

    @staticmethod
    def __hash(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value or '.' not in value:
            raise ValueError('Invalid email address')
        self._email = value

    @property
    def is_locked(self):
        return self.__locked

    def login(self, password):
        if self.__locked:
            print('Account locked. Contact support.')
            return False
        if self.__hash(password) == self.__password:
            self.__attempts = 0
            print(f'Welcome, {self.username}!')
            return True
        self.__attempts += 1
        if self.__attempts >= 3:
            self.__locked = True
            print('Too many failed attempts. Account locked.')
        else:
            print(f'Wrong password. {3 - self.__attempts} attempt(s) left.')
        return False

    def change_password(self, old_pw, new_pw):
        if self.__hash(old_pw) != self.__password:
            raise ValueError('Current password is incorrect')
        if len(new_pw) < 8:
            raise ValueError('New password must be at least 8 characters')
        self.__password = self.__hash(new_pw)
        print('Password changed successfully')

    @classmethod
    def get_active_users(cls):
        return cls._active_users

    def __str__(self):
        status = 'locked' if self.__locked else 'active'
        return f'User({self.username}, {self._email}, {status})'


user = UserAccount('alice', 'alice@example.com', 'secret123')
user.login('wrongpass')
user.login('wrongpass')
user.login('wrongpass')         # locks account
user.login('secret123')         # locked — can't login

user2 = UserAccount('bob', 'bob@example.com', 'pass1234')
user2.login('pass1234')
user2.change_password('pass1234', 'newpass99')

print(UserAccount.get_active_users())   # 2
print(user)
print(user2)


# ═══════════════════════════════════════════════════════════════
# PART 5: ENCAPSULATION vs ABSTRACTION
# ═══════════════════════════════════════════════════════════════
#
#   Encapsulation = HIDING DATA
#     → private/protected attributes
#     → @property for controlled access
#     → prevents direct manipulation of internal state
#
#   Abstraction = HIDING IMPLEMENTATION
#     → abstract methods (ABC)
#     → shows WHAT to do, hides HOW it's done
#     → user calls login() without knowing the hashing logic
#
#   They work TOGETHER:
#     Abstraction  → defines the interface (what methods exist)
#     Encapsulation → protects the data behind that interface


# ═══════════════════════════════════════════════════════════════
# QUICK REFERENCE
# ═══════════════════════════════════════════════════════════════
#
#   self.name      → public    — accessible anywhere
#   self._name     → protected — convention: internal/subclass only
#   self.__name    → private   — name-mangled to _ClassName__name
#
#   @property      → getter (read as attribute)
#   @x.setter      → setter with validation
#   @x.deleter     → called on del obj.x
#
#   Name mangling:
#     self.__x inside class Foo → stored as _Foo__x
#     obj._Foo__x               → still accessible (but don't!)
