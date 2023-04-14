class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def dp(l, r):
            if l > r: return 0  # Return 0 since it's empty string
            if l == r: return 1  # Return 1 since it has 1 character
            if s[l] == s[r]:
                return dp(l+1, r-1) + 2
            return max(dp(l, r-1), dp(l+1, r))
        
        return dp(0, n-1)