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
        def dp(i, j):
            if i == len(s) or j < 0:
                return 0
            if s[i] == s[j]:
                return 1 + dp(i+1, j-1)
            return max(dp(i+1,j), dp(i,j-1))
        return dp(0, len(s)-1)