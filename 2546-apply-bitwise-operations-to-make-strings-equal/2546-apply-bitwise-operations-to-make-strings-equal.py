class Solution:
    def makeStringsEqual(self, s: str, t: str) -> bool:
        return max(s) == max(t)             