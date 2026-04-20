# LC 41 - First Missing Positive (Hard)
#
# PROBLEM: Unsorted array with any integers (negatives, zeros, large numbers).
#          Find the smallest missing POSITIVE integer. O(n) time, O(1) space.
#
# DIFFERENCE FROM OTHER CYCLIC SORT PROBLEMS:
# ─────────────────────────────────────────────────────────────────
# All previous → range is clean [1,n] or [0,n], no negatives/zeros
# This one     → array has ANY integers, negatives, zeros, huge nums
#                → only care about range [1, n] (answer must be in [1, n+1])
#                → ignore anything outside [1, n] during sort
# ─────────────────────────────────────────────────────────────────
#
# WHY answer is always in [1, n+1]?
#   Array has n elements. Best case all are [1,n] → missing is n+1.
#   Any gap in [1,n] → answer is smaller than n+1.
#
# APPROACH:
#   Cyclic sort but SKIP numbers outside [1, n]
#   After sort → first index where nums[i] != i+1 → return i+1

def first_missing_positive(nums):
    n = len(nums)
    i = 0

    while i < n:
        correct = nums[i] - 1                          # where nums[i] belongs
        if 1 <= nums[i] <= n and nums[i] != nums[correct]:  # valid & not in place
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1   # out of range or already correct → skip

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1   # first gap found

    return n + 1   # all [1,n] present → answer is n+1


print(first_missing_positive([1, 2, 0]))        # 3
print(first_missing_positive([3, 4, -1, 1]))    # 2
print(first_missing_positive([7, 8, 9, 11, 12]))# 1
print(first_missing_positive([1, 2, 3]))        # 4
