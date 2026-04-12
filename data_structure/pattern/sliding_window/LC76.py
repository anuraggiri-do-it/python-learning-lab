# ============================================================
# LC 76. Minimum Window Substring
# ============================================================
# PROBLEM:
#   Given strings s and t, return the shortest substring of s
#   that contains every character in t (with duplicates).
#   Return "" if impossible.
#
# EXAMPLE:
#   s = "ADOBECODEBANC", t = "ABC"  →  "BANC"
#   s = "a",             t = "a"    →  "a"
#   s = "a",             t = "aa"   →  ""
#
# PATTERN: Sliding Window (variable size)
#
# INTUITION:
#   - Count chars needed from t
#   - Expand right until all chars covered (formed == required)
#   - Shrink left to minimize window, record result
#   - Repeat until high reaches end
#
# VISUAL:
#   s = "ADOBECODEBANC", t = "ABC"
#   Expand → "ADOBEC"  (has A,B,C) → valid, record len=6
#   Shrink → "DOBEC"   (no A)      → invalid, expand
#   Expand → "DOBECODEBA" → valid, record len=10? no, 6 is better
#   ...
#   Final valid minimum → "BANC" (len=4) ✅
#
# TIME  : O(n + m)
# SPACE : O(n + m)
# ============================================================

from collections import Counter

def minWindow(s, t):
    if not s or not t:
        return ""

    need    = Counter(t)       # chars needed and their counts
    window  = {}               # chars in current window
    have     = 0               # distinct chars fully satisfied
    required = len(need)       # distinct chars we need to satisfy

    low = 0
    result = ""
    min_len = float('inf')

    for high in range(len(s)):
        c = s[high]
        window[c] = window.get(c, 0) + 1

        if c in need and window[c] == need[c]:
            have += 1                          # one more char fully covered

        while have == required:                # valid window → try to shrink
            if (high - low + 1) < min_len:
                min_len = high - low + 1
                result  = s[low : high + 1]   # save smallest window so far

            lc = s[low]
            window[lc] -= 1
            if lc in need and window[lc] < need[lc]:
                have -= 1                      # lost coverage → stop shrinking
            low += 1

    return result


# ── TEST CASES ──────────────────────────────────────────────
if __name__ == "__main__":
    print(minWindow("ADOBECODEBANC", "ABC"))      # "BANC"
    print(minWindow("a", "a"))                    # "a"
    print(minWindow("a", "aa"))                   # ""
    print(minWindow("aa", "aa"))                  # "aa"
    print(minWindow("cabwefgewcwaefgcf", "cae"))  # "cwae"
