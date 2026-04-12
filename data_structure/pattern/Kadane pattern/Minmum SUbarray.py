def minSubarray(nums):
    min_sum = [0]
    for i in range(len(nums)):
        min_sum.append(min(min_sum[-1] + nums[i], nums[i]))
    return min(min_sum[1:])

# Example usage
nums = [1, -2, 3, -4, 5]
result = minSubarray(nums)
print("Minimum subarray sum:", result)
