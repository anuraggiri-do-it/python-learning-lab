# LC 53. Maximum Subarray
# LC 53. Maximum Subarray
def maxSubarray(nums):
    max_sum = nums[0]
    best = nums[0]

    for i in range(1, len(nums)):
        max_sum = max(nums[i], max_sum + nums[i])
        best = max(best, max_sum)

    return best
