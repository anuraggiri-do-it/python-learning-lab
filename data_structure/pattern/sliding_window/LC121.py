# ============================================================
# LC 121. Best Time to Buy and Sell Stock
# ============================================================
# PROBLEM:
#   Given an array prices where prices[i] is the price on day i,
#   return the maximum profit from ONE buy and ONE sell.
#   You must buy BEFORE you sell. Return 0 if no profit possible.
#
# EXAMPLE:
#   prices = [7, 1, 5, 3, 6, 4]  →  Output = 5  (buy@1, sell@6)
#   prices = [7, 6, 4, 3, 1]     →  Output = 0  (prices only fall)
#
# PATTERN: Sliding Window (track min so far + max profit)
#
# INTUITION:
#   - Track the minimum price seen so far (best buy day)
#   - At each day, calculate profit if we sell today
#   - Update max profit
#
# TIME  : O(n) — single pass
# SPACE : O(1) — only two variables
# ============================================================

def maxProfit(prices):
    min_price = float('inf')   # best buy price seen so far
    max_profit = 0             # best profit seen so far

    for price in prices:
        if price < min_price:
            min_price = price          # found a cheaper buy day
        else:
            max_profit = max(max_profit, price - min_price)  # sell today

    return max_profit


# ── TEST CASES ──────────────────────────────────────────────
if __name__ == "__main__":
    print(maxProfit([7, 1, 5, 3, 6, 4]))   # 5  → buy@1 sell@6
    print(maxProfit([7, 6, 4, 3, 1]))      # 0  → no profit possible
    print(maxProfit([1, 2]))               # 1  → buy@1 sell@2
    print(maxProfit([2, 4, 1]))            # 2  → buy@2 sell@4
    print(maxProfit([1]))                  # 0  → only one day
