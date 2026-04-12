# ============================================================
# LC 1004. Max Consecutive Ones III
# ============================================================
# PROBLEM:
#   Given a binary array nums and an integer k,
#   return the maximum number of consecutive 1s
#   if you can flip at most k 0s.
#
# EXAMPLE:
#   nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
#   Output: 6  → flip index 9 and 10 → [1,1,1,0,0,1,1,1,1,1,1]
#
# PATTERN: Sliding Window (Variable Size)
#
# INTUITION:
#   - Expand window by moving `high` pointer right
#   - Count zeros inside the window
#   - If zeros > k → shrink window from left (move `low`)
#   - At every step track max window size
#
# TIME  : O(n) — each element visited at most twice
# SPACE : O(1) — only counters used
# ============================================================

def longestOnes(nums, k):
    low = 0       # left boundary of window
    zero = 0      # count of zeros in current window
    ans = 0       # max window size found so far

    for high in range(len(nums)):

        # expand window: if current element is 0, use one flip
        if nums[high] == 0:
            zero += 1

        # shrink window from left if flips exceeded
        while zero > k:
            if nums[low] == 0:
                zero -= 1   # give back the flip
            low += 1        # shrink window

        # valid window: update answer
        ans = max(ans, high - low + 1)

    return ans


# ── TEST CASES ──────────────────────────────────────────────
if __name__ == "__main__":
    print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # 6
    print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))  # 10
    print(longestOnes([1,1,1,1], 0))  # 4 — no zeros, no flips needed
    print(longestOnes([0,0,0], 0))    # 0 — can't flip anything
