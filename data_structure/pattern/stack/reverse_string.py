# Reverse a String using Stack
#
# PROBLEM: Reverse a string using a stack.
#
# PATTERN: Stack - LIFO reversal
#   push all chars → pop all chars
#   LIFO naturally reverses the order
#
# ANALOGY: Stack of books 📚
#   You stack books one by one (A, B, C on top)
#   Pick them back → C, B, A → reversed

def reverse_string(s):
    stack = []

    for char in s:
        stack.append(char)   # push all chars

    result = []
    while len(stack) > 0:
        result.append(stack.pop())   # pop = reverse order

    return ''.join(result)


print(reverse_string("hello"))      # "olleh"
print(reverse_string("abcde"))      # "edcba"
print(reverse_string("racecar"))    # "racecar"
