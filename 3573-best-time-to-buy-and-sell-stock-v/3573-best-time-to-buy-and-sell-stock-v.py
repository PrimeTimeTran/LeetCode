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
        @lru_cache(1000*4)
        # 0 = None
        # 1 = buy_to_open
        # 2 = sell_to_open
        def dp(i, position, completed_count):
            if i == n or completed_count == k:
                return 0 if position is None else -inf
            price = prices[i]
            i+=1
            skip = dp(i, position, completed_count)
            cashflow_realized = price if position == 1 else -price
            if position:
                realized = price if position == 1 else -price
                act = realized + dp(i, None, completed_count+1)
            else:
                act = max(
                    dp(i, 1, completed_count) - price,
                    dp(i, 2, completed_count) + price
                )
            return max(skip, act)
        return dp(0, None, 0)