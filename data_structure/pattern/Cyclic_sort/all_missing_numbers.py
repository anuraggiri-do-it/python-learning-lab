# LC 448 - Find All Numbers Disappeared in an Array
#
# PROBLEM: Array of n numbers in range [1, n], some appear twice,
#          some missing. Return all missing numbers.
#
# SAME AS base cyclic sort (range [1,n])
# After sort → every index where nums[i] != i+1 → i+1 is missing

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
