# ============================================================
# OOP 6 — Special Methods, Class Methods, Static Methods
# ============================================================
# ANALOGY: THE TEA SHOP SYSTEM
#
#   __str__       = the label on the cup  ("Masala Tea, 2 sugars")
#   __repr__      = the shop's internal record  (for debugging)
#   __eq__        = are two cups the same recipe?
#   __add__       = blend two teas together
#   @classmethod  = shop-level action (affects all cups / the shop itself)
#   @staticmethod = general tea knowledge (no cup or shop needed)
#
# ============================================================

class Tea:
    total_cups = 0                     # CLASS variable — shared by ALL objects

    def __init__(self, tea_type, sugar, milk):
        self.tea_type = tea_type
        self.sugar    = sugar
        self.milk     = milk
        Tea.total_cups += 1            # every new cup increments shop counter

    # ── DUNDER: human-readable string (print / str()) ───────
    # Like the label written on your cup
    def __str__(self):
        milk_str = "with milk" if self.milk else "no milk"
        return f"{self.tea_type} Tea | sugar: {self.sugar} | {milk_str}"

    # ── DUNDER: developer/debug string (repr()) ─────────────
    # Like the internal order ticket in the kitchen
    def __repr__(self):
        return f"Tea('{self.tea_type}', sugar={self.sugar}, milk={self.milk})"

    # ── DUNDER: equality check ───────────────────────────────
    # Two cups are "equal" if same type, sugar, milk
    def __eq__(self, other):
        return (self.tea_type == other.tea_type and
                self.sugar    == other.sugar    and
                self.milk     == other.milk)

    # ── DUNDER: blend two teas (+ operator) ─────────────────
    # cup1 + cup2 → a new blended tea
    def __add__(self, other):
        blended_type = f"{self.tea_type}-{other.tea_type} Blend"
        avg_sugar    = (self.sugar + other.sugar) // 2
        return Tea(blended_type, avg_sugar, self.milk or other.milk)

    # ── CLASS METHOD ────────────────────────────────────────
    # Acts on the CLASS itself, not a specific object
    # Like the shop manager checking total cups made today
    @classmethod
    def get_total_cups(cls):
        return f"Total cups made today: {cls.total_cups}"

    # Alternative constructor — create Tea from a string "Masala,2,True"
    @classmethod
    def from_string(cls, tea_string):
        tea_type, sugar, milk = tea_string.split(",")
        return cls(tea_type, int(sugar), milk.strip() == "True")

    # ── STATIC METHOD ───────────────────────────────────────
    # General tea knowledge — doesn't need self or cls
    # Like a tea fact board in the shop — no specific cup needed
    @staticmethod
    def ideal_temperature(tea_type):
        temps = {
            "Green":  "75–80°C  (don't boil — ruins the taste)",
            "Black":  "90–95°C",
            "Masala": "90–95°C  (needs full boil for spices)",
            "White":  "70–75°C  (most delicate)",
        }
        return temps.get(tea_type, "85°C (general default)")


# ── USAGE ───────────────────────────────────────────────────
cup1 = Tea("Masala", 2, True)
cup2 = Tea("Green",  0, False)
cup3 = Tea("Masala", 2, True)

print(cup1)                            # __str__  → readable label
print(repr(cup1))                      # __repr__ → debug info

print(cup1 == cup3)                    # True  — same recipe
print(cup1 == cup2)                    # False — different

blend = cup1 + cup2                    # __add__
print(blend)                           # Masala-Green Blend

print(Tea.get_total_cups())            # classmethod — 3 cups made

cup4 = Tea.from_string("Ginger, 1, True")   # alternative constructor
print(cup4)

print(Tea.ideal_temperature("Green"))  # staticmethod — no object needed
print(Tea.ideal_temperature("Masala"))

# ── KEY POINTS ──────────────────────────────────────────────
# __str__      → called by print() and str()   — for humans
# __repr__     → called by repr()              — for developers
# __eq__       → called by ==                  — custom equality
# __add__      → called by +                   — custom operator
# @classmethod → receives cls, works on class  — factory methods
# @staticmethod→ no self/cls, pure utility     — helper functions
