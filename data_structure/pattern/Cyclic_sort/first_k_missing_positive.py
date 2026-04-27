# ─────────────────────────────────────────────────────────────
# Problem Challenge 3 - Find the First K Missing Positive Numbers (Hard)
# ─────────────────────────────────────────────────────────────
# PROBLEM: Given array and integer k, find the first k missing
#          positive numbers in order.
#
# IDENTIFY: find multiple missing positives → cyclic sort + extra scan
#
# DIFFERENCE FROM first_missing_positive (LC 41):
#   LC 41  → find ONE smallest missing positive
#   This   → find FIRST K missing positives in ascending order
#
# APPROACH:
#   Step 1 → cyclic sort (ignore values outside [1, n])
#   Step 2 → scan [0, n): collect indices where nums[i] != i+1
#             these are missing numbers within [1, n]
#   Step 3 → if still need more (k not filled):
#             continue from n+1 upward BUT skip numbers already in array
#             use a set of extra numbers seen in array for O(1) lookup
#
# WHY a set for step 3?
#   After cyclic sort, values > n are still in the array (we skipped them).
#   These large values might coincide with the numbers we want to add.
#   Set lets us check in O(1) whether a candidate is already present.
#
# TIME: O(n + k)  SPACE: O(n) for the extra_nums set

def first_k_missing_positive(nums, k):
    n = len(nums)
    i = 0

    # step 1: cyclic sort, skip values outside [1, n]
    while i < n:
        correct = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    # step 2: collect missing within [1, n] and track extra values
    missing    = []
    extra_nums = set()   # values > n still sitting in array

    for i in range(n):
        if nums[i] != i + 1:
            missing.append(i + 1)        # i+1 is missing
            extra_nums.add(nums[i])      # nums[i] is an extra (> n or duplicate)
        if len(missing) == k:
            return missing

    # step 3: still need more → go beyond n
    candidate = n + 1
    while len(missing) < k:
        if candidate not in extra_nums:  # not already in array
            missing.append(candidate)
        candidate += 1

    return missing


print(first_k_missing_positive([3, -1, 4, 5, 5], 3))  # [1, 2, 6]
print(first_k_missing_positive([2, 3, 4], 3))          # [1, 5, 6]
print(first_k_missing_positive([1, 2, 3, 6], 2))       # [4, 5]
print(first_k_missing_positive([-1, -2], 3))           # [1, 2, 3]
