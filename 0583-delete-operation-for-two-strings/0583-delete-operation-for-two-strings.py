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
    def minDistance(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        @lru_cache(None)
        def dp(i, j):
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + dp(i+1, j+1)
            return max(dp(i+1,j), dp(i, j+1))
        common = dp(0, 0) * 2
        return (m+n) - common