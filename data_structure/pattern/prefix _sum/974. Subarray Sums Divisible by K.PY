# LC 974 - Subarray Sums Divisible by K
# ─────────────────────────────────────────────────────────────────────────────
# PROBLEM:
#   Given an integer array nums and integer k, return the number of
#   non-empty subarrays whose sum is divisible by k.
#
# CORE INSIGHT (Prefix Sum + Modulo):
#   sum(i..j) = prefix[j] - prefix[i-1]
#   For sum(i..j) % k == 0:
#       (prefix[j] - prefix[i-1]) % k == 0
#       →  prefix[j] % k == prefix[i-1] % k
#
#   So: count pairs where two prefix sums share the same remainder mod k.
#
# WHY STORE REMAINDERS?
#   If we've seen remainder `r` appear `c` times before index j,
#   then there are `c` subarrays ending at j with sum divisible by k.
#
# PYTHON MODULO NOTE:
#   Python's % always returns non-negative for positive k,
#   so no need to handle negative remainders manually.
#   e.g. -1 % 5 = 4  ✓  (unlike C/Java where it would be -1)
#
# TIME:  O(n)
# SPACE: O(k)  — at most k distinct remainders (0 to k-1)
# ─────────────────────────────────────────────────────────────────────────────

def subarraysDivByK(nums, k):
    count = 0
    prefix_rem = 0
    rem_freq = {0: 1}   # remainder 0 seen once (empty prefix)

    for n in nums:
        prefix_rem = (prefix_rem + n) % k
        count += rem_freq.get(prefix_rem, 0)   # subarrays ending here divisible by k
        rem_freq[prefix_rem] = rem_freq.get(prefix_rem, 0) + 1

    return count


# ─────────────────────────────────────────────────────────────────────────────
# DRY RUN: nums = [4, 5, 0, -2, -3, 1], k = 5
#
#  i  | n  | prefix_rem | rem_freq                    | count
# ────|────|────────────|─────────────────────────────|──────
#  -  | -  |     0      | {0:1}                       |  0
#  0  | 4  |     4      | {0:1, 4:1}                  |  0
#  1  | 5  |     4      | {0:1, 4:2}                  |  1   ← rem 4 seen once before
#  2  | 0  |     4      | {0:1, 4:3}                  |  3   ← rem 4 seen twice before
#  3  | -2 |     2      | {0:1, 4:3, 2:1}             |  3
#  4  | -3 |     4      | {0:1, 4:4, 2:1}             |  6   ← rem 4 seen 3 times before
#  5  | 1  |     0      | {0:2, 4:4, 2:1}             |  7   ← rem 0 seen once before
#
# Answer: 7  ✓
# ─────────────────────────────────────────────────────────────────────────────

# Tests
print(subarraysDivByK([4, 5, 0, -2, -3, 1], 5))  # 7
print(subarraysDivByK([5], 9))                     # 0
print(subarraysDivByK([5], 5))                     # 1
print(subarraysDivByK([2, -2, 2, -2], 2))          # 10
