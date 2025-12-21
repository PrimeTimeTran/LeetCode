class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def dp(i: int, holding: int) -> int:
            if i == n: return 0
            if holding:
                return max(prices[i] + dp(i+1, 0), dp(i+1, 1))
            else:
                return max(-prices[i] + dp(i+1, 1), dp(i+1, 0))
        return dp(0, 0)