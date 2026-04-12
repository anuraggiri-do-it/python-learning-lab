# LC 141 - Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Pattern: Slow & Fast Pointer (Floyd's Cycle Detection)
#
# Problem:
#   Given head of a linked list, return True if it has a cycle, else False.
#   A cycle exists if some node's next pointer points back to a previous node.
#
# Intuition:
#   Think of two runners on a circular track — the faster one will always lap the slower one.
#   - slow moves 1 step at a time
#   - fast moves 2 steps at a time
#   If a cycle exists → fast will eventually catch up to slow (they meet).
#   If no cycle     → fast reaches None (end of list).
#
# Why `is` and not `==`?
#   `is` checks object identity (same node in memory).
#   `==` checks value equality — two different nodes can have the same val, giving false positives.
#
# Time:  O(n) — fast pointer traverses at most 2n steps before meeting slow or hitting None
# Space: O(1) — no extra data structures, just two pointers

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def build_list(values: list, pos: int) -> Optional[ListNode]:
    """
    Build a linked list from values.
    pos: index of the node that tail connects to (-1 means no cycle).
    """
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]   # create cycle
    return nodes[0]


def run_test(values: list, pos: int, expected: bool, label: str):
    head = build_list(values, pos)
    result = Solution().hasCycle(head)
    status = "PASS" if result == expected else "FAIL"
    print(f"[{status}] {label} → {result}")


# ---------------------------------------------------------------------------
# Test Cases
# ---------------------------------------------------------------------------

# 1. Classic cycle: tail → index 1  →  3 → 2 → 0 → 4 → (back to 2)
run_test([3, 2, 0, -4], pos=1, expected=True,  label="cycle at pos 1")

# 2. Two-node cycle: tail → head
run_test([1, 2],        pos=0, expected=True,  label="two nodes, cycle at pos 0")

# 3. Single node, no cycle
run_test([1],           pos=-1, expected=False, label="single node, no cycle")

# 4. Empty list
run_test([],            pos=-1, expected=False, label="empty list")

# 5. Long list, no cycle
run_test([1, 2, 3, 4, 5], pos=-1, expected=False, label="5 nodes, no cycle")

# 6. Cycle back to head
run_test([1, 2, 3, 4],    pos=0,  expected=True,  label="cycle back to head")

# 7. Self-loop (single node pointing to itself)
node = ListNode(1)
node.next = node
result = Solution().hasCycle(node)
print(f"[{'PASS' if result else 'FAIL'}] self-loop → {result}")
