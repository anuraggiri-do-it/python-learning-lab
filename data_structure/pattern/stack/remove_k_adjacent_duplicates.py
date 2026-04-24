# LC 1209 - Remove All Adjacent Duplicates in String II (Medium)
#
# PROBLEM: Given string s and integer k, remove k adjacent duplicate
#          characters repeatedly until no k-adjacent duplicates remain.
#
# DIFFERENCE FROM EASY VERSION (remove pairs):
#   Easy  → remove exactly 2 adjacent same chars
#   This  → remove exactly K adjacent same chars
#           need to TRACK COUNT of consecutive chars → stack of [char, count]
#
# PATTERN: Stack storing [char, count] pairs
#   push [char, 1] if top char != current
#   if top char == current → increment count
#   if count == k → pop (k duplicates found → remove them)
#
# ANALOGY: Jenga blocks 🧱
#   Stack k same-colored blocks → they collapse together.
#   Keep stacking until k reached → remove entire group.

def remove_k_duplicates(s, k):
    stack = []   # [char, count]

    for char in s:
        if len(stack) > 0 and stack[-1][0] == char:
            stack[-1][1] += 1          # same char → increment count
            if stack[-1][1] == k:
                stack.pop()            # k reached → remove group
        else:
            stack.append([char, 1])    # new char → push with count 1

    # rebuild string: each [char, count] → char * count
    result = []
    for char, count in stack:
        result.append(char * count)

    return ''.join(result)


print(remove_k_duplicates("abcd", 2))          # "abcd"  (no k duplicates)
print(remove_k_duplicates("deeedbbcccbdaa", 3))# "aa"
print(remove_k_duplicates("pbbcggttciiippooaais", 2))  # "ps"
