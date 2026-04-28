# ─────────────────────────────────────────────────────────────
# Problem Challenge 2 - Find the Smallest Missing Positive Number (Medium)
# LC 41 - First Missing Positive
# ─────────────────────────────────────────────────────────────
# PROBLEM: Unsorted array with ANY integers (negatives, zeros, huge numbers).
#          Find the smallest missing POSITIVE integer.
#          O(n) time, O(1) space.
#
# IDENTIFY: find missing positive → cyclic sort but ignore out-of-range values
#
# DIFFERENCE FROM all previous cyclic sort problems:
#   All previous → clean range [1,n] or [0,n], no negatives/zeros
#   This         → ANY integers → must IGNORE values outside [1, n]
#                  only numbers in [1, n] can be placed at correct index
#
# WHY answer is always in [1, n+1]?
#   Array has n slots. Best case: holds exactly [1..n] → answer = n+1.
#   Any gap in [1..n] → answer is smaller. So search space = [1, n+1].
#
# APPROACH:
#   Cyclic sort, skip anything outside [1, n]
#   After sort → first index where nums[i] != i+1 → return i+1
#
# TIME: O(n)  SPACE: O(1)

def first_missing_positive(nums):
    n = len(nums)
    i = 0

    while i < n:
        correct = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1   # out of range [1,n] or already correct → skip

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1   # all [1, n] present → answer is n+1


print(first_missing_positive([1, 2, 0]))         # 3
print(first_missing_positive([3, 4, -1, 1]))     # 2
print(first_missing_positive([7, 8, 9, 11, 12])) # 1
print(first_missing_positive([1, 2, 3]))         # 4
