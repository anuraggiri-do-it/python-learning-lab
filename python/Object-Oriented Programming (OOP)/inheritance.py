# ============================================================
# OOP 2 — Inheritance
# ============================================================
# ANALOGY: BASE TEA RECIPE → SPECIALISED TEA RECIPES
#
#   Imagine you have a basic tea recipe (parent class).
#   Now you want to make Masala Tea and Green Tea.
#   Both are still "tea" — they share the base steps.
#   But each adds its OWN special steps on top.
#
#   PARENT CLASS (Base Tea)  → has common steps: boil water, add leaves
#   CHILD CLASS  (MasalaTea) → inherits base steps + adds spices
#   CHILD CLASS  (GreenTea)  → inherits base steps + steeps differently
#
#   Inheritance = "is-a" relationship
#   MasalaTea IS-A Tea ✅
#   GreenTea  IS-A Tea ✅
#
# ============================================================

# ── PARENT CLASS ────────────────────────────────────────────
class Tea:
    def __init__(self, tea_type, temperature):
        self.tea_type    = tea_type
        self.temperature = temperature

    def boil_water(self):
        print("Boiling water...")

    def add_leaves(self):
        print(f"Adding {self.tea_type} leaves.")

    def describe(self):
        print(f"{self.tea_type} tea at {self.temperature}°C")


# ── CHILD CLASS 1 ───────────────────────────────────────────
class MasalaTea(Tea):                        # inherits from Tea
    def __init__(self, temperature, spices):
        super().__init__("Masala", temperature)  # call parent __init__
        self.spices = spices                 # extra attribute

    def add_spices(self):                    # extra method
        print(f"Adding spices: {', '.join(self.spices)}")

    def brew(self):
        self.boil_water()                    # inherited from Tea
        self.add_spices()                    # own method
        self.add_leaves()                    # inherited from Tea
        print("Masala tea is ready! ☕")


# ── CHILD CLASS 2 ───────────────────────────────────────────
class GreenTea(Tea):                         # inherits from Tea
    def __init__(self, temperature, steep_time):
        super().__init__("Green", temperature)
        self.steep_time = steep_time         # extra attribute

    def steep(self):                         # extra method
        print(f"Steeping for {self.steep_time} minutes (don't over-steep!).")

    def brew(self):
        self.boil_water()                    # inherited
        self.steep()                         # own method
        print("Green tea is ready! 🍵")


# ── USAGE ───────────────────────────────────────────────────
masala = MasalaTea(90, ["cardamom", "ginger", "cinnamon"])
masala.brew()
masala.describe()    # inherited method works on child too

print()

green = GreenTea(80, 3)
green.brew()
green.describe()

# ── KEY POINTS ──────────────────────────────────────────────
# 1. Child class gets ALL methods and attributes of parent
# 2. super().__init__() → calls parent's constructor
# 3. Child can ADD new methods (add_spices, steep)
# 4. Child can OVERRIDE parent methods (brew)
# 5. isinstance(masala, Tea) → True  (child IS-A parent)
print(isinstance(masala, Tea))   # True
print(isinstance(green,  Tea))   # True
