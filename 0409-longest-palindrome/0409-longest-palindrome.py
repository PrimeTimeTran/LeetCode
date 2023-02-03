class Solution:
    def longestPalindrome(self, s: str) -> int:
        h = set()
        for c in s:
            if c in h:
                h.remove(c)
            else: h.add(c)
        return len(s)-len(h)+1 if len(h) > 0 else len(s)