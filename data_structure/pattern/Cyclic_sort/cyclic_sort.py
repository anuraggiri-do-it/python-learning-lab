# Cyclic Sort - Sort array containing [1, n]
#
# PROBLEM: Given array with numbers in range [1, n], sort in place O(n)
#
# TEMPLATE: nums[i] belongs at index nums[i]-1
#   if not there → swap it to correct index
#   if already correct → move i forward

def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct = nums[i] - 1          # nums[i] should sit at this index
        if nums[i] != nums[correct]:   # not in right place → swap
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1                     # correct place → move on
    return nums


print(cyclic_sort([3, 1, 5, 4, 2]))   # [1, 2, 3, 4, 5]
print(cyclic_sort([2, 6, 4, 3, 1, 5]))# [1, 2, 3, 4, 5, 6]
print(cyclic_sort([1, 5, 6, 4, 3, 2]))# [1, 2, 3, 4, 5, 6]
