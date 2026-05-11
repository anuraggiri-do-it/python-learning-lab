# ═══════════════════════════════════════════════════════════════
#         INPUT, OUTPUT, COMMENTS & DOCSTRINGS
# ═══════════════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════════════
# PART 1: OUTPUT — print()
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: Megaphone 📢
#   print() = shout a message to the console
#   sep, end, file, flush = control HOW you shout

# basic
print('Hello, World!')
print('a', 'b', 'c')               # a b c  (space-separated by default)

# sep — custom separator
print('a', 'b', 'c', sep='-')      # a-b-c
print('2024', '01', '15', sep='/')  # 2024/01/15
print(*[1, 2, 3], sep=', ')        # 1, 2, 3  (unpack list)

# end — custom line ending (default is '\n')
print('Hello', end=' ')
print('World')                      # Hello World  (on same line)
print('Loading', end='')
print('...')                        # Loading...

# file — redirect output
import sys
print('Error message', file=sys.stderr)     # print to stderr

# flush — force immediate output (useful in loops/progress bars)
import time
for i in range(3):
    print(f'\rProgress: {i+1}/3', end='', flush=True)
    time.sleep(0.1)
print()                             # newline after progress


# ═══════════════════════════════════════════════════════════════
# PART 2: STRING FORMATTING
# ═══════════════════════════════════════════════════════════════

name  = 'Alice'
score = 95.6789
count = 1234567

# ── f-strings (Python 3.6+) — PREFERRED ─────────────────────
print(f'Name: {name}')                      # Name: Alice
print(f'Score: {score:.2f}')                # Score: 95.68
print(f'Score: {score:.0f}')                # Score: 96
print(f'Count: {count:,}')                  # Count: 1,234,567
print(f'Count: {count:_}')                  # Count: 1_234_567
print(f'Hex: {255:#x}')                     # Hex: 0xff
print(f'Binary: {10:#b}')                   # Binary: 0b1010
print(f'Percent: {0.856:.1%}')              # Percent: 85.6%
print(f'Sci: {0.000123:.2e}')               # Sci: 1.23e-04

# alignment
print(f'{"left":<10}|')                     # left      |
print(f'{"right":>10}|')                    # right|
print(f'{"center":^10}|')                   # center|
print(f'{"fill":*^10}|')                    # ***fill***|

# expressions inside f-strings
x = 10
print(f'{x} squared = {x**2}')
print(f'{"yes" if x > 5 else "no"}')        # yes
print(f'{name!r}')                           # 'Alice'  ← repr
print(f'{name!s}')                           # Alice    ← str
print(f'{name!a}')                           # 'Alice'  ← ascii

# debug format (Python 3.8+)
print(f'{score=}')                           # score=95.6789
print(f'{score=:.2f}')                       # score=95.68

# ── .format() ────────────────────────────────────────────────
print('{} is {} years old'.format(name, 30))
print('{0} and {0} again'.format(name))      # reuse positional
print('{n} scored {s:.1f}'.format(n=name, s=score))

# ── % formatting (old style — avoid) ─────────────────────────
print('%s scored %.2f' % (name, score))


# ═══════════════════════════════════════════════════════════════
# PART 3: INPUT — input()
# ═══════════════════════════════════════════════════════════════
#
# input() ALWAYS returns a STRING — cast manually if needed
# ANALOGY: Question box 📝 — you ask, user types, you get a string back

# basic (commented out to avoid blocking execution)
# name = input('Enter your name: ')
# age  = int(input('Enter your age: '))
# price = float(input('Enter price: '))

# safe input with validation
def get_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f'Must be at least {min_val}')
                continue
            if max_val is not None and value > max_val:
                print(f'Must be at most {max_val}')
                continue
            return value
        except ValueError:
            print('Please enter a valid integer')

# age = get_int('Enter age (1-120): ', 1, 120)

# reading multiple values on one line
# values = input('Enter numbers: ').split()   # '1 2 3' → ['1','2','3']
# nums   = list(map(int, values))             # ['1','2','3'] → [1,2,3]

# reading a list of ints in one line
# nums = [int(x) for x in input('Numbers: ').split()]


# ═══════════════════════════════════════════════════════════════
# PART 4: COMMENTS
# ═══════════════════════════════════════════════════════════════
#
# Comments = notes for humans, ignored by Python
# RULE: explain WHY, not WHAT (code shows what)

# single-line comment
x = 10  # inline comment — 2 spaces before #, 1 space after

