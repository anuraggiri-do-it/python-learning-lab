# ─────────────────────────────────────────────────────────────
# Cyclic Sort (Easy)
# ─────────────────────────────────────────────────────────────
# PROBLEM: Given array with numbers in range [1, n], sort in O(n).
#
# IDENTIFY: numbers in range [1,n] → each number has a known home
#           → no need to compare → just place each at correct index
#
# TEMPLATE (memorize this):
#   correct = nums[i] - 1        ← where nums[i] BELONGS
#   if nums[i] != nums[correct]  ← not home yet → swap
#   else                         ← home → move forward
#
# WHY i doesn't increment on swap?
#   After swap, new nums[i] might also be out of place.
#   Only move i when current position is confirmed correct.
#
# TIME: O(n)  SPACE: O(1)

def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    return nums


print(cyclic_sort([3, 1, 5, 4, 2]))    # [1, 2, 3, 4, 5]
print(cyclic_sort([2, 6, 4, 3, 1, 5])) # [1, 2, 3, 4, 5, 6]
print(cyclic_sort([1, 5, 6, 4, 3, 2])) # [1, 2, 3, 4, 5, 6]
