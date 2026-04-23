# Remove Adjacent Duplicates
#
# PROBLEM: Given string, remove all adjacent duplicate characters repeatedly
#          until no adjacent duplicates remain.
#
# PATTERN: Stack
#   push char if stack top != current char
#   else pop (remove the duplicate pair)
#
# ANALOGY: Bubble wrap popping 🫧
#   Two same bubbles side by side → they pop together
#   Keep popping until no adjacent pair remains

def remove_adjacent_duplicates(s):
    stack = []

    for char in s:
        if len(stack) > 0 and stack[-1] == char:
            stack.pop()       # duplicate found → remove both
        else:
            stack.append(char)

    return ''.join(stack)


print(remove_adjacent_duplicates("abbaca"))   # "ca"
print(remove_adjacent_duplicates("azxxzy"))   # "ay"
print(remove_adjacent_duplicates("aabbcc"))   # ""
