# ─── Output ──────────────────────────────────────────────────────────────────
print("Hello, World!")
print("a", "b", "c")              # a b c
print("a", "b", sep="-")          # a-b
print("Hello", end=" ")           # no newline
print("World")                    # Hello World

# ─── Input ───────────────────────────────────────────────────────────────────
# name = input("Enter your name: ")       # always returns str
# age  = int(input("Enter your age: "))   # cast to int

# ─── Comments ────────────────────────────────────────────────────────────────
# single-line comment

x = 10  # inline comment

# Multi-line comment (use multiple #)
# line 1
# line 2

# ─── Docstrings ──────────────────────────────────────────────────────────────
def add(a, b):
    """Return the sum of a and b."""
    return a + b


def divide(a, b):
    """
    Divide a by b.

    Args:
        a (float): numerator
        b (float): denominator

    Returns:
        float: result of division

    Raises:
        ValueError: if b is zero
    """
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b


class Circle:
    """Represents a circle with a given radius."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Return area of the circle."""
        return 3.14 * self.radius ** 2


# Access docstring
print(add.__doc__)
print(divide.__doc__)
print(Circle.__doc__)
