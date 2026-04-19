# LC 442 - Find All Duplicates in an Array
#
# PROBLEM: Array of n numbers in range [1, n], each appears once or twice.
#          Return all duplicates.
#
# SAME template as find_duplicate but collect ALL wrong-index numbers

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
            duplicates.append(nums[i])   # number sitting at wrong index → duplicate

    return duplicates


print(find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # [2, 3]
print(find_all_duplicates([1, 1, 2]))                  # [1]
