# ============================================================
# LC 143 — Reorder List
# ============================================================


# ── 1. WHAT THE PROBLEM WANTS ────────────────────────────────
# Transform:
#   L0 → L1 → L2 → ... → Ln
# into:
#   L0 → Ln → L1 → Ln-1 → L2 → Ln-2 ...
#
# So you need:
#   front part
#   reversed back part
#   then interleave


# ── 2. STEP-BY-STEP PLAN ─────────────────────────────────────

# Step 1: Find middle
# slow = head
# fast = head
#
# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next

# Step 2: Reverse second half
# prev = None
# curr = slow.next
# slow.next = None   # cut the list
#
# while curr:
#     nxt = curr.next
#     curr.next = prev
#     prev = curr
#     curr = nxt
#
# Now:
#   first half  = head
#   second half = prev (reversed)

# Step 3: Merge alternately
# first = head
# second = prev
#
# while second:
#     tmp1 = first.next
#     tmp2 = second.next
#
#     first.next = second
#     second.next = tmp1
#
#     first = tmp1
#     second = tmp2


# ── 3. FULL CODE ─────────────────────────────────────────────
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        prev = None
        curr = slow.next
        slow.next = None        # cut the list

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: merge
        first  = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next  = second
            second.next = tmp1

            first  = tmp1
            second = tmp2


# ── 4. EXAMPLE ───────────────────────────────────────────────
# [1, 2, 3, 4, 5]
#
# Step 1 (find middle):
#   1 → 2 → 3 | 4 → 5
#
# Step 2 (reverse second half):
#   1 → 2 → 3 | 5 → 4
#
# Step 3 (merge):
#   1 → 5 → 2 → 4 → 3


# ── 5. CRITICAL DETAILS ──────────────────────────────────────
# 1. slow.next = None
#      Cuts the list
#      If you forget → cycle / infinite loop ❌
#
# 2. Reverse starts from slow.next
#      Not from slow
#
# 3. Merge carefully — order matters:
#      first.next  = second
#      second.next = old_first_next


# ── 6. PATTERN EXTRACTION ────────────────────────────────────
# Step            Pattern
# ──────────────────────────────────
# Find middle  →  fast–slow
# Reverse half →  in-place reversal
# Merge        →  two-pointer weaving


# ── 7. CONNECTION TO PREVIOUS PROBLEMS ───────────────────────
# Problem           Same Steps
# ──────────────────────────────
# Middle of LL   →  Step 1
# Palindrome LL  →  Step 1 + 2
# Reorder List   →  Step 1 + 2 + 3


# ── 8. FINAL MENTAL MODEL ────────────────────────────────────
# Split → Reverse → Interleave


# ── 9. TEST CASES ────────────────────────────────────────────
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

# Odd length
head = build([1, 2, 3, 4, 5])
sol.reorderList(head)
print(to_list(head))    # [1, 5, 2, 4, 3]

# Even length
head = build([1, 2, 3, 4])
sol.reorderList(head)
print(to_list(head))    # [1, 4, 2, 3]

# Two nodes
head = build([1, 2])
sol.reorderList(head)
print(to_list(head))    # [1, 2]

# Single node
head = build([1])
sol.reorderList(head)
print(to_list(head))    # [1]
