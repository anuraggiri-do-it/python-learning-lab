# ═════════════════════════════════════════════════════════════════════════════
# PROBLEM : Longest Substring with K Distinct Characters
# ═════════════════════════════════════════════════════════════════════════════
#
# Given a string s and integer k,
# return the length of the longest substring with AT MOST k distinct characters.
#
# Example:
#   s = "araaci",  k = 2
#   Output = 4   →  "araa"  (distinct: a, r)
#
# Constraints:
#   - 1 <= s.length <= 10^5
#   - s consists of English letters
#   - 0 <= k <= 26
# ═════════════════════════════════════════════════════════════════════════════


# ─────────────────────────────────────────────────────────────────────────────
# APPROACH 1 : Brute Force
# ─────────────────────────────────────────────────────────────────────────────
#
# IDEA:
#   Try every possible substring using two loops.
#   For each substring, count distinct characters using a set.
#   If distinct count <= k, update max length.
#
# WHY set?
#   We only need to know HOW MANY distinct chars exist, not their count.
#   set automatically ignores duplicates → len(set) = distinct count.
#
# WHY break early?
#   Once distinct > k, extending further only adds more chars.
#   No point continuing inner loop → break saves time.
#
# Time  : O(n²)  → outer loop n times, inner loop up to n times
# Space : O(k)   → set holds at most k+1 chars before we break
# ─────────────────────────────────────────────────────────────────────────────

def longest_k_distinct_brute(s: str, k: int) -> int:
    if not s or k == 0:
        return 0

    max_len = 0

    for start in range(len(s)):
        seen = set()
        for end in range(start, len(s)):
            seen.add(s[end])            # add current char to window
            if len(seen) > k:
                break                   # distinct exceeded k → no point going further
            max_len = max(max_len, end - start + 1)

    return max_len


# ─────────────────────────────────────────────────────────────────────────────
# APPROACH 2 : Sliding Window  ✅ OPTIMAL
# ─────────────────────────────────────────────────────────────────────────────
#
# CORE IDEA:
#   Maintain a window [low ... high] where distinct chars <= k.
#   EXPAND  → move high right, add s[high] to frequency map
#   SHRINK  → when distinct > k, move low right, remove s[low] from map
#   ANSWER  → after every valid window, update max_len
#
# WHY dictionary (freq map) instead of set?
#   A set only tells us IF a char exists, not HOW MANY times.
#   When we shrink from left, we need to know if a char is fully gone.
#   dict tracks count → when count hits 0, delete key → len(freq) = distinct count.
#
# WHY delete key when count == 0?
#   len(freq) is how we count distinct characters in the window.
#   If we keep keys with count=0, len(freq) gives wrong distinct count.
#   Deleting ensures len(freq) is always accurate.
#
# WHY update max_len AFTER the while loop?
#   After shrinking, the window is guaranteed valid (distinct <= k).
#   So we safely record the current window size.
#
# ─────────────────────────────────────────────────────────────────────────────
# VISUAL TRACE:  s = "araaci",  k = 2
# ─────────────────────────────────────────────────────────────────────────────
#
#  Step  high  char  freq              distinct  action         max_len
#  ────  ────  ────  ────────────────  ────────  ─────────────  ───────
#   1     0    'a'   {a:1}             1  ≤ 2    valid           1
#   2     1    'r'   {a:1, r:1}        2  ≤ 2    valid           2
#   3     2    'a'   {a:2, r:1}        2  ≤ 2    valid           3
#   4     3    'a'   {a:3, r:1}        2  ≤ 2    valid           4
#   5     4    'c'   {a:3, r:1, c:1}   3  > 2    shrink low=0
#              del?  a:3→2             still 3   shrink low=1
#              del?  r:1→0 → del r     {a:2,c:1} 2  ≤ 2    valid  4
#   6     5    'i'   {a:2, c:1, i:1}   3  > 2    shrink low=2
#              del?  a:2→1             still 3   shrink low=3
#              del?  a:1→0 → del a     {c:1,i:1} 2  ≤ 2    valid  4
#
#  Final Answer = 4  ✅
# ─────────────────────────────────────────────────────────────────────────────
#
# Time  : O(n)  → each character added once (high) and removed once (low)
# Space : O(k)  → freq map holds at most k+1 keys before shrinking
# ─────────────────────────────────────────────────────────────────────────────

def longest_k_distinct(s: str, k: int) -> int:
    if not s or k == 0:
        return 0

    low = 0
    max_len = 0
    freq = {}               # char → frequency in current window

    for high in range(len(s)):
        char = s[high]
        freq[char] = freq.get(char, 0) + 1      # EXPAND: add right char

        while len(freq) > k:                     # distinct > k → must shrink
            left_char = s[low]
            freq[left_char] -= 1                 # reduce count of leftmost char
            if freq[left_char] == 0:
                del freq[left_char]              # fully removed → delete to keep distinct count accurate
            low += 1                             # shrink window from left

        max_len = max(max_len, high - low + 1)   # window valid → update answer

    return max_len


# ─────────────────────────────────────────────────────────────────────────────
# COMPLEXITY SUMMARY
# ─────────────────────────────────────────────────────────────────────────────
#
#  Approach        Time     Space   Why
#  ──────────────  ───────  ──────  ──────────────────────────────────────────
#  Brute Force     O(n²)    O(k)    two loops, restart from each position
#  Sliding Window  O(n)     O(k)    each char added & removed at most once
#
# ─────────────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":

    tests = [
        ("araaci",  2,  4),   # "araa"   → a,r
        ("araaci",  1,  2),   # "aa"     → only a
        ("cbbebi",  3,  5),   # "cbbeb"  → c,b,e
        ("aabbcc",  2,  4),   # "aabb" or "bbcc"
        ("abcdef",  6,  6),   # entire string, all 6 distinct
        ("aaaa",    2,  4),   # only 1 distinct, k=2 still fine
        ("",        2,  0),   # empty string
        ("araaci",  0,  0),   # k=0 → no chars allowed
    ]

    print(f"{'Input':<12} {'k':<4} {'Expected':<10} {'Got':<6} {'Pass?'}")
    print("-" * 45)
    for s, k, expected in tests:
        result = longest_k_distinct(s, k)
        status = "✅" if result == expected else "❌"
        print(f"{s!r:<12} {k:<4} {expected:<10} {result:<6} {status}")

    print("\n--- brute force cross-check ---")
    for s, k, expected in tests:
        result = longest_k_distinct_brute(s, k)
        status = "✅" if result == expected else "❌"
        print(f"{s!r:<12} {k:<4} {expected:<10} {result:<6} {status}")
