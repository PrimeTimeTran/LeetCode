'''
1. Understand
Use k transactions max to maximum a realized profit.
Must open and close to make a profit.
Can be both short and long positions.
'''

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        # 0 = None
        # 1 = Buy to open
        # 2 = Sell to open
        @lru_cache(maxsize=1000*4)
        def dp(i, kount, holding):
            if i == n or kount == k:
                return 0 if holding is None else -10**18
            price = prices[i]
            i+=1
            skip = dp(i, kount, holding)
            if holding:
                sign = 1 if holding == 1 else -1
                pnl_from_close = sign * price
                pnl_today_included = pnl_from_close + dp(i, kount+1, None)
            else:
                pnl_today_included = max(
                    price + dp(i, kount, 2),
                    dp(i, kount, 1) - price,
                )
            return max(skip, pnl_today_included)
        return dp(0, 0, False)