class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        for i, j in zip(s, t):
            if s.find(i) == t.find(j):
                continue
            else:return False
        return True