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
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dp(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                return 1 + dp(l+1, r-1)
            return max(dp(l+1, r), dp(l, r-1))
        return dp(0, len(s)-1)