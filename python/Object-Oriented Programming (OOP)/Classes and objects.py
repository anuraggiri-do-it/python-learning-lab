# ============================================================
# OOP 1 — Classes and Objects
# ============================================================
# ANALOGY: A RECIPE vs A CUP OF TEA
#
#   CLASS  = The recipe for making tea
#             → it defines: ingredients, steps, properties
#             → it does NOT exist physically, it's just a blueprint
#
#   OBJECT = An actual cup of tea made using that recipe
#             → it IS physical, it exists in memory
#             → you can make many cups (objects) from one recipe (class)
#
#   ATTRIBUTE = properties of the tea  (color, temperature, type)
#   METHOD    = actions you can do     (brew(), add_sugar(), drink())
#
# ============================================================

# ── CLASS (the recipe / blueprint) ──────────────────────────
class Tea:
    # __init__ = the moment you START making the tea
    # self     = "this particular cup" — refers to the object itself
    def __init__(self, tea_type, sugar, milk):
        self.tea_type    = tea_type    # attribute: type of tea
        self.sugar       = sugar       # attribute: spoons of sugar
        self.milk        = milk        # attribute: True/False
        self.temperature = "hot"       # attribute: default value

    # method = action you can perform on this cup of tea
    def brew(self):
        print(f"Brewing {self.tea_type} tea...")

    def add_sugar(self):
        print(f"Adding {self.sugar} spoon(s) of sugar.")

    def describe(self):
        milk_status = "with milk" if self.milk else "without milk"
        print(f"{self.tea_type} tea | sugar: {self.sugar} | {milk_status} | {self.temperature}")


# ── OBJECTS (actual cups of tea) ────────────────────────────
cup1 = Tea("Masala", 2, True)    # object 1 — masala tea
cup2 = Tea("Green",  0, False)   # object 2 — green tea (no sugar, no milk)
cup3 = Tea("Ginger", 1, True)    # object 3 — ginger tea

cup1.brew()
cup1.add_sugar()
cup1.describe()

print()
cup2.describe()   # each object has its OWN data

# ── KEY POINTS ──────────────────────────────────────────────
# 1. class  → blueprint (defined once)
# 2. object → instance  (created many times from same class)
# 3. self   → always refers to the current object
# 4. __init__ is called automatically when object is created
# 5. each object has its own copy of attributes
