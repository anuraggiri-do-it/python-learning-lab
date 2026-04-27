# ─────────────────────────────────────────────────────────────
# Problem Challenge 1 - Find the Corrupt Pair (Easy)
# LC 645 - Set Mismatch
# ─────────────────────────────────────────────────────────────
# PROBLEM: Array of n numbers in range [1, n]. One number is duplicated
#          which causes one number to go missing.
#          Return [duplicate, missing].
#
# IDENTIFY: range [1, n], one wrong slot → find both duplicate AND missing
#
# WHY "corrupt pair"?
#   The duplicate CORRUPTED the array by stealing another number's slot.
#   That stolen slot = missing number.
#   Both always come together → that's the corrupt pair.
#
# COMBINES:
#   find_duplicate → nums[i] at wrong index = duplicate
#   find_missing   → i+1 at that wrong index = missing
#
# After sort → first index where nums[i] != i+1:
#   nums[i] = duplicate (sitting in wrong place)
#   i + 1   = missing   (should have been here)
#
# TIME: O(n)  SPACE: O(1)

def find_corrupt_pair(nums):
    i = 0
    while i < len(nums):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicate = nums[i]
            missing   = i + 1
            return [duplicate, missing]

    return [-1, -1]


print(find_corrupt_pair([3, 1, 2, 5, 2]))  # [2, 4]
print(find_corrupt_pair([3, 1, 2, 3, 6, 4]))  # [3, 5]
print(find_corrupt_pair([1, 2, 2, 4]))     # [2, 3]
