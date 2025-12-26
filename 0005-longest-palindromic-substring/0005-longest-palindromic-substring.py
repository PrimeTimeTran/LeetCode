class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, max_len, res = len(s), 1, s[0]
        for l in range(n-1):
            for r in range(l+1, n):
                substring = s[l:r+1]
                cur_len = len(substring)
                is_palindrome = substring == substring[::-1]
                new_max_len = cur_len > max_len
                if new_max_len and is_palindrome:
                    max_len = cur_len
                    res = substring
        return res
