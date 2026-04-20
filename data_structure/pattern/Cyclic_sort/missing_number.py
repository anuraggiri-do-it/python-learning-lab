# LC 268 - Missing Number
#
# PROBLEM: Array of n numbers in range [0, n], one number missing, find it.
#
# DIFFERENCE FROM BASE:
#   Range is [0, n] not [1, n]
#   → correct index = nums[i] (not nums[i]-1)
#   → skip if nums[i] == n (n has no valid index in size-n array)
#
# After sort → scan for index where nums[i] != i → that i is missing

def missing_number(nums):
    i = 0
    n = len(nums)

    while i < n:
        correct = nums[i]                        # nums[i] belongs at index nums[i]
        if nums[i] < n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    # scan for the missing index
    for i in range(n):
        if nums[i] != i:
            return i

    return n   # if all [0,n-1] are present → n is missing


print(missing_number([4, 0, 3, 1]))   # 2
print(missing_number([8,3,5,2,4,6,0,1]))  # 7
print(missing_number([0, 1]))         # 2
