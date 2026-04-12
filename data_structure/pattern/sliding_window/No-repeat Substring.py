# ═════════════════════════════════════════════════════════════════════════════
# PROBLEM : Longest Substring Without Repeating Characters  (LeetCode #3)
# ═════════════════════════════════════════════════════════════════════════════
#
# Given a string s, find the length of the longest substring
# that has NO duplicate characters.
#
# Example:
#   s = "abcabcbb"  →  Output = 3   ("abc")
#   s = "bbbbb"     →  Output = 1   ("b")
#   s = "pwwkew"    →  Output = 3   ("wke")
#
# KEY INSIGHT:
#   A substring is a CONTINUOUS part of the string (no skipping).
#   We need the longest window where every character appears exactly once.
#
# Constraints:
#   - 0 <= s.length <= 5 * 10^4
#   - s consists of English letters, digits, symbols and spaces
# ═════════════════════════════════════════════════════════════════════════════


# ─────────────────────────────────────────────────────────────────────────────
# APPROACH 1 : Brute Force
# ─────────────────────────────────────────────────────────────────────────────
#
# IDEA:
#   Check every possible substring using two loops.
#   Use a set to track characters in current substring.
#   If a duplicate is found → stop, move to next start.
#   If no duplicate → update max length.
#
# WHY set?
#   set.add() and 'in' check are both O(1).
#   Automatically tells us if a char already exists in window.
#
# Time  : O(n²)  → two nested loops
# Space : O(n)   → set can hold up to n characters
# ─────────────────────────────────────────────────────────────────────────────

def length_of_longest_substring_brute(s: str) -> int:
    max_len = 0

    for start in range(len(s)):
        seen = set()
        for end in range(start, len(s)):
            if s[end] in seen:          # duplicate found → stop
                break
            seen.add(s[end])            # new char → add to window
            max_len = max(max_len, end - start + 1)

    return max_len


# ─────────────────────────────────────────────────────────────────────────────
# APPROACH 2 : Sliding Window  ✅ OPTIMAL
# ─────────────────────────────────────────────────────────────────────────────
#
# CORE IDEA:
#   Maintain a window [low ... high] with no duplicate characters.
#   EXPAND  → move high right, add s[high] to a set
#   SHRINK  → if s[high] already in set, remove s[low] and move low right
#             keep shrinking until the duplicate is removed
#   ANSWER  → after every valid window, update max_len
#
# WHY set here (not dict)?
#   We only need to know IF a char exists in window, not its count.
#   No duplicates allowed → presence check is enough.
#   set gives O(1) add, remove, and lookup.
#
# WHY shrink until duplicate is gone?
#   When s[high] is already in the window, the window is invalid.
#   We remove from the LEFT one by one until the duplicate is gone.
#   Then the window is valid again.
#
# ─────────────────────────────────────────────────────────────────────────────
# VISUAL TRACE:  s = "abcabcbb"
# ─────────────────────────────────────────────────────────────────────────────
#
#  Step  low  high  char  window     seen          action         max
#  ────  ───  ────  ────  ─────────  ────────────  ─────────────  ───
#   1     0    0    'a'   "a"        {a}           valid           1
#   2     0    1    'b'   "ab"       {a,b}         valid           2
#   3     0    2    'c'   "abc"      {a,b,c}       valid           3  ✅
#   4     0    3    'a'   duplicate! shrink low=0
#                         remove a   {b,c}         still dup? no
#                   'a'   "bca"      {b,c,a}       valid           3
#   5     1    4    'b'   duplicate! shrink low=1
#                         remove b   {c,a}         still dup? no
#                   'b'   "cab"      {c,a,b}       valid           3
#   6     2    5    'c'   duplicate! shrink low=2
#                         remove c   {a,b}         still dup? no
#                   'c'   "abc"      {a,b,c}       valid           3
#   7     3    6    'b'   duplicate! shrink low=3
#                         remove a   {b,c}         still dup? yes (b)
#                         remove b   {c}           still dup? no
#                   'b'   "cb"       {c,b}         valid           3
#   8     5    7    'b'   duplicate! shrink low=5
#                         remove c   {b}           still dup? yes (b)
#                         remove b   {}            still dup? no
#                   'b'   "b"        {b}           valid           3
#
#  Final Answer = 3  ✅
# ─────────────────────────────────────────────────────────────────────────────
#
# Time  : O(n)  → each character added once (high) and removed once (low)
# Space : O(n)  → set holds at most min(n, alphabet_size) characters
# ─────────────────────────────────────────────────────────────────────────────

