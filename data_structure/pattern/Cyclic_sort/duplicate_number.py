# ─────────────────────────────────────────────────────────────
# LC 287 - Find the Duplicate Number (Easy via Cyclic Sort)
# ─────────────────────────────────────────────────────────────
# PROBLEM: Array of n+1 numbers in range [1, n], one number appears twice.
#          Find the duplicate.
#
# IDENTIFY: range [1, n] with one extra → cyclic sort, find misplaced
#
# KEY INSIGHT:
#   After cyclic sort → every number should be at index nums[i]-1.
#   If nums[i] != i+1 → this number is a duplicate
#   (it couldn't go home because its home was already taken by itself)
#
# NOTE: LC 287 says don't modify array → use slow/fast pointer instead.
#       This cyclic sort version modifies the array (educative variant).
#
# TIME: O(n)  SPACE: O(1)

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
            return nums[i]

    return -1


print(find_duplicate([1, 4, 4, 3, 2]))    # 4
print(find_duplicate([2, 1, 3, 3, 5, 4])) # 3
print(find_duplicate([2, 4, 1, 4, 4]))    # 4
