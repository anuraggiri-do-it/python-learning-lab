# ═══════════════════════════════════════════════════════════════
#                         STACK
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS A STACK?
# ─────────────────────────────────────────────────────────────
# A linear data structure that follows LIFO principle:
#   Last In → First Out
#
# ANALOGY: Stack of plates 🍽️
#   - You add a plate on TOP
#   - You remove a plate from TOP
#   - You can never remove from the middle or bottom
#   - The LAST plate placed is the FIRST one removed
#
# OPERATIONS:
#   push(x)  → add x to top         O(1)
#   pop()    → remove from top       O(1)
#   peek()   → see top without remove O(1)
#   isEmpty()→ check if empty        O(1)
#
# ─────────────────────────────────────────────────────────────
# HOW TO IDENTIFY — use stack when you see:
# ─────────────────────────────────────────────────────────────
#   ✅ "matching pairs" → brackets, tags, parentheses
#   ✅ "undo / back button" → browser history, text editor
#   ✅ "next greater / smaller element"
#   ✅ "previous greater / smaller element"
#   ✅ nested structures → HTML tags, recursive calls
#   ✅ "evaluate expression" → postfix, infix
#   ✅ need to REVERSE something
#   ✅ need to remember what you SAW BEFORE current element
#
# ─────────────────────────────────────────────────────────────
# PATTERNS THAT USE STACK:
# ─────────────────────────────────────────────────────────────
#   1. Monotonic Stack   → next/prev greater or smaller element
#   2. Valid Parentheses → matching open/close brackets
#   3. Expression Eval   → postfix/prefix evaluation
#   4. DFS iterative     → replace recursion call stack
#   5. Backtracking      → undo last step
#
# ─────────────────────────────────────────────────────────────
# MONOTONIC STACK ANALOGY: Bouncer at a club 🚪
#   Only people TALLER than you can stay behind you.
#   When someone taller arrives → shorter ones leave first.
#   Stack always stays in order (increasing or decreasing).
#
# ─────────────────────────────────────────────────────────────
# QUESTION LIST (this file):
# ─────────────────────────────────────────────────────────────
#   1. Stack implementation using list
#   2. LC 20  - Valid Parentheses
#   3. LC 155 - Min Stack
#   4. LC 739 - Daily Temperatures (monotonic stack)
#   5. LC 496 - Next Greater Element I
#   6. LC 84  - Largest Rectangle in Histogram (hard)
# ═══════════════════════════════════════════════════════════════


# ───────────────────────────────────────────────────────────────
# 1. STACK IMPLEMENTATION
# ───────────────────────────────────────────────────────────────
# Python list is a perfect stack:
#   append() → push   (add to end = top)
#   pop()    → pop    (remove from end = top)
#   [-1]     → peek   (see top)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# ───────────────────────────────────────────────────────────────
# 2. LC 20 - Valid Parentheses
# ───────────────────────────────────────────────────────────────
# PROBLEM: Given string of brackets, return True if valid.
#
# ANALOGY: Nesting dolls 🪆
#   Every open doll must be closed by the MATCHING size.
#   The LAST opened must be the FIRST closed.
#   → perfect LIFO → stack
#
# PATTERN: matching pairs
#   push open brackets
#   on close bracket → check if top matches
#   end → stack must be empty

def is_valid(s):
    stack = []
    match = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            if len(stack) == 0 or stack[-1] != match[char]:
                return False
            stack.pop()

    return len(stack) == 0


print(is_valid("()[]{}"))    # True
print(is_valid("([{}])"))    # True
print(is_valid("(]"))        # False
print(is_valid("([)]"))      # False


# ───────────────────────────────────────────────────────────────
# 3. LC 155 - Min Stack
# ───────────────────────────────────────────────────────────────
# PROBLEM: Stack that supports push, pop, top, and getMin in O(1).
#
# TRICK: Keep a second stack that tracks minimum at every level.
#   When you push → also push current min to min_stack
#   When you pop  → also pop from min_stack
#   getMin        → peek min_stack top (always current min)
#
# ANALOGY: Two stacks of plates side by side.
#   Left stack = actual values
#   Right stack = "what was the min when this plate was added"

