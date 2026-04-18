# ═══════════════════════════════════════════════════════════════
#                     CYCLIC SORT PATTERN
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS CYCLIC SORT?
# ─────────────────────────────────────────────────────────────
# A sorting technique that places each number at its CORRECT
# INDEX in O(n) time and O(1) space.
#
# Core idea:
#   If array contains numbers in range [1, n] or [0, n-1],
#   then number `x` belongs at index `x-1` (or index `x`).
#   Keep swapping until every number is at its correct index.
#
# ─────────────────────────────────────────────────────────────
# HOW TO IDENTIFY — use cyclic sort when you see:
# ─────────────────────────────────────────────────────────────
#   ✅ Array of size n with numbers in range [1, n] or [0, n-1]
#   ✅ "Find missing number"
#   ✅ "Find duplicate number"
#   ✅ "Find all missing / all duplicates"
#   ✅ "Numbers from 1 to n, one is missing/repeated"
#   ✅ No extra space allowed (O(1) space constraint)
#
# ─────────────────────────────────────────────────────────────
# WHY CYCLIC SORT WORKS:
# ─────────────────────────────────────────────────────────────
#   If nums = [3,1,2] and range is [1,3]:
#     number 1 → belongs at index 0
#     number 2 → belongs at index 1
#     number 3 → belongs at index 2
#
#   After cyclic sort → [1,2,3]
#   Now scan: wherever nums[i] != i+1 → that index is the answer
#
# ─────────────────────────────────────────────────────────────
# THE TEMPLATE:
# ─────────────────────────────────────────────────────────────
#
#   i = 0
#   while i < len(nums):
#       correct = nums[i] - 1          # where nums[i] should go
#       if nums[i] != nums[correct]:   # not in right place → swap
#           nums[i], nums[correct] = nums[correct], nums[i]
#       else:
#           i += 1                     # already correct → move on
#
#   After this loop → every number is at its correct index
#   (or a duplicate/missing is revealed)
#
# ─────────────────────────────────────────────────────────────
# WHY NOT JUST SORT NORMALLY?
# ─────────────────────────────────────────────────────────────
#   Normal sort  → O(n log n)
#   Cyclic sort  → O(n)  ← faster because we know WHERE each
#                          number belongs without comparing
#
# ─────────────────────────────────────────────────────────────
# QUESTION LIST (this folder):
# ─────────────────────────────────────────────────────────────
#   1. cyclic_sort.py              → sort array [1,n] in place
#   2. missing_number.py           → LC 268  - one missing in [0,n]
#   3. all_missing_numbers.py      → LC 448  - all missing in [1,n]
#   4. duplicate_number.py         → LC 287  - one duplicate in [1,n]
#   5. all_duplicates.py           → LC 442  - all duplicates in [1,n]
#   6. duplicate_and_missing.py    → LC 645  - find both duplicate & missing
#   7. first_missing_positive.py   → LC 41   - smallest missing positive (hard)
#
# ─────────────────────────────────────────────────────────────
# PATTERN VARIATIONS:
# ─────────────────────────────────────────────────────────────
#   Range [1, n]  → correct index = nums[i] - 1
#   Range [0, n]  → correct index = nums[i]
#   Duplicates    → swap condition: nums[i] != nums[correct]
#                   (prevents infinite swap loop on duplicates)
# ═══════════════════════════════════════════════════════════════
