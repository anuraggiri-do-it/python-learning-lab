# ============================================================
# LC 72. Edit Distance
# ============================================================
# PROBLEM:
#   Given two strings word1 and word2, return the minimum number
#   of operations to convert word1 into word2.
#   Allowed operations (each costs 1):
#     - Insert a character
#     - Delete a character
#     - Replace a character
#
# EXAMPLE:
#   word1 = "horse", word2 = "ros"  →  3
#     horse → rorse (replace h→r)
#     rorse → rose  (delete r)
#     rose  → ros   (delete e)
#
#   word1 = "intention", word2 = "execution"  →  5
#
# PATTERN: Dynamic Programming (2D DP table)
#
# INTUITION:
#   dp[i][j] = min operations to convert word1[:i] → word2[:j]
#
#   BASE CASES:
#     dp[i][0] = i  → delete all i chars from word1
#     dp[0][j] = j  → insert all j chars from word2
#
#   RECURRENCE:
#     if word1[i-1] == word2[j-1]:
#         dp[i][j] = dp[i-1][j-1]        → chars match, no operation needed
#     else:
#         dp[i][j] = 1 + min(
#             dp[i-1][j],                 → delete from word1
#             dp[i][j-1],                 → insert into word1
#             dp[i-1][j-1]               → replace in word1
#         )
#
# VISUAL TRACE: word1="horse", word2="ros"
#
#       ""  r  o  s
#   ""   0  1  2  3
#   h    1  1  2  3
#   o    2  2  1  2
#   r    3  2  2  2
#   s    4  3  3  2
#   e    5  4  4  3   ← answer = dp[5][3] = 3 ✅
#
# TIME  : O(m × n) — fill entire dp table
# SPACE : O(m × n) — dp table  |  can be optimised to O(n) with 1D dp
# ============================================================

def minDistance(word1, word2):
    m, n = len(word1), len(word2)

    # dp[i][j] = min edits to convert word1[:i] to word2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # base cases
    for i in range(m + 1):
        dp[i][0] = i       # delete all chars from word1
    for j in range(n + 1):
        dp[0][j] = j       # insert all chars of word2

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i-1][j-1]           # chars match → free
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],                    # delete
                    dp[i][j-1],                    # insert
                    dp[i-1][j-1]                   # replace
                )

    return dp[m][n]


# ============================================================
# SPACE OPTIMISED — O(n) space
# ============================================================
# We only ever need the PREVIOUS row to compute the current row.
# So we can use a single 1D array and update it in place.
#
# TIME  : O(m × n)
# SPACE : O(n)
# ============================================================

def minDistance_optimised(word1, word2):
    m, n = len(word1), len(word2)
    prev = list(range(n + 1))          # represents dp[i-1]

    for i in range(1, m + 1):
        curr = [i] + [0] * n           # curr[0] = i (delete i chars)
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]  # match → no cost
            else:
                curr[j] = 1 + min(
                    prev[j],           # delete
                    curr[j - 1],       # insert
                    prev[j - 1]        # replace
                )
        prev = curr

    return prev[n]


# ── TEST CASES ──────────────────────────────────────────────
if __name__ == "__main__":
    tests = [
        ("horse",     "ros",       3),
        ("intention", "execution", 5),
        ("",          "",          0),   # both empty
        ("abc",       "",          3),   # delete all
        ("",          "abc",       3),   # insert all
        ("abc",       "abc",       0),   # identical
        ("a",         "b",         1),   # single replace
    ]

    print(f"{'word1':<12} {'word2':<12} {'Exp':<5} {'2D':<5} {'1D':<5} {'Pass?'}")
    print("-" * 45)
    for w1, w2, expected in tests:
        r1 = minDistance(w1, w2)
        r2 = minDistance_optimised(w1, w2)
        status = "✅" if r1 == expected and r2 == expected else "❌"
        print(f"{w1:<12} {w2:<12} {expected:<5} {r1:<5} {r2:<5} {status}")
