# LC 15 - Three Sum
#
# PROBLEM: Given array, find all unique triplets that sum to 0.
#          No duplicate triplets in result.
#
# BRUTE FORCE: O(n³) — three nested loops
# TWO POINTER: O(n²) — sort + fix one element + two pointer on rest
#
# APPROACH:
#   Sort the array first
#   Fix nums[i] as first element (loop i from 0 to n-2)
#   Use two pointer on nums[i+1 .. n-1] to find pair = -nums[i]
#   Skip duplicates at every level to avoid duplicate triplets
#
# DUPLICATE SKIPPING:
#   After fixing i → skip if nums[i] == nums[i-1]
#   After finding triplet → skip duplicate left values
#                         → skip duplicate right values

def three_sum(nums):
    nums.sort()
    result = []
    n      = len(nums)

    for i in range(n - 2):
        # skip duplicate values for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # early exit — smallest possible sum already > 0
        if nums[i] > 0:
            break

        left  = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # skip duplicates for left and right
                while left < right and nums[left]  == nums[left  + 1]: left  += 1
                while left < right and nums[right] == nums[right - 1]: right -= 1

                left  += 1
                right -= 1

            elif total < 0:
                left  += 1      # need larger sum
            else:
                right -= 1      # need smaller sum

    return result


print(three_sum([-1, 0, 1, 2, -1, -4]))   # [[-1,-1,2],[-1,0,1]]
print(three_sum([0, 1, 1]))               # []
print(three_sum([0, 0, 0]))               # [[0,0,0]]
print(three_sum([-2, 0, 1, 1, 2]))        # [[-2,0,2],[-2,1,1]]
