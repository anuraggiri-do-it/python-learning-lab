# ─────────────────────────────────────────────────────────────
# LC 442 - Find All Duplicate Numbers (Easy)
# ─────────────────────────────────────────────────────────────
# PROBLEM: Array of n numbers in range [1, n], each appears once or twice.
#          Return ALL duplicates.
#
# IDENTIFY: range [1, n], collect all misplaced after sort
#
# DIFFERENCE FROM find_duplicate (LC 287):
#   LC 287 → one duplicate, return it
#   This   → multiple duplicates, collect all
#   Code is identical except we collect ALL wrong-index values
#
# After sort → nums[i] != i+1 means nums[i] is a duplicate
# (it tried to go home but home was already taken by itself)
#
# TIME: O(n)  SPACE: O(1) excluding output

def find_all_duplicates(nums):
    i = 0
    while i < len(nums):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    duplicates = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicates.append(nums[i])

    return duplicates


print(find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # [2, 3]
print(find_all_duplicates([1, 1, 2]))                  # [1]
print(find_all_duplicates([1, 2, 3]))                  # []
