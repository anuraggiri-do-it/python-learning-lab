# ============================================================
# LC 457 — Circular Array Loop
# ============================================================


# ── 1. WHAT MAKES THIS DIFFERENT ─────────────────────────────
# You still have:
#   index → next index
#
# But now:
#   Movement can be forward or backward
#   Cycle must have:
#     same direction only (all + or all -)
#     length > 1 (no self-loop)


# ── 2. DEFINE "NEXT INDEX" ───────────────────────────────────
# You need a safe way to move in a circular array:
#
# def next_index(nums, i):
#     n = len(nums)
#     return (i + nums[i]) % n


# ── 3. TWO CRITICAL CONSTRAINTS ──────────────────────────────
# 1. Same direction only
#      nums[i] * nums[next] > 0
#      → ensures both positive OR both negative
#
# 2. No self-loop
#      next_index(i) == i → invalid
#      → cycle length must be > 1


# ── 4. APPLY FLOYD'S CYCLE DETECTION ────────────────────────
# For each index:
#   start slow and fast
#   move:
#     slow → 1 step
#     fast → 2 steps


# ── 5. FULL CODE ─────────────────────────────────────────────
class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = i
            direction = nums[i] > 0

            while True:
                # move slow 1 step
                nxt = next_index(slow)
                if (nums[nxt] > 0) != direction:
                    break
                slow = nxt

                # move fast 2 steps
                nxt = next_index(fast)
                if (nums[nxt] > 0) != direction:
                    break

                nxt2 = next_index(nxt)
                if (nums[nxt2] > 0) != direction:
                    break
                fast = nxt2

                # cycle found
                if slow == fast:
                    if slow == next_index(slow):
                        break       # self-loop → invalid
                    return True

            # mark visited path as 0 (optimization)
            j = i
            while nums[j] != 0 and (nums[j] > 0) == direction:
                nxt = next_index(j)
                nums[j] = 0
                j = nxt

        return False


# ── 6. PATTERN CONNECTION ────────────────────────────────────
# Problem                  Type
# ─────────────────────────────────────────
# Linked List Cycle     →  detect cycle
# Happy Number          →  detect cycle
# Find Duplicate        →  find cycle start
# This problem          →  detect cycle with constraints


# ── 7. WHY THIS IS HARDER ────────────────────────────────────
# Cycle must satisfy:
#   1. Same direction
#   2. Length > 1
#   3. Circular indexing
#
# So plain Floyd is not enough — you must filter invalid moves


# ── 8. KEY MENTAL MODEL ──────────────────────────────────────
# Array → Graph (each index has one outgoing edge)
#
# Then:
#   Find cycle under constraints


# ── 9. COMMON MISTAKES ───────────────────────────────────────
# ❌ Ignoring direction     → counts invalid cycles
# ❌ Not checking self-loop → [1,1,1] might falsely pass
# ❌ Not marking visited    → leads to O(n²)


# ── 10. PATTERN EXTRACTION ───────────────────────────────────
# Whenever you see:
#   - circular structure
#   - jump rules
#   - repeated movement
#
# → Think:
#   Graph + Cycle detection


# ── 11. FINAL INSIGHT ────────────────────────────────────────
# This problem tests whether you can:
#   Adapt Floyd's algorithm under constraints
#   — not just apply it blindly


# ── 12. TEST CASES ───────────────────────────────────────────
sol = Solution()

print(sol.circularArrayLoop([2, -1, 1, 2, 2]))   # True  → cycle: 0→2→3→0
print(sol.circularArrayLoop([-1, 2]))             # False → direction changes
print(sol.circularArrayLoop([-2, 1, -1, -2, -2]))# False → no valid cycle
print(sol.circularArrayLoop([1, 1, 1, 1]))        # True  → all forward cycle
print(sol.circularArrayLoop([1]))                 # False → self-loop only
