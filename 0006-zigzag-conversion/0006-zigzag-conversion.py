class Solution:
    def convert(self, s: str, n: int) -> str:
        if n >= len(s) or n == 1:
            return s
        l = [''] * n
        i, v = 0, 1
        for c in s:
            l[i] += c
            if i == 0:
                v = 1
            elif i == (n-1):
                v = -1
            i += v
        return ''.join(l)
                
        