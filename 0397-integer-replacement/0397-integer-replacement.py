class Solution:
    def integerReplacement(self, n: int) -> int:
        @lru_cache(None)
        def dp(i):
            if i == 1:
                return 0
            if i % 2 == 0:
                return 1 + dp(i // 2)
            return 1 + min(dp(i + 1), dp(i - 1))
        return dp(n)