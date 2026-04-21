# LC 645 - Set Mismatch
#
# PROBLEM: Array of n numbers in range [1, n], one number duplicated
#          (causing one number to be missing). Return [duplicate, missing].
#
# COMBINES both problems:
#   duplicate → nums[i] != i+1 AND nums[i] is the value sitting there
#   missing   → the index i+1 that has wrong number

def find_duplicate_and_missing(nums):
    i = 0
    while i < len(nums):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicate = nums[i]   # value sitting at wrong index
            missing   = i + 1     # value that should be here
            return [duplicate, missing]

    return [-1, -1]


print(find_duplicate_and_missing([1, 2, 2, 4]))   # [2, 3]
print(find_duplicate_and_missing([3, 1, 2, 5, 2]))# [2, 4]  (wait: let's trace)
print(find_duplicate_and_missing([1, 2, 3, 3, 5]))# [3, 4]
