'''
1. Understand
Use k transactions max to maximum a realized profit.
Must open and close to make a profit.
Can be both short and long positions.
'''

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        @lru_cache(None)
        def dp(i, num, holding):
            if i == n or num == k:
                return 0 if holding is None else -inf
            skip = dp(i+1, num, holding)
            price = prices[i]
            num += 1 if holding else 0
            if holding:
                sign = -1 if holding == "sell_to_open" else 1
                pnl_today = sign * price
                pnl = sign * price
                pnl_unrealized = dp(i+1, num, None)
                pnl_today_included = pnl + pnl_unrealized
            else:
                pnl_today_included = max(
                    dp(i+1, num, "sell_to_open") + price,
                    dp(i+1, num, "buy_to_open") - price
                )
            return max(skip, pnl_today_included)
        return dp(0, 0, False)
