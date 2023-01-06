class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        a, b = Counter(s1), Counter(s2)
        if not a == b: return False
        c = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                c+=1
        if c != 2:
            return False
        return True