# ============================================================
# LC 287 — Find the Duplicate Number
# ============================================================


# ── 1. UNDERSTAND THE TRICK (core idea) ─────────────────────
# You are given:
#   nums[i] is in range [1, n]
#   Array size = n + 1
#
# That means:
#   There must be a duplicate (Pigeonhole Principle)


# ── 2. CONVERT ARRAY → LINKED STRUCTURE ─────────────────────
# This is the key step most people miss.
#
# Treat:
#   index → value
# as:
#   i → nums[i]
#
# So you can think:
#   0 → nums[0]
#         ↓
#       nums[nums[0]]
#         ↓
#       nums[nums[nums[0]]]
#
# This behaves like a linked list


# ── 3. WHY CYCLE MUST EXIST ──────────────────────────────────
# Because:
#   Values are in [1, n]
#   You keep jumping indices
#   Eventually you revisit a number
#   → cycle forms
#   → duplicate = cycle entry


# ── 4. SO THIS BECOMES ───────────────────────────────────────
# Detect cycle + find start of cycle
#
# This is exactly:
#   Floyd's Algorithm (fast & slow)
#   Same as your linked list cycle II problem


# ── 5. CODE (step-by-step) ───────────────────────────────────

# Phase 1: detect meeting point
# slow = nums[0]
# fast = nums[0]
#
# while True:
#     slow = nums[slow]
#     fast = nums[nums[fast]]
#
#     if slow == fast:
#         break

# Phase 2: find cycle start (duplicate)
# slow = nums[0]
#
# while slow != fast:
#     slow = nums[slow]
#     fast = nums[fast]
#
# return slow


# ── 6. FULL SOLUTION ─────────────────────────────────────────
class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        # Phase 1
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


# ── 7. DRY RUN (important) ───────────────────────────────────
# nums = [1, 3, 4, 2, 2]
#
# Structure:
#   0 → 1 → 3 → 2 → 4 → 2  (cycle)
#
# Cycle starts at:
#   2  (duplicate)


# ── 8. PATTERN CONNECTION (VERY important) ───────────────────
# Problem                  What you did
# ─────────────────────────────────────────
# Linked List Cycle II  →  find cycle start
# Happy Number          →  detect cycle
# This problem          →  find cycle start


# ── 9. KEY SHIFT IN THINKING ─────────────────────────────────
# Array ≠ just array
# Array = graph / linked structure


# ── 10. FINAL TAKEAWAY ───────────────────────────────────────
# You should now recognize instantly:
#
# If:
#   - values act like pointers
#   - range is restricted
#   - repetition exists
#
# Then:
#   → convert to cycle problem
#   → apply Floyd's algorithm
