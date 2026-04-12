# LC 202 — Happy Number
# https://leetcode.com/problems/happy-number/
# Pattern: Fast & Slow Pointer (cycle detection on implicit sequence)
#
# Problem:
#   A number is "happy" if repeatedly replacing it with the sum of squares
#   of its digits eventually reaches 1.
#   If it never reaches 1, it loops forever → return False.
#
# Intuition:
#   n → f(n) → f(f(n)) → ...  forms an implicit linked list.
#   - Happy number   → sequence reaches 1 (no cycle before 1)
#   - Unhappy number → sequence loops forever (cycle detected)
#
#   Apply Floyd's cycle detection:
#     slow moves 1 step, fast moves 2 steps.
#     If fast == 1  → happy
#     If slow == fast (and ≠ 1) → cycle → not happy
#
# Why not HashSet?
#   HashSet works but uses O(n) space.
#   Fast & slow gives O(1) space — same pattern as LC 141/142.
#
# Time:  O(log n) per step × O(n) steps = O(n log n)
# Space: O(1)


def get_next(n: int) -> int:
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total


def isHappy(n: int) -> bool:
    slow, fast = n, n
    while True:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
        if fast == 1:
            return True
        if slow == fast:
            return False


# ─── Test Cases ─────────────────────────────────────────────────

# n = 19 trace (happy):
#   19 → 82 → 68 → 100 → 1  ✅
assert isHappy(19) is True,  "TC1 failed"

# n = 2 trace (unhappy — enters cycle: 4→16→37→58→89→145→42→20→4):
assert isHappy(2)  is False, "TC2 failed"

assert isHappy(1)  is True,  "TC3 failed"   # base case
assert isHappy(7)  is True,  "TC4 failed"   # known happy
assert isHappy(4)  is False, "TC5 failed"   # known unhappy

print("All test cases passed ✅")
