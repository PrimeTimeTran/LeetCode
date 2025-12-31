from functools import lru_cache

class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(None)
        def dp(i):
            if i <= 1:
                return i

            return min(
                (i % 2) + 1 + dp(i // 2),
                (i % 3) + 1 + dp(i // 3),
            )

        return dp(n)
