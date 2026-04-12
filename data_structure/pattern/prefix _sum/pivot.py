# LC 724 - Find Pivot Index
# Pivot index: left sum == right sum
# right sum = total - left_sum - nums[i]

def pivotIndex(nums):
    total = sum(nums)
    left_sum = 0

    for i, n in enumerate(nums):
        # right_sum = total - left_sum - nums[i]
        if left_sum == total - left_sum - n:
            return i
        left_sum += n

    return -1


# Test
print(pivotIndex([1, 7, 3, 6, 5, 6]))  # 3
print(pivotIndex([1, 2, 3]))            # -1
print(pivotIndex([2, 1, -1]))           # 0
