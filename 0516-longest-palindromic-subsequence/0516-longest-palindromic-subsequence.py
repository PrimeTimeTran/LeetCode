'''
1. Understand
2. Diagram
3. Pseudocode
4. Code
5. BigO
Time: O()
Space: O()
'''
from functools import lru_cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return 2 + dp(i+1, j-1)
            else:
                return max(dp(i+1, j), dp(i, j-1))
        
        return dp(0, n-1)
