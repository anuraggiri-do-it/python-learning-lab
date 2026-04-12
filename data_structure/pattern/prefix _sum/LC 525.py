# 525. Contiguous Array 

##-questiion:- Given a binary array nums,
# return the maximum length of a contiguous subarray
# with an equal number of 0 and 1.

# mean of the question is - there  will be  array of nums  that have the  number in it is binary
# and we have to find the length of the longest subarray that have equal number of 0 and 1
##-example:- Input: nums = [0,1]
## Example 1:

#Input: nums = [0,1]
#Output: 2
#Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

# what if there is no equal no of 0 and 1 ?

# Example 2:
#Input: nums = [0,1,0]
#Output: 2
#Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with an equal number of 0 and 1. 

# ─────────────────────────────────────────────────────────────
# ANSWER
# ─────────────────────────────────────────────────────────────

# INTUITION:
# Treat every 0 as -1 and every 1 as +1.
# Now "equal number of 0s and 1s" becomes "subarray sum = 0".
#
# Compute a running prefix_sum as we scan left to right.
# If the same prefix_sum appears at index i and later at index j,
# the subarray nums[i+1 .. j] has sum 0  →  equal 0s and 1s.
# Length = j - i.
#
# Store the FIRST time each prefix_sum is seen in a hash map.
# If we see it again, compute the length and update the answer.
#
# Answer to "what if there is no equal no of 0 and 1?":
# The hash map will never find a repeated prefix_sum (other than
# the initial 0 at index -1), so max_len stays 0 and we return 0.

# APPROACH — Prefix Sum + Hash Map
# Time  : O(n)
# Space : O(n)

# STEP-BY-STEP DRY RUN on [0, 1, 0]:
#  treat 0→-1, 1→+1  →  [-1, +1, -1]
#
#  index  value  prefix_sum  seen map              max_len
#  start    —        0       {0: -1}                 0
#    0      -1       -1      {0:-1, -1:0}             0
#    1      +1        0      {0:-1, -1:0}         0-(-1)=2  ← prefix_sum 0 seen before at -1
#    2      -1       -1      {0:-1, -1:0}         max(2, 2-0)=2  ← prefix_sum -1 seen before at 0
#
#  Answer: 2  ✓

def findMaxLength(nums: list) -> int:
    # map prefix_sum → first index it was seen
    seen = {0: -1}   # prefix_sum 0 exists before the array starts (index -1)
    prefix_sum = 0
    max_len = 0

    for i, num in enumerate(nums):
        prefix_sum += 1 if num == 1 else -1   # treat 0 as -1

        if prefix_sum in seen:
            max_len = max(max_len, i - seen[prefix_sum])
        else:
            seen[prefix_sum] = i   # store only the FIRST occurrence

    return max_len


# ── TEST CASES ───────────────────────────────────────────────
if __name__ == "__main__":
    print(findMaxLength([0, 1]))          # 2
    print(findMaxLength([0, 1, 0]))       # 2
    print(findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))  # 6
    print(findMaxLength([0, 0, 0]))       # 0  (no equal pair exists)
    print(findMaxLength([1, 1, 0, 1, 1, 0, 0]))     # 6
