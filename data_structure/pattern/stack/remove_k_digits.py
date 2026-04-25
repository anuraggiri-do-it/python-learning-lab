# LC 402 - Remove K Digits (Hard - Problem Challenge)
#
# PROBLEM: Given string number and integer k, remove k digits to make
#          the resulting number as SMALL as possible. Return as string.
#
# PATTERN: Monotonic Increasing Stack (Greedy)
#   To minimize the number → remove larger digits that appear
#   BEFORE smaller digits (they make the number bigger).
#
#   Keep a monotonic increasing stack:
#   When current digit < stack top → pop top (remove that larger digit)
#   This greedy choice always gives the smallest result.
#
# ANALOGY: Trimming a price tag 🏷️
#   Number "1432219", remove 3 digits.
#   "1432219" → see 4, then 3 → 3 < 4 → remove 4 → "132219"
#   "132219"  → see 2 → 2 < 3 → remove 3 → "12219"
#   "12219"   → see 1 → already increasing → remove last → "1219"
#   Result = "1219" (smallest possible)
#
# EDGE CASES:
#   Leading zeros → strip them
#   k still > 0 after loop → remove from end (already increasing)
#   result empty → return "0"

def remove_k_digits(num, k):
    stack = []

    for digit in num:
        # pop larger digits before current smaller digit
        while k > 0 and len(stack) > 0 and digit < stack[-1]:
            stack.pop()
            k -= 1
        stack.append(digit)

    # if k still remaining → remove from end (stack is increasing)
    if k > 0:
        stack = stack[:-k]

    # join and strip leading zeros
    result = ''.join(stack).lstrip('0')

    return result if result else '0'


print(remove_k_digits("1432219", 3))   # "1219"
print(remove_k_digits("10200", 1))     # "200"  → strip leading 0 → "200"
print(remove_k_digits("10", 2))        # "0"
print(remove_k_digits("9", 1))         # "0"
print(remove_k_digits("112", 1))       # "11"
