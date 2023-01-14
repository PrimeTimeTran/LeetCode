class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = set()
        for c in s:
            if c in hash:
                hash.remove(c)
            else:
                hash.add(c)
        # len(hash) is the number of the odd letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)