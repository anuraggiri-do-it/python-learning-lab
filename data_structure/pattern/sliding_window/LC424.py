# ============================================================
# LC 424. Longest Repeating Character Replacement
# ============================================================
# PROBLEM:
#   Given a string s and integer k, you can replace at most k
#   characters in the string with any uppercase letter.
#   Return the length of the longest substring with all same chars.
#
# EXAMPLE:
#   s = "ABAB", k = 2  →  4  (replace both B's → "AAAA")
#   s = "AABABBA", k = 1  →  4  (replace one B → "AABA" or "ABBA")
#
# PATTERN: Sliding Window (variable size)
#
# INTUITION:
#   - In any window of size `w`, we need to replace (w - maxFreq) chars
#   - maxFreq = count of the most frequent char in the window
#   - If (window_size - maxFreq) > k → too many replacements needed → shrink
#   - Key formula: window_size - maxFreq <= k  →  valid window
#
# WHY array of size 26?
#   Only uppercase letters A-Z → index = ord(char) - ord('A')
#   Faster than a dict for fixed alphabet
#
# TIME  : O(n) — single pass
# SPACE : O(1) — fixed array of 26
# ============================================================

def characterReplacement(s, k):
    count   = [0] * 26    # frequency of each char in current window
    left    = 0
    maxFreq = 0            # max frequency of any single char in window
    result  = 0

    for right in range(len(s)):
        idx = ord(s[right]) - ord('A')
        count[idx] += 1                          # EXPAND: add right char

        maxFreq = max(maxFreq, count[idx])       # update max frequency

        # window_size - maxFreq = chars we need to replace
        # if > k → invalid → shrink from left
        while (right - left + 1) - maxFreq > k:
            count[ord(s[left]) - ord('A')] -= 1  # remove left char
            left += 1                            # shrink window

        result = max(result, right - left + 1)   # valid window → update answer

    return result


# ── TEST CASES ──────────────────────────────────────────────
if __name__ == "__main__":
    print(characterReplacement("ABAB", 2))        # 4
    print(characterReplacement("AABABBA", 1))     # 4
    print(characterReplacement("AAAA", 0))        # 4 — already all same
    print(characterReplacement("ABCD", 0))        # 1 — no replacements
    print(characterReplacement("BABOONIFICATION", 5))  # test custom
