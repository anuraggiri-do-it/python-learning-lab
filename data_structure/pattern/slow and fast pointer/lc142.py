# LC 142 — Linked List Cycle II
# Pattern: Fast & Slow Pointer (two-phase)
# Goal: Return the node where the cycle begins, or None

# ─── Why it works ───────────────────────────────────────────────
# Let L = head → cycle start
#     x = cycle start → meeting point
#
# At meeting point:
#   fast traveled = 2 × slow
#   → L + x = kC
#
# So: reset slow to head, move both 1 step
# → they meet exactly at cycle start
# ────────────────────────────────────────────────────────────────

# Common mistakes:
#   ❌ Returning True/False instead of node
#   ❌ Skipping phase 2
#   ❌ Moving fast faster than slow in phase 2 (both must be 1 step)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectCycle(head: ListNode) -> ListNode:
    slow = fast = head

    # Phase 1: detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None  # no cycle

    # Phase 2: find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # cycle entry node


# ─── Test Cases ─────────────────────────────────────────────────

def build_list_with_cycle(values, cycle_index):
    """Build linked list; cycle_index = -1 means no cycle."""
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_index != -1:
        nodes[-1].next = nodes[cycle_index]
    return nodes[0], nodes[cycle_index] if cycle_index != -1 else None


# TC1: cycle starts at index 1 → [3→1→2→4→(back to 1)]
head, expected = build_list_with_cycle([3, 1, 2, 4], 1)
assert detectCycle(head) is expected, "TC1 failed"

# TC2: cycle starts at index 0 (full cycle) → [1→2→(back to 1)]
head, expected = build_list_with_cycle([1, 2], 0)
assert detectCycle(head) is expected, "TC2 failed"

# TC3: no cycle → [1→2→3]
head, _ = build_list_with_cycle([1, 2, 3], -1)
assert detectCycle(head) is None, "TC3 failed"

# TC4: single node, no cycle
head, _ = build_list_with_cycle([1], -1)
assert detectCycle(head) is None, "TC4 failed"

# TC5: single node pointing to itself
head, expected = build_list_with_cycle([1], 0)
assert detectCycle(head) is expected, "TC5 failed"

# TC6: cycle at last node → [1→2→3→4→(back to 3)]
head, expected = build_list_with_cycle([1, 2, 3, 4], 2)
assert detectCycle(head) is expected, "TC6 failed"

print("All test cases passed ✅")
