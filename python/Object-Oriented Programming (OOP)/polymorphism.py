# ============================================================
# OOP 4 — Polymorphism
# ============================================================
# ANALOGY: ONE COMMAND "MAKE TEA" — DIFFERENT RESULTS
#
#   You tell three people: "Make me tea."
#   → Your mom makes Masala Tea with milk and spices
#   → Your friend makes Green Tea with lemon
#   → A café makes Iced Tea with ice
#
#   Same command → "make tea"
#   Different behaviour depending on WHO you asked
#
#   That is Polymorphism:
#   SAME method name → DIFFERENT behaviour based on the object
#
#   Two types:
#   1. METHOD OVERRIDING  → child redefines parent's method
#   2. DUCK TYPING        → if it has the method, it works (Python style)
#
# ============================================================

# ── BASE CLASS ──────────────────────────────────────────────
class Tea:
    def brew(self):
        print("Brewing generic tea...")

    def describe(self):
        print("I am a tea.")


# ── CHILD CLASSES — each overrides brew() differently ───────
class MasalaTea(Tea):
    def brew(self):                          # OVERRIDES parent brew()
        print("Boiling water → adding spices → adding milk → Masala Tea ☕")


class GreenTea(Tea):
    def brew(self):                          # OVERRIDES parent brew()
        print("Heating water to 80°C → steeping 3 min → Green Tea 🍵")


class IcedTea(Tea):
    def brew(self):                          # OVERRIDES parent brew()
        print("Brewing strong tea → cooling → adding ice → Iced Tea 🧊")


# ── POLYMORPHISM IN ACTION ───────────────────────────────────
# Same function, works on ANY tea object
def serve_tea(tea_obj):
    tea_obj.brew()                           # calls the RIGHT brew() automatically


teas = [MasalaTea(), GreenTea(), IcedTea()]

for tea in teas:
    serve_tea(tea)                           # same call → different output


# ── DUCK TYPING (Python's natural polymorphism) ─────────────
# "If it walks like a duck and quacks like a duck, it's a duck"
# Python doesn't care about the TYPE — only if the METHOD exists

class HerbalTea:                             # doesn't even inherit from Tea!
    def brew(self):
        print("Steeping herbs in warm water → Herbal Tea 🌿")

herbal = HerbalTea()
serve_tea(herbal)                            # works! because it has brew() ✅


# ── METHOD OVERRIDING vs OVERLOADING ────────────────────────
# Python does NOT support method overloading (same name, diff params)
# Instead use default arguments:

class TeaMaker:
    def make(self, tea_type="Masala", cups=1):
        print(f"Making {cups} cup(s) of {tea_type} tea.")

maker = TeaMaker()
maker.make()                    # Masala, 1 cup
maker.make("Green", 2)          # Green, 2 cups

# ── KEY POINTS ──────────────────────────────────────────────
# 1. Same method name → different behaviour = Polymorphism
# 2. Override parent method in child class
# 3. Python uses Duck Typing — type doesn't matter, method does
# 4. No true overloading in Python → use default args instead
