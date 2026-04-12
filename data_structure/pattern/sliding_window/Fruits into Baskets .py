# ═════════════════════════════════════════════════════════════════════════════
# PROBLEM : Fruits into Baskets
# ═════════════════════════════════════════════════════════════════════════════
#
# You have a row of trees where fruits[i] is the type of fruit tree i produces.
# You have exactly 2 baskets. Each basket can hold only ONE type of fruit
# but unlimited quantity.
#
# Starting from any tree, pick fruits continuously without skipping a tree.
# Return the MAXIMUM number of fruits you can collect.
#
# Example:
#   fruits = [1, 2, 1]       →  Output = 3   (pick all)
#   fruits = [0, 1, 2, 2]    →  Output = 3   (pick [1,2,2])
#   fruits = [1, 2, 3, 2, 2] →  Output = 4   (pick [2,3,2,2])
#
# KEY INSIGHT:
#   "2 baskets, 1 type each" = longest subarray with AT MOST 2 distinct values
#   This is exactly the K Distinct Characters problem with k = 2
#
# Constraints:
#   - 1 <= fruits.length <= 10^5
#   - 0 <= fruits[i] < fruits.length
# ═════════════════════════════════════════════════════════════════════════════


# ─────────────────────────────────────────────────────────────────────────────
# APPROACH 1 : Brute Force
# ─────────────────────────────────────────────────────────────────────────────
#
# IDEA:
#   Try every possible subarray using two loops.
#   Track distinct fruit types using a set.
#   If distinct types <= 2, update max count.
#
# WHY set?
#   We only care about HOW MANY distinct types exist, not their count.
#   set ignores duplicates → len(set) = distinct fruit types.
#
# WHY break early?
#   Once distinct > 2, adding more fruits only increases distinct count.
#   No valid subarray can start here → break inner loop.
#
# Time  : O(n²)  → two nested loops over n trees
# Space : O(1)   → set holds at most 3 elements before we break
# ─────────────────────────────────────────────────────────────────────────────

def total_fruit_brute(fruits: list[int]) -> int:
    max_fruits = 0

    for start in range(len(fruits)):
        basket = set()
        for end in range(start, len(fruits)):
            basket.add(fruits[end])         # add fruit type to basket
            if len(basket) > 2:
                break                       # 3rd type found → stop
            max_fruits = max(max_fruits, end - start + 1)

    return max_fruits


# ─────────────────────────────────────────────────────────────────────────────
# APPROACH 2 : Sliding Window  ✅ OPTIMAL
# ─────────────────────────────────────────────────────────────────────────────
#
# CORE IDEA:
#   Maintain a window [low ... high] with at most 2 distinct fruit types.
#   EXPAND  → move high right, add fruits[high] to frequency map
#   SHRINK  → when distinct types > 2, move low right, remove fruits[low]
#   ANSWER  → after every valid window, update max_fruits
#
# WHY frequency map (dict) instead of set?
#   When shrinking from left, we need to know if a fruit type is fully gone.
#   dict tracks count → when count hits 0, delete key.
#   len(freq) = number of distinct types currently in window.
#
# WHY delete key when count == 0?
#   len(freq) is how we count distinct types.
#   Keeping zero-count keys makes len(freq) inaccurate.
#   Delete ensures len(freq) always reflects actual distinct count.
#
# WHY update max_fruits AFTER the while loop?
#   After shrinking, window is guaranteed valid (distinct <= 2).
#   Safe to record current window size as a candidate answer.
#
# ─────────────────────────────────────────────────────────────────────────────
# VISUAL TRACE:  fruits = [1, 2, 3, 2, 2]
# ─────────────────────────────────────────────────────────────────────────────
#
#  Step  high  fruit  freq              distinct  action          max
#  ────  ────  ─────  ────────────────  ────────  ──────────────  ───
#   1     0     1     {1:1}             1  ≤ 2    valid            1
#   2     1     2     {1:1, 2:1}        2  ≤ 2    valid            2
#   3     2     3     {1:1, 2:1, 3:1}   3  > 2    shrink low=0
#                     1:1→0 → del 1     {2:1,3:1} 2  ≤ 2    valid  3
#   4     3     2     {2:2, 3:1}        2  ≤ 2    valid            4  ✅
#   5     4     2     {2:3, 3:1}        2  ≤ 2    valid            4
#
#  Final Answer = 4  ✅  (subarray [2, 3, 2, 2])
# ─────────────────────────────────────────────────────────────────────────────
#
# Time  : O(n)  → each fruit added once (high) and removed once (low)
# Space : O(1)  → freq map holds at most 3 keys before shrinking (k=2 fixed)
# ─────────────────────────────────────────────────────────────────────────────

