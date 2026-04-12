# LC 560 - Subarray Sum Equals K
# prefix_sum[j] - prefix_sum[i] = k  →  prefix_sum[i] = prefix_sum[j] - k

def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    seen = {0: 1}  # prefix_sum 0 seen once

    for n in nums:
        prefix_sum += n
        count += seen.get(prefix_sum - k, 0)
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count


# Test
print(subarraySum([1, 1, 1], 2))        # 2
print(subarraySum([1, 2, 3], 3))        # 2
print(subarraySum([1, 2, 1, 2, 1], 3)) # 4
