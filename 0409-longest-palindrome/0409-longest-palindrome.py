'''
Count number of odd characters and subtract that count from length of the string + 1

'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = set()
        for c in s:
            if c in hash:
                hash.remove(c)
            else:
                hash.add(c)
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)