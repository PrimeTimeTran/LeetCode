class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        @lru_cache(maxsize=1000*4)
        def dp(i: int, completed_transactions: int, position: str):
            if i == len(prices) or completed_transactions == k:
                return 0 if position == None else -inf
            p, pnl_today_included = prices[i], -inf
            i+=1
            if position:
                sign = -1 if position == "sell_to_open" else 1
                pnl_today = sign * p
                pnl_unrealized = dp(i, completed_transactions + 1, None)
                pnl_today_included = pnl_today + pnl_unrealized
            else:
                pnl_today_included = max(
                    dp(i, completed_transactions, "sell_to_open") + p,
                    dp(i, completed_transactions, "buy_to_open") - p,
                )
            pnl_today_skipped = dp(i, completed_transactions, position)
            return max(pnl_today_skipped, pnl_today_included)
        return dp(0, 0, None)
