# ─────────────────────────────────────────────────────────────
# LC 268 - Find the Missing Number (Easy)
# ─────────────────────────────────────────────────────────────
# PROBLEM: Array of n numbers in range [0, n], one missing. Find it.
#
# IDENTIFY: range [0, n] with one gap → cyclic sort then scan
#
# DIFFERENCE FROM BASE cyclic sort:
#   Base  → range [1, n] → correct index = nums[i] - 1
#   This  → range [0, n] → correct index = nums[i]
#           n itself has no valid index (array size is n) → skip it
#
# After sort → first index where nums[i] != i → that i is missing
# If all match → n is missing (it was never placed)
#
# TIME: O(n)  SPACE: O(1)

def missing_number(nums):
    i = 0
    n = len(nums)

    while i < n:
        correct = nums[i]
        if nums[i] < n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i

    return n   # all [0, n-1] present → n is missing


print(missing_number([4, 0, 3, 1]))        # 2
print(missing_number([8, 3, 5, 2, 4, 6, 0, 1]))  # 7
print(missing_number([0, 1]))              # 2