def total_fruit(fruits: list[int]) -> int:
    if not fruits:
        return 0

    low = 0
    max_fruits = 0
    freq = {}               # fruit_type → count in current window

    for high in range(len(fruits)):
        fruit = fruits[high]
        freq[fruit] = freq.get(fruit, 0) + 1        # EXPAND: add right fruit

        while len(freq) > 2:                         # more than 2 types → shrink
            left_fruit = fruits[low]
            freq[left_fruit] -= 1                    # reduce count of leftmost fruit
            if freq[left_fruit] == 0:
                del freq[left_fruit]                 # fully removed → delete key
            low += 1                                 # shrink window from left

        max_fruits = max(max_fruits, high - low + 1) # window valid → update answer

    return max_fruits


# ─────────────────────────────────────────────────────────────────────────────
# CONNECTION TO K DISTINCT PROBLEM
# ─────────────────────────────────────────────────────────────────────────────
#
# Fruits into Baskets  ==  Longest Subarray with K=2 Distinct Values
#
#   fruits  →  characters in a string
#   basket  →  distinct character type
#   k = 2   →  exactly 2 baskets
#
# Generic version (works for any k):
def longest_k_distinct(arr: list[int], k: int) -> int:
    low, max_len, freq = 0, 0, {}
    for high in range(len(arr)):
        freq[arr[high]] = freq.get(arr[high], 0) + 1
        while len(freq) > k:
            freq[arr[low]] -= 1
            if freq[arr[low]] == 0:
                del freq[arr[low]]
            low += 1
        max_len = max(max_len, high - low + 1)
    return max_len

# total_fruit(fruits) == longest_k_distinct(fruits, k=2)


# ─────────────────────────────────────────────────────────────────────────────
# COMPLEXITY SUMMARY
# ─────────────────────────────────────────────────────────────────────────────
#
#  Approach        Time     Space   Why
#  ──────────────  ───────  ──────  ──────────────────────────────────────────
#  Brute Force     O(n²)    O(1)    two loops, restart from each tree
#  Sliding Window  O(n)     O(1)    each fruit added & removed at most once
#                                   space O(1) because k=2 is fixed
#
# ─────────────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":

    tests = [
        ([1, 2, 1],          3),   # pick all → [1,2,1]
        ([0, 1, 2, 2],       3),   # [1,2,2]
        ([1, 2, 3, 2, 2],    4),   # [2,3,2,2]
        ([3, 3, 3, 1, 2, 1], 4),   # [3,3,3,1]
        ([1],                1),   # single tree
        ([1, 1, 1, 1],       4),   # all same type → 1 basket used
        ([],                 0),   # empty
    ]

    print(f"{'fruits':<25} {'Expected':<10} {'Got':<6} {'Pass?'}")
    print("-" * 50)
    for fruits, expected in tests:
        result = total_fruit(fruits)
        status = "✅" if result == expected else "❌"
        print(f"{str(fruits):<25} {expected:<10} {result:<6} {status}")

    print("\n--- brute force cross-check ---")
    for fruits, expected in tests:
        if not fruits:
            continue
        result = total_fruit_brute(fruits)
        status = "✅" if result == expected else "❌"
        print(f"{str(fruits):<25} {expected:<10} {result:<6} {status}")
