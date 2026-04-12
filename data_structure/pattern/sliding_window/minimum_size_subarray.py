# ─────────────────────────────────────────────────────────────────────────────
# PROBLEM: Minimum Size Subarray Sum
# ─────────────────────────────────────────────────────────────────────────────
# Given an array of positive integers and a target value,
# find the MINIMUM LENGTH of a subarray whose sum >= target.
# Return 0 if no such subarray exists.
#
# Example:
#   nums = [2, 3, 1, 2, 4, 3],  target = 7
#   Answer = 2  →  subarray [4, 3]
# ─────────────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# APPROACH 1: Brute Force
# ─────────────────────────────────────────────────────────────────────────────
# WHY: Try every possible subarray, check if sum >= target, track minimum length
# HOW: Two nested loops — outer picks start, inner picks end
#
# Time  : O(n²)  → two nested loops over n elements
# Space : O(1)   → no extra data structure used
# ─────────────────────────────────────────────────────────────────────────────

def minSubArrayLen_brute(target: int, nums: list[int]) -> int:
    n = len(nums)
    min_len = float('inf')

    for start in range(n):              # try every start index
        total = 0
        for end in range(start, n):     # expand end until sum >= target
            total += nums[end]
            if total >= target:
                min_len = min(min_len, end - start + 1)
                break                   # no need to go further, already found

    return min_len if min_len != float('inf') else 0


# ─────────────────────────────────────────────────────────────────────────────
# APPROACH 2: Sliding Window  ✅ OPTIMAL
# ─────────────────────────────────────────────────────────────────────────────
# WHY: Instead of recomputing sum from scratch every time,
#      we EXPAND the window by moving `high` right (add element)
#      and SHRINK the window by moving `low` right (remove element)
#      This avoids repeated work → O(n) instead of O(n²)
#
# VISUAL:
#   nums = [2, 3, 1, 2, 4, 3],  target = 7
#
#   high→  [2]              sum=2  < 7  → expand
#   high→  [2,3]            sum=5  < 7  → expand
#   high→  [2,3,1]          sum=6  < 7  → expand
#   high→  [2,3,1,2]        sum=8  ≥ 7  → length=4, shrink from low
#          [3,1,2]          sum=6  < 7  → expand
#   high→  [3,1,2,4]        sum=10 ≥ 7  → length=4, shrink
#          [1,2,4]          sum=7  ≥ 7  → length=3, shrink
#          [2,4]            sum=6  < 7  → expand
#   high→  [2,4,3]          sum=9  ≥ 7  → length=3, shrink
#          [4,3]            sum=7  ≥ 7  → length=2 ✅ shrink
#          [3]              sum=3  < 7  → done
#
# Time  : O(n)  → each element is added once and removed once
# Space : O(1)  → only 3 variables used
# ─────────────────────────────────────────────────────────────────────────────

def minSubArrayLen(target: int, nums: list[int]) -> int:
    if not nums or target <= 0:
        return 0

    low = 0                     # left boundary of window
    current_sum = 0             # sum of current window
    min_length = float('inf')   # track smallest valid window

    for high in range(len(nums)):
        current_sum += nums[high]       # EXPAND: add right element

        while current_sum >= target:    # window is valid → try to shrink
            min_length = min(min_length, high - low + 1)  # update answer
            current_sum -= nums[low]    # SHRINK: remove left element
            low += 1                    # move left boundary right

    return min_length if min_length != float('inf') else 0
    # WHY float('inf')? → if no valid window found, inf stays unchanged
    # returning 0 means "no answer exists"


# ─────────────────────────────────────────────────────────────────────────────
# COMPLEXITY SUMMARY
# ─────────────────────────────────────────────────────────────────────────────
# Approach        Time    Space   Notes
# ─────────────────────────────────────────────────────────────────────────────
# Brute Force     O(n²)   O(1)    simple but slow for large input
# Sliding Window  O(n)    O(1)    optimal — each element touched at most twice
# ─────────────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    #              target  nums                  expected   why
    print(minSubArrayLen(7,  [2, 3, 1, 2, 4, 3]))  # 2  → [4,3] is shortest
    print(minSubArrayLen(4,  [1, 4, 4]))            # 1  → [4] alone meets target
    print(minSubArrayLen(11, [1, 1, 1, 1, 1]))      # 0  → max sum=5, never reaches 11
    print(minSubArrayLen(15, [1, 2, 3, 4, 5]))      # 5  → need entire array (sum=15)
    print(minSubArrayLen(7,  []))                   # 0  → empty array, no subarray

    print("--- brute force ---")
    print(minSubArrayLen_brute(7,  [2, 3, 1, 2, 4, 3]))  # 2
    print(minSubArrayLen_brute(4,  [1, 4, 4]))            # 1
    print(minSubArrayLen_brute(11, [1, 1, 1, 1, 1]))      # 0
