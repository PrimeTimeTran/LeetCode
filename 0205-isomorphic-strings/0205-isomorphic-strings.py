class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        for i, j in zip(s, t):
            if not s.find(i) == t.find(j): return False
        return True