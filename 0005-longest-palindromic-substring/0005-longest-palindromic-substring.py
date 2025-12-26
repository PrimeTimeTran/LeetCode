class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, res = len(s), s[0]
        for l in range(n-1):
            for r in range(l+1, n):
                substr, len_substr = s[l:r+1], r - l + 1
                is_palindrome = substr == substr[::-1]
                is_new_max = len_substr > len(res)
                if is_palindrome and is_new_max:
                    res = substr
        return res