class Solution:
    def findContentChildren(self, g, s):
        s.sort()
        g.sort()
        i = j = c = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[i]:
                i+=1
                c+=1
            j+=1
        return c