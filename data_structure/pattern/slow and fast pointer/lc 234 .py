# 234. Palindrome Linked List\

#This problem combines two patterns you’ve already seen:

#*Find middle (fast–slow)
#*Reverse a linked list

#*The constraint O(1) space rules out arrays/stacks.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    #1. Find middle
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

     
    #2. Reverse second half
    prev = None
    curr = slow

    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    #3. Compare first and second half
    first_half = head
    second_half = prev
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    return True

# 🧠 Key takeaway
# 🚨 When you see "palindrome", think "reverse second half
# This is a pattern-composition problem:
#Middle + Reverse + Compare
