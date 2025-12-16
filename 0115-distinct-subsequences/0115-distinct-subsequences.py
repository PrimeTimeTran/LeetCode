'''
1. Understand
2. Diagram
3. Pseudocode
4. Code
5. BigO
Time: O()
Space: O()
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        @lru_cache(None)
        def dp(i, j):
            if j == n:
                return 1
            if i == m:
                return 0
            ans = dp(i+1, j)
            if s[i] == t[j]:
                ans += dp(i+1, j+1)
            return ans
        return dp(0, 0)