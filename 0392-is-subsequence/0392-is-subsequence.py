class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(c in t for c in s)
        # if len(s)==0:
        #     return True
        # elif len(s)>len(t):
        #     return False
        # elif s[0]==t[0]:
        #     return self.isSubsequence(s[1:], t[1:])
        # return self.isSubsequence(s, t[1:])