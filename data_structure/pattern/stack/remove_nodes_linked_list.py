# LC 1474 - Remove Nodes From Linked List (Easy)
# (also known as: remove nodes with greater value to the right)
#
# PROBLEM: Given head of linked list, remove every node that has
#          a node with greater value to its right. Return modified list.
#
# PATTERN: Monotonic Decreasing Stack
#   Push nodes onto stack keeping only decreasing order.
#   When a larger node arrives → pop all smaller nodes (they get removed).
#   Rebuild list from stack (reverse = correct order).
#
# ANALOGY: Tall buildings blocking the view 🏙️
#   A shorter building gets demolished if a taller one is built to its right.
#   Only buildings that are the tallest from their position to the end survive.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

def remove_nodes(head):
    stack = []
    curr  = head

    # push all nodes, pop smaller ones when larger arrives
    while curr is not None:
        while len(stack) > 0 and curr.val > stack[-1].val:
            stack.pop()   # this node is removed (larger exists to its right)
        stack.append(curr)
        curr = curr.next

    # rebuild linked list from stack
    for i in range(len(stack) - 1):
        stack[i].next = stack[i + 1]
    stack[-1].next = None

    return stack[0]

def build_list(vals):
    dummy = ListNode(0)
    curr  = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

print_list(remove_nodes(build_list([5, 2, 13, 3, 8])))   # [13, 8]
print_list(remove_nodes(build_list([1, 1, 1, 1])))        # [1, 1, 1, 1]
