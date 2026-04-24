# LC 496 - Next Greater Element I (Easy)
#
# PROBLEM: nums1 is a subset of nums2. For each element in nums1,
#          find the next greater element to its RIGHT in nums2.
#          Return -1 if none exists.
#
# PATTERN: Monotonic Decreasing Stack
#   Traverse nums2, maintain stack of elements waiting for NGE.
#   When current num > stack top → stack top found its NGE.
#
# ANALOGY: People in a queue waiting for someone taller 🧍
#   Each person waits. When a taller person arrives →
#   all shorter people behind them get their answer.

def next_greater_element(nums1, nums2):
    stack   = []
    nge_map = {}   # num → next greater element

    for num in nums2:
        while len(stack) > 0 and num > stack[-1]:
            smaller = stack.pop()
            nge_map[smaller] = num   # num is NGE for smaller
        stack.append(num)

    while len(stack) > 0:
        nge_map[stack.pop()] = -1   # no NGE found

    return [nge_map[n] for n in nums1]


print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))   # [-1, 3, -1]
print(next_greater_element([2, 4], [1, 2, 3, 4]))       # [3, -1]
