# ============================================================
# OOP 3 — Encapsulation
# ============================================================
# ANALOGY: THE TEA MACHINE (you press a button, you don't see inside)
#
#   When you use a tea vending machine:
#   → You press "Masala Tea" button
#   → You don't see the internal boiler temperature, pipe pressure etc.
#   → The machine HIDES its internal details from you
#   → You only interact through the BUTTONS (public interface)
#
#   Encapsulation = bundling data + methods together
#                 + HIDING internal details from outside
#
#   PUBLIC    (name)    → anyone can access
#   PROTECTED (_name)   → meant for internal/subclass use (convention)
#   PRIVATE   (__name)  → strictly internal, name-mangled by Python
#
# ============================================================

class TeaMachine:
    def __init__(self):
        self.brand          = "ChaiBoss"    # public   — anyone can read
        self._water_level   = 500           # protected — internal use
        self.__boiler_temp  = 95            # private   — hidden completely

    # ── PUBLIC METHOD (the button you press) ────────────────
    def make_tea(self, tea_type):
        if self.__is_water_enough():         # uses private method internally
            self.__heat_water()              # uses private method internally
            print(f"Here is your {tea_type} tea! ☕")
        else:
            print("Not enough water! Please refill.")

    def refill_water(self, amount):
        self._water_level += amount
        print(f"Water refilled. Level: {self._water_level}ml")

    # ── PRIVATE METHODS (internal machine logic — hidden) ───
    def __heat_water(self):
        print(f"[Internal] Heating water to {self.__boiler_temp}°C")

    def __is_water_enough(self):
        return self._water_level >= 150

    # ── GETTER / SETTER (controlled access to private data) ─
    # Instead of directly accessing __boiler_temp,
    # we provide a controlled way to read/change it
    @property
    def boiler_temp(self):
        return self.__boiler_temp            # read allowed

    @boiler_temp.setter
    def boiler_temp(self, temp):
        if 60 <= temp <= 100:                # validation before setting
            self.__boiler_temp = temp
            print(f"Boiler temp set to {temp}°C")
        else:
            print("Invalid temp! Must be between 60–100°C")


# ── USAGE ───────────────────────────────────────────────────
machine = TeaMachine()

machine.make_tea("Masala")           # public interface — works fine
machine.refill_water(200)

print(machine.brand)                 # public — accessible ✅
print(machine.boiler_temp)           # via property getter ✅

machine.boiler_temp = 85             # via setter with validation ✅
machine.boiler_temp = 200            # rejected — out of range ❌

# print(machine.__boiler_temp)       # ❌ AttributeError — private!

# ── KEY POINTS ──────────────────────────────────────────────
# 1. Public    (name)   → accessible everywhere
# 2. Protected (_name)  → convention only, still accessible
# 3. Private   (__name) → Python name-mangles it → _ClassName__name
# 4. Use @property for controlled read access
# 5. Use @setter for controlled write access with validation
