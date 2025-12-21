'''
1. Understand
Use k transactions max to maximum a realized profit.
Must open and close to make a profit.
Can be both short and long positions.
'''

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @lru_cache(maxsize=1000*4)
        def dp(i, kount, holding):
            if i == n or kount == k:
                return 0 if holding is None else -inf
            price = prices[i]
            i+=1
            skip = dp(i, kount, holding)
            if holding:
                sign = 1 if holding == "sell_to_open" else -1
                pnl_today_included = (sign * price) + dp(i, kount+1, None)
            else:
                pnl_today_included = max(
                    dp(i, kount, "buy_to_open") + price,
                    dp(i, kount, "sell_to_open") - price,
                )
            return max(skip, pnl_today_included)
        return dp(0, 0, False)