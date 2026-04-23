# Balanced Parentheses
# LC 20 - Valid Parentheses
#
# PROBLEM: Given string of brackets (){}[], return True if balanced.
#
# PATTERN: Stack - matching pairs
#   push every open bracket
#   on close bracket → top must be its matching open
#   end → stack must be empty (every open was closed)
#
# ANALOGY: Nesting dolls 🪆
#   Every open doll must close in reverse order of opening.
#   Last opened → first closed → LIFO → stack

def is_balanced(s):
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


print(is_balanced("()[]{}"))   # True
print(is_balanced("([{}])"))   # True
print(is_balanced("(]"))       # False
print(is_balanced("([)]"))     # False
print(is_balanced("{[]"))      # False