# multi-line — use multiple # lines (NOT triple quotes)
# Step 1: validate input
# Step 2: process data
# Step 3: return result

# GOOD comment — explains WHY
x = x + 1  # Compensate for off-by-one in legacy API response

# BAD comment — explains WHAT (obvious from code)
# x = x + 1  # Add 1 to x  ← useless

# TODO / FIXME / NOTE — common conventions
# TODO: add input validation here
# FIXME: this breaks when list is empty
# NOTE: API returns 1-indexed values, convert to 0-indexed

# commented-out code — use sparingly, prefer version control
# old_method = lambda x: x * 2   # replaced by new_method


# ═══════════════════════════════════════════════════════════════
# PART 5: DOCSTRINGS
# ═══════════════════════════════════════════════════════════════
#
# Docstrings = string literals as the FIRST statement in a
# module, class, or function. Stored in __doc__ attribute.
# Used by help(), IDEs, and documentation generators (Sphinx).
#
# ANALOGY: Product manual 📖
#   Code = the product
#   Docstring = the manual explaining what it does and how to use it

# ── one-liner docstring ──────────────────────────────────────
def add(a, b):
    """Return the sum of a and b."""
    return a + b


# ── multi-line docstring (Google style) ─────────────────────
def divide(a, b):
    """
    Divide a by b and return the result.

    Args:
        a (float): The numerator.
        b (float): The denominator. Must not be zero.

    Returns:
        float: The result of a divided by b.

    Raises:
        ValueError: If b is zero.

    Example:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 0)
        ValueError: Cannot divide by zero
    """
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b


# ── NumPy / SciPy style docstring ───────────────────────────
def normalize(data, min_val=0, max_val=1):
    """
    Normalize a list of numbers to a given range.

    Parameters
    ----------
    data : list of float
        Input values to normalize.
    min_val : float, optional
        Minimum value of output range. Default is 0.
    max_val : float, optional
        Maximum value of output range. Default is 1.

    Returns
    -------
    list of float
        Normalized values in [min_val, max_val].

    Examples
    --------
    >>> normalize([0, 5, 10])
    [0.0, 0.5, 1.0]
    """
    lo = min(data)
    hi = max(data)
    return [min_val + (x - lo) / (hi - lo) * (max_val - min_val) for x in data]


# ── class docstring ──────────────────────────────────────────
class Rectangle:
    """
    Represents a rectangle with width and height.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Example:
        >>> r = Rectangle(4, 5)
        >>> r.area()
        20
    """

    def __init__(self, width, height):
        """
        Initialize Rectangle with width and height.

        Args:
            width (float): Width of the rectangle. Must be positive.
            height (float): Height of the rectangle. Must be positive.

        Raises:
            ValueError: If width or height is not positive.
        """
        if width <= 0 or height <= 0:
            raise ValueError('Width and height must be positive')
        self.width  = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def is_square(self):
        """Return True if the rectangle is a square."""
        return self.width == self.height


# ── accessing docstrings ─────────────────────────────────────
print(add.__doc__)
print(divide.__doc__)
print(Rectangle.__doc__)
print(Rectangle.__init__.__doc__)

help(Rectangle)                     # full formatted help


# ═══════════════════════════════════════════════════════════════
# PART 6: pprint — pretty printing complex data
# ═══════════════════════════════════════════════════════════════

from pprint import pprint

data = {
    'users': [
        {'name': 'Alice', 'age': 30, 'skills': ['Python', 'ML', 'SQL']},
        {'name': 'Bob',   'age': 25, 'skills': ['JS', 'React']},
    ],
    'total': 2,
    'active': True,
}

print(data)         # one long line — hard to read
pprint(data)        # nicely formatted — easy to read
pprint(data, depth=1)       # limit nesting depth
pprint(data, width=40)      # wrap at 40 chars


# ═══════════════════════════════════════════════════════════════
# QUICK REFERENCE
# ═══════════════════════════════════════════════════════════════
#
#   print(x, sep=' ', end='\n', file=sys.stdout, flush=False)
#   input('prompt')          → always returns str
#
#   f'{val:.2f}'             → 2 decimal places
#   f'{val:,}'               → thousands separator
#   f'{val:>10}'             → right-align in 10 chars
#   f'{val:^10}'             → center in 10 chars
#   f'{val:.1%}'             → percentage
#   f'{val=}'                → debug: prints name=value
#
#   # comment               → single line
#   """docstring"""          → first statement in func/class/module
#   __doc__                  → access docstring programmatically
#   help(obj)                → formatted docstring output