class MinStack:
    def __init__(self):
        self.stack     = []
        self.min_stack = []   # tracks min at every state

    def push(self, val):
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            current_min = self.min_stack[-1]
            if val < current_min:
                self.min_stack.append(val)
            else:
                self.min_stack.append(current_min)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]


ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)
ms.push(2)
print(ms.get_min())   # 2
ms.pop()
print(ms.get_min())   # 3
print(ms.top())       # 7


# ───────────────────────────────────────────────────────────────
# 4. LC 739 - Daily Temperatures (Monotonic Stack)
# ───────────────────────────────────────────────────────────────
# PROBLEM: Given temperatures[], return array where result[i] =
#          how many days until a warmer temperature.
#
# PATTERN: Monotonic Decreasing Stack
#   Stack stores INDICES of temperatures seen so far.
#   Stack stays in decreasing order of temperatures.
#
# ANALOGY: People waiting in line for a taller person 🧍🧍🧍
#   Each person waits until someone taller arrives.
#   When taller person arrives → everyone shorter gets their answer.

def daily_temperatures(temps):
    stack  = []          # stores indices
    result = [0] * len(temps)

    for i in range(len(temps)):
        # while current temp is warmer than stack top → answer found
        while len(stack) > 0 and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx   # days waited = current index - that index
        stack.append(i)

    return result


print(daily_temperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(daily_temperatures([30,40,50,60]))               # [1,1,1,0]
print(daily_temperatures([30,60,90]))                  # [1,1,0]


# ───────────────────────────────────────────────────────────────
# 5. LC 496 - Next Greater Element I
# ───────────────────────────────────────────────────────────────
# PROBLEM: nums1 is subset of nums2. For each element in nums1,
#          find the next greater element in nums2. Return -1 if none.
#
# PATTERN: Monotonic stack on nums2 → build a map of next greater
#          then just look up each nums1 element in the map

def next_greater_element(nums1, nums2):
    stack    = []
    nge_map  = {}   # num → its next greater element in nums2

    for num in nums2:
        while len(stack) > 0 and num > stack[-1]:
            smaller = stack.pop()
            nge_map[smaller] = num   # num is the next greater for smaller
        stack.append(num)

    # anything left in stack has no next greater
    while len(stack) > 0:
        nge_map[stack.pop()] = -1

    return [nge_map[n] for n in nums1]


print(next_greater_element([4,1,2], [1,3,4,2]))   # [-1,3,-1]
print(next_greater_element([2,4], [1,2,3,4]))      # [3,-1]


# ───────────────────────────────────────────────────────────────
# 6. LC 84 - Largest Rectangle in Histogram (Hard)
# ───────────────────────────────────────────────────────────────
# PROBLEM: Given array of bar heights, find largest rectangle area.
#
# PATTERN: Monotonic Increasing Stack
#   Stack stores indices of bars in increasing height order.
#   When a shorter bar arrives → all taller bars behind it
#   can no longer extend right → calculate their area now.
#
# ANALOGY: Buildings blocking sunlight 🏙️
#   A shorter building blocks all taller buildings behind it
#   from extending their rectangle further right.
#   → calculate area for each blocked building immediately.
#
# area formula: height[i] * (right_boundary - left_boundary - 1)

def largest_rectangle(heights):
    stack    = []   # monotonic increasing stack of indices
    max_area = 0
    heights.append(0)   # sentinel: forces all remaining bars to be processed

    for i in range(len(heights)):
        while len(stack) > 0 and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]

            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1

            area = height * width
            if area > max_area:
                max_area = area

        stack.append(i)

    heights.pop()   # restore original array
    return max_area


print(largest_rectangle([2,1,5,6,2,3]))   # 10
print(largest_rectangle([2,4]))           # 4
print(largest_rectangle([6,2,5,4,5,1,6]))# 12
