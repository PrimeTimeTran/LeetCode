'''
1. Understand
Use at most k transactions to realize a maximum total profit from the range of days given.
Open positions muse be closed to realize a profit.

Can both short and long stocks.

Opened transactions must be closed the day before opening a new one.


Pseudocode:
Start from the base case, the first day with 0 transactions & no open positions.
Recurse by moving forward in the timeline and incrementing the count of completed transactions when appropriate.
On each recursion step, if holding close the transaction. Otherwise open a short or long position.
Also calculate the outcome if the day is skipped.

Return the maximum of the potential pnl from acting today and skipped.
'''

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        # 1 = buy to open
        # 2 = sell to open
        @lru_cache(1000**4)
        def dp(i, completed_count, position):
            if i == n or completed_count == k:
                return 0 if position is None else -inf
            price = prices[i]
            i+=1
            skip = dp(i, completed_count, position)
            if position:
                sign = 1 if position == 1 else -1
                buy_or_sell = sign * price
                pnl_today_included = buy_or_sell + dp(i, completed_count+1, None)
            else:
                pnl_today_included = max(
                    dp(i, completed_count, 1) - price,
                    dp(i, completed_count, 2) + price
                )

            return max(skip, pnl_today_included)
        return dp(0, 0, 0)
