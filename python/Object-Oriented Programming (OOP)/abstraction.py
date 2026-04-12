# ============================================================
# OOP 5 — Abstraction
# ============================================================
# ANALOGY: TEA SHOP MENU
#
#   When you order tea at a shop:
#   → You see the MENU (what's available)
#   → You DON'T see how the kitchen works
#   → The shop FORCES every tea to have a name and a brew() method
#   → But HOW each tea is brewed is up to each tea type
#
#   Abstraction = showing WHAT to do, hiding HOW it's done
#
#   Abstract Class  = the MENU (defines what must exist)
#   Abstract Method = items on the menu (must be implemented)
#   Concrete Class  = actual tea recipes (fills in the HOW)
#
#   You CANNOT order from the menu itself (can't instantiate abstract class)
#   You order a SPECIFIC tea (concrete class)
#
# ============================================================

from abc import ABC, abstractmethod   # ABC = Abstract Base Class


# ── ABSTRACT CLASS (the menu — defines rules) ───────────────
class Tea(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def brew(self):
        pass                           # no implementation — subclass MUST define

    @abstractmethod
    def ingredients(self):
        pass                           # subclass MUST define

    # concrete method — shared by all teas (not abstract)
    def serve(self):
        print(f"Serving {self.name}... enjoy! ☕")


# ── CONCRETE CLASS 1 (fills in the HOW) ─────────────────────
class MasalaTea(Tea):
    def __init__(self):
        super().__init__("Masala Tea")

    def brew(self):                    # MUST implement — abstract method
        print("Boil water → add spices → add milk → simmer 5 min")

    def ingredients(self):             # MUST implement — abstract method
        return ["water", "milk", "ginger", "cardamom", "tea leaves", "sugar"]


# ── CONCRETE CLASS 2 ────────────────────────────────────────
class GreenTea(Tea):
    def __init__(self):
        super().__init__("Green Tea")

    def brew(self):
        print("Heat water to 80°C → steep leaves 2-3 min → remove leaves")

    def ingredients(self):
        return ["water", "green tea leaves"]


# ── USAGE ───────────────────────────────────────────────────
masala = MasalaTea()
masala.brew()
masala.serve()                         # concrete method from abstract class
print("Ingredients:", masala.ingredients())

print()

green = GreenTea()
green.brew()
green.serve()

# ── CANNOT instantiate abstract class directly ───────────────
# tea = Tea("Some Tea")   # ❌ TypeError: Can't instantiate abstract class

# ── KEY POINTS ──────────────────────────────────────────────
# 1. ABC        → marks a class as abstract
# 2. @abstractmethod → forces child to implement the method
# 3. Abstract class CAN have concrete methods (like serve())
# 4. You CANNOT create an object of an abstract class
# 5. Abstraction hides complexity, shows only what's necessary
#
# Abstraction vs Encapsulation:
#   Encapsulation = HIDING data (private attributes)
#   Abstraction   = HIDING implementation (abstract methods)
