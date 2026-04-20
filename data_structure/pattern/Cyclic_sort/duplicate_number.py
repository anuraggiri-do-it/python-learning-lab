# LC 287 - Find the Duplicate Number
#
# PROBLEM: Array of n+1 numbers in range [1, n], one number duplicated.
#          Find it. No extra space, don't modify array.
#
# NOTE: LC 287 restricts modifying array → use slow/fast pointer.
#       Cyclic sort version (modifies array) is the educative variant.
#
# CYCLIC SORT VERSION (modifies array):
#   After sort → index where nums[i] != i+1 → nums[i] is the duplicate
#   (because the real number for that index was displaced by duplicate)

def find_duplicate(nums):
    i = 0
    while i < len(nums):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return nums[i]   # this number is sitting at wrong index → duplicate

    return -1


print(find_duplicate([1, 4, 4, 3, 2]))   # 4
print(find_duplicate([2, 1, 3, 3, 5, 4]))# 3
print(find_duplicate([2, 4, 1, 4, 4]))   # 4
