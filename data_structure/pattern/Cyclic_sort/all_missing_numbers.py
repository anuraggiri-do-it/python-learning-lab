# ─────────────────────────────────────────────────────────────
# LC 448 - Find All Missing Numbers (Easy)
# ─────────────────────────────────────────────────────────────
# PROBLEM: Array of n numbers in range [1, n]. Some appear twice,
#          some are missing. Return ALL missing numbers.
#
# IDENTIFY: range [1, n], multiple gaps → cyclic sort then collect all gaps
#
# DIFFERENCE FROM missing_number (LC 268):
#   LC 268  → range [0, n], find ONE missing
#   This    → range [1, n], find ALL missing (duplicates cause gaps)
#
# After sort → every index where nums[i] != i+1 → i+1 is missing
# (duplicate took that slot, pushing the real number out)
#
# TIME: O(n)  SPACE: O(1) excluding output

def find_all_missing(nums):
    i = 0
    while i < len(nums):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    missing = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing.append(i + 1)

    return missing


print(find_all_missing([4, 3, 2, 7, 8, 2, 3, 1]))  # [5, 6]
print(find_all_missing([1, 1]))                     # [2]
print(find_all_missing([2, 2]))                     # [1]
