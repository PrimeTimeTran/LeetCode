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
        def dp(i: int, completed: int, holding: int):
            # holding: 0 = no position, 1 = buy_to_open, 2 = sell_to_open
            if i == n or completed == k:
                return 0 if holding == 0 else -float('inf')

            skip = dp(i + 1, completed, holding)
            price = prices[i]

            if holding != 0:
                sign = 1 if holding == 1 else -1
                pnl = sign * price + dp(i + 1, completed + 1, 0)
            else:
                # Open a position
                pnl = max(
                    dp(i + 1, completed, 1) - price,  # buy_to_open
                    dp(i + 1, completed, 2) + price   # sell_to_open
                )

            return max(skip, pnl)

        return dp(0, 0, 0)