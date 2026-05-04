# ═══════════════════════════════════════════════════════════════
#         ERROR HANDLING & DEBUGGING — Exceptions
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS AN EXCEPTION?
# ─────────────────────────────────────────────────────────────
# An exception = an event that disrupts normal program flow.
# Python raises an exception object when something goes wrong.
# If not caught → program crashes with a traceback.
#
# ANALOGY: Seatbelt in a car 🚗
#   Normal code = driving normally
#   Exception    = crash happens
#   try/except   = seatbelt — catches the crash, lets you recover
#   finally      = airbag — deploys no matter what (cleanup)


# ─────────────────────────────────────────────────────────────
# PART 1: BASIC try / except / else / finally
# ─────────────────────────────────────────────────────────────
#
# try     → code that might raise an exception
# except  → handle the exception
# else    → runs ONLY if no exception occurred
# finally → ALWAYS runs (cleanup: close files, DB connections)

try:
    x      = int(input('Enter a number: '))
    result = 10 / x
except ValueError:
    print('Invalid input — not a number')
except ZeroDivisionError:
    print('Cannot divide by zero')
except Exception as e:
    print(f'Unexpected error: {type(e).__name__}: {e}')
else:
    print(f'Result: {result}')            # only runs if no exception
finally:
    print('Always runs — cleanup here')   # runs regardless


# ─────────────────────────────────────────────────────────────
# PART 2: BUILT-IN EXCEPTION HIERARCHY
# ─────────────────────────────────────────────────────────────
#
# BaseException
# └── Exception
#     ├── ArithmeticError
#     │   ├── ZeroDivisionError
#     │   └── OverflowError
#     ├── LookupError
#     │   ├── IndexError
#     │   └── KeyError
#     ├── TypeError
#     ├── ValueError
#     ├── AttributeError
#     ├── NameError
#     ├── FileNotFoundError  (subclass of OSError)
#     ├── ImportError
#     ├── StopIteration
#     └── RuntimeError

# catching multiple exceptions in one line
try:
    data = [1, 2, 3]
    print(data[10])
except (IndexError, KeyError) as e:
    print(f'Lookup error: {e}')

# catching by parent class (catches all subclasses)
try:
    result = 1 / 0
except ArithmeticError as e:
    print(f'Math error: {e}')             # catches ZeroDivisionError too


# ─────────────────────────────────────────────────────────────
# PART 3: RAISING EXCEPTIONS
# ─────────────────────────────────────────────────────────────

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError(f'Age must be int, got {type(age).__name__}')
    if age < 0:
        raise ValueError(f'Age cannot be negative: {age}')
    if age > 150:
        raise ValueError(f'Age unrealistically large: {age}')
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(e)

# re-raise — catch, log, then re-raise for caller to handle
def process():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        print('Logging error...')
        raise                             # re-raises the same exception

try:
    process()
except ZeroDivisionError:
    print('Caught re-raised exception')

# raise from — chain exceptions (preserve original cause)
try:
    try:
        int('abc')
    except ValueError as original:
        raise RuntimeError('Config parsing failed') from original
except RuntimeError as e:
    print(e)
    print(f'Caused by: {e.__cause__}')


# ─────────────────────────────────────────────────────────────
# PART 4: CUSTOM EXCEPTIONS
# ─────────────────────────────────────────────────────────────
#
# ANALOGY: Custom alarm system 🚨
#   Built-in exceptions = generic fire alarm
#   Custom exceptions   = specific alarms (smoke, CO2, intruder)
#   More specific → easier to catch exactly what you need

class AppError(Exception):
    """Base exception for this application."""
    pass

class ValidationError(AppError):
    """Raised when input validation fails."""
    def __init__(self, field, message):
        self.field   = field
        self.message = message
        super().__init__(f'[{field}] {message}')

class DatabaseError(AppError):
    """Raised when a database operation fails."""
    def __init__(self, query, reason):
        self.query  = query
        self.reason = reason
        super().__init__(f'DB error on "{query}": {reason}')

class NotFoundError(AppError):
    """Raised when a resource is not found."""
    def __init__(self, resource, identifier):
        super().__init__(f'{resource} with id={identifier} not found')


# using custom exceptions
def create_user(name, age):
    if not name:
        raise ValidationError('name', 'cannot be empty')
    if not isinstance(age, int) or age < 0:
        raise ValidationError('age', 'must be a non-negative integer')
    return {'name': name, 'age': age}

try:
    user = create_user('', 25)
except ValidationError as e:
    print(f'Validation failed on field "{e.field}": {e.message}')
except AppError as e:
    print(f'App error: {e}')


# ─────────────────────────────────────────────────────────────
# PART 5: CONTEXT MANAGERS & EXCEPTION SAFETY
# ─────────────────────────────────────────────────────────────
#
# with statement = guaranteed cleanup even if exception occurs
# ANALOGY: Automatic door 🚪 — opens when you enter, closes when you leave
#          even if you trip and fall inside

# file — always closed even if exception inside
try:
    with open('nonexistent.txt') as f:
        data = f.read()
except FileNotFoundError as e:
    print(f'File not found: {e.filename}')

# contextlib.suppress — silently ignore specific exceptions
from contextlib import suppress

with suppress(FileNotFoundError):
    open('nonexistent.txt')              # no crash, no noise
print('Continued after suppressed error')

# contextlib.contextmanager — create custom context manager
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f'Acquiring {name}')
    try:
        yield name                        # code inside `with` runs here
    except Exception as e:
        print(f'Error while using {name}: {e}')
        raise
    finally:
        print(f'Releasing {name}')        # always runs

with managed_resource('database connection') as res:
    print(f'Using {res}')


# ─────────────────────────────────────────────────────────────
# PART 6: EXCEPTION GROUPS (Python 3.11+)
# ─────────────────────────────────────────────────────────────
# Handle multiple exceptions raised simultaneously (async tasks)

# try:
#     raise ExceptionGroup('multiple errors', [
#         ValueError('bad value'),
#         TypeError('bad type'),
#     ])
# except* ValueError as eg:
#     print(f'ValueError(s): {eg.exceptions}')
# except* TypeError as eg:
#     print(f'TypeError(s): {eg.exceptions}')


# ─────────────────────────────────────────────────────────────
# PART 7: DEBUGGING TECHNIQUES
# ─────────────────────────────────────────────────────────────

import traceback
import logging

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s | %(levelname)s | %(message)s')

# traceback — get full stack trace as string
def risky():
    return 1 / 0

try:
    risky()
except ZeroDivisionError:
    tb = traceback.format_exc()          # full traceback as string
    logging.error('Division failed:\n%s', tb)

# assert — lightweight checks during development
def divide(a, b):
    assert b != 0, 'Denominator must not be zero'
    return a / b

# NOTE: assertions are disabled with python -O (optimized mode)
# Use raise for production validation, assert for dev-time checks

# warnings — non-fatal issues
import warnings

def old_function():
    warnings.warn('old_function is deprecated, use new_function()',
                  DeprecationWarning, stacklevel=2)
    return 42

with warnings.catch_warnings():
    warnings.simplefilter('ignore', DeprecationWarning)
    old_function()                        # suppressed


# ─────────────────────────────────────────────────────────────
# PART 8: BEST PRACTICES
# ─────────────────────────────────────────────────────────────
#
# ✅ Catch specific exceptions, not bare `except:`
# ✅ Never silence exceptions without logging
# ✅ Use finally for cleanup (files, connections, locks)
# ✅ Create custom exceptions for your domain
# ✅ Use `raise X from Y` to preserve exception chain
# ✅ Use contextlib.suppress only for truly ignorable errors
# ✅ Use assert only for dev-time invariants, not production checks
#
# ❌ except:              → catches EVERYTHING including KeyboardInterrupt
# ❌ except Exception: pass → silently swallows errors
# ❌ using exceptions for flow control (use if/else instead)

# GOOD
def safe_divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

# BAD — using exception for normal flow control
def bad_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None                       # use `if b == 0` instead


# ─────────────────────────────────────────────────────────────
# PART 9: PRACTICE QUESTIONS
# ─────────────────────────────────────────────────────────────

# Q1. Safe int converter — return None instead of crashing
def safe_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

print(safe_int('42'))    # 42
print(safe_int('abc'))   # None
print(safe_int(None))    # None


# Q2. Retry decorator — retry a function N times on exception
import functools, time as _time

def retry(times=3, delay=0.1, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == times:
                        raise
                    print(f'Attempt {attempt} failed: {e}. Retrying...')
                    _time.sleep(delay)
        return wrapper
    return decorator

@retry(times=3, delay=0.05, exceptions=(ValueError,))
def flaky(n):
    import random
    if random.random() < 0.7:
        raise ValueError('Random failure')
    return f'Success on attempt with n={n}'

try:
    print(flaky(5))
except ValueError:
    print('All retries exhausted')


# Q3. Custom exception hierarchy for a bank app
class BankError(Exception): pass
class InsufficientFundsError(BankError):
    def __init__(self, balance, amount):
        super().__init__(f'Need {amount}, have {balance}')
        self.balance = balance
        self.amount  = amount

class AccountLockedError(BankError): pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(e)                              # Need 150, have 100
except BankError as e:
    print(f'Bank error: {e}')
