# LC 26 - Remove Duplicates from Sorted Array
#
# PROBLEM: Given sorted array, remove duplicates IN-PLACE.
#          Return length of unique elements.
#          (Don't allocate extra array — O(1) space)
#
# APPROACH: Same-direction two pointer
#   slow = 0  → tracks position of last unique element
#   fast = 1  → scans ahead looking for new unique values
#
#   if nums[fast] != nums[slow] → new unique found
#       slow += 1
#       nums[slow] = nums[fast]  → place it after last unique
#   else → duplicate → just move fast forward
#
# ANALOGY: Two workers on a conveyor belt 🏭
#   fast worker picks up items one by one
#   slow worker only accepts NEW items, ignores repeats

def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:   # new unique value found
            slow += 1
            nums[slow] = nums[fast]    # place it right after last unique

    return slow + 1                    # length = index + 1


nums = [1, 1, 2]
k = remove_duplicates(nums)
print(k, nums[:k])                     # 2 [1, 2]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = remove_duplicates(nums)
print(k, nums[:k])                     # 5 [0, 1, 2, 3, 4]
