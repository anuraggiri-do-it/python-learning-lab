# ═══════════════════════════════════════════════════════════════
#                   TWO POINTER PATTERN
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS TWO POINTER?
# ─────────────────────────────────────────────────────────────
# Use two index variables that move through an array/string,
# usually from opposite ends or at different speeds.
# Reduces O(n²) brute force to O(n) in most cases.
#
# ANALOGY: Two people walking toward each other 🚶→ ←🚶
#   Left pointer starts at beginning → moves right
#   Right pointer starts at end      → moves left
#   They meet in the middle when done
#
# ─────────────────────────────────────────────────────────────
# IDENTIFY — use two pointer when you see:
# ─────────────────────────────────────────────────────────────
#   ✅ Sorted array + find pair with target sum
#   ✅ "Find two numbers that..."
#   ✅ Palindrome check
#   ✅ Remove duplicates in-place
#   ✅ Container with most water
#   ✅ Squaring a sorted array
#   ✅ Triplet / quadruplet sum problems
#
# ─────────────────────────────────────────────────────────────
# TWO MAIN VARIANTS:
# ─────────────────────────────────────────────────────────────
#   Opposite ends  → left=0, right=n-1, move toward each other
#   Same direction → both start at 0, one moves faster (slow/fast)
#
# ─────────────────────────────────────────────────────────────
# QUESTION LIST (this folder):
# ─────────────────────────────────────────────────────────────
#   1. two_sum_sorted.py          → LC 167  - pair with target sum
#   2. remove_duplicates.py       → LC 26   - remove duplicates in-place
#   3. squaring_sorted_array.py   → LC 977  - squares of sorted array
#   4. triplet_sum_zero.py        → LC 15   - three sum = 0
#   5. container_with_water.py    → LC 11   - max water container
#   6. palindrome.py              → valid palindrome check
# ═══════════════════════════════════════════════════════════════
