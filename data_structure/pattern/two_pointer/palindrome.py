# LC 125 - Valid Palindrome
#
# PROBLEM: Given string, return True if it is a palindrome
#          considering only alphanumeric characters, ignoring case.
#
# APPROACH: opposite ends two pointer
#   left = 0, right = n-1
#   skip non-alphanumeric characters on both sides
#   compare chars (lowercased)
#   if mismatch → not palindrome
#   if pointers cross → palindrome
#
# ANALOGY: Reading a word forward and backward 📖
#   "racecar" → r-a-c-e-c-a-r → same both ways → palindrome
#   Two people reading from each end, comparing letter by letter

def is_palindrome(s):
    left  = 0
    right = len(s) - 1

    while left < right:
        # skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1

        # skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left  += 1
        right -= 1

    return True


print(is_palindrome('A man, a plan, a canal: Panama'))  # True
print(is_palindrome('race a car'))                      # False
print(is_palindrome(' '))                               # True
print(is_palindrome('Was it a car or a cat I saw?'))    # True
print(is_palindrome('No lemon, no melon'))              # True
