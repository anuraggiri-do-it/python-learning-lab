# ============================================================
# LC 876 — Middle of the Linked List
# Pure fast–slow pointer problem. No tricks beyond that.
# ============================================================


# ── 1. WHAT THE QUESTION IS ASKING ──────────────────────────
# Return the middle node
# If two middles exist → return the second one


# ── 2. KEY IDEA ──────────────────────────────────────────────
# Use two pointers:
#   slow → moves 1 step
#   fast → moves 2 steps


# ── 3. HOW IT WORKS ──────────────────────────────────────────
# When fast reaches the end
# slow will be at the middle


# ── 4. CODE ──────────────────────────────────────────────────
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


# ── 5. WHY THIS RETURNS SECOND MIDDLE ───────────────────────
# Case 1: Odd length
#   1 → 2 → 3 → 4 → 5
#               ↑
#             slow
#   → Perfect middle → 3
#
# Case 2: Even length
#   1 → 2 → 3 → 4 → 5 → 6
#                   ↑
#                 slow
#   → Two middles: 3 and 4
#   → slow lands on 4 (second middle) ✅


# ── 6. WHY IT WORKS (important intuition) ───────────────────
# Each step:
#   fast moves twice as quickly
#   So when fast finishes the list:
#   slow has covered half the distance


# ── 7. PATTERN EXTRACTION ────────────────────────────────────
# Problem                  Goal
# ─────────────────────────────────────────
# Linked List Cycle     →  detect loop
# Happy Number          →  detect loop
# Find Duplicate        →  find cycle start
# Middle of List        →  find midpoint
#
# Same tool: fast & slow pointers


# ── 8. COMMON MISTAKE ────────────────────────────────────────
# Some people try:
#   count nodes → divide by 2
#
# That works but:
#   requires 2 passes ❌
#   less elegant


# ── 9. MENTAL SHORTCUT ───────────────────────────────────────
# Whenever you see:
#   "middle", "half", "balanced split"
#
# → Immediately think:
#   fast = 2x speed
#   slow = 1x speed


# ── 10. TEST CASES ───────────────────────────────────────────
def build(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

sol = Solution()

# Odd length → single middle
head = build([1, 2, 3, 4, 5])
print(to_list(sol.middleNode(head)))    # [3, 4, 5]

# Even length → second middle
head = build([1, 2, 3, 4, 5, 6])
print(to_list(sol.middleNode(head)))    # [4, 5, 6]

# Single node
head = build([1])
print(to_list(sol.middleNode(head)))    # [1]

# Two nodes → second node
head = build([1, 2])
print(to_list(sol.middleNode(head)))    # [2]