def length_of_longest_substring(s: str) -> int:
    if not s:
        return 0

    low = 0
    max_len = 0
    seen = set()            # characters in current window

    for high in range(len(s)):
        while s[high] in seen:          # duplicate found → shrink from left
            seen.remove(s[low])         # remove leftmost char
            low += 1                    # move left boundary right

        seen.add(s[high])               # EXPAND: add right char (now unique)
        max_len = max(max_len, high - low + 1)  # update answer

    return max_len


# ─────────────────────────────────────────────────────────────────────────────
# APPROACH 3 : Sliding Window with Index Map  ✅ FASTER SHRINK
# ─────────────────────────────────────────────────────────────────────────────
#
# IDEA:
#   Instead of shrinking one step at a time,
#   store the LAST SEEN INDEX of each character.
#   When a duplicate is found, JUMP low directly past the last occurrence.
#   This avoids the inner while loop entirely.
#
# WHY faster?
#   Approach 2 shrinks one step at a time → still O(n) but more iterations.
#   Approach 3 jumps directly → fewer operations in practice.
#
# WHY max(low, last_seen[char] + 1)?
#   last_seen might store an index BEFORE our current window (low).
#   We never move low backwards → take the max.
#
# Time  : O(n)  → single pass, no inner loop
# Space : O(n)  → dict holds at most min(n, alphabet_size) entries
# ─────────────────────────────────────────────────────────────────────────────

def length_of_longest_substring_optimized(s: str) -> int:
    if not s:
        return 0

    low = 0
    max_len = 0
    last_seen = {}          # char → last index seen

    for high in range(len(s)):
        char = s[high]
        if char in last_seen and last_seen[char] >= low:
            low = last_seen[char] + 1   # JUMP: skip past last duplicate

        last_seen[char] = high          # update last seen index
        max_len = max(max_len, high - low + 1)

    return max_len


# ─────────────────────────────────────────────────────────────────────────────
# COMPLEXITY SUMMARY
# ─────────────────────────────────────────────────────────────────────────────
#
#  Approach               Time     Space   Why
#  ─────────────────────  ───────  ──────  ──────────────────────────────────
#  Brute Force            O(n²)    O(n)    two loops, restart each time
#  Sliding Window (set)   O(n)     O(n)    shrink one step at a time
#  Sliding Window (dict)  O(n)     O(n)    jump directly to valid position
#
# ─────────────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":

    tests = [
        ("abcabcbb",  3),   # "abc"
        ("bbbbb",     1),   # "b"
        ("pwwkew",    3),   # "wke"
        ("abcdef",    6),   # all unique → entire string
        (" ",         1),   # single space
        ("au",        2),   # two unique chars
        ("",          0),   # empty string
        ("dvdf",      3),   # "vdf"
    ]

    print(f"{'Input':<15} {'Expected':<10} {'Set':<6} {'Dict':<6} {'Pass?'}")
    print("-" * 45)
    for s, expected in tests:
        r1 = length_of_longest_substring(s)
        r2 = length_of_longest_substring_optimized(s)
        status = "✅" if r1 == expected and r2 == expected else "❌"
        print(f"{s!r:<15} {expected:<10} {r1:<6} {r2:<6} {status}")

    print("\n--- brute force cross-check ---")
    for s, expected in tests:
        result = length_of_longest_substring_brute(s)
        status = "✅" if result == expected else "❌"
        print(f"{s!r:<15} {expected:<10} {result:<6} {status}")
