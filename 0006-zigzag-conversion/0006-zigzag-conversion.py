class Solution:
    def convert(self, s: str, n: int) -> str:
        if n >= len(s) or n == 1:
            return s
        index, v = 0, 1
        res = ['']*n
        
        for c in s:
            res[index] += c
            if index == 0:
                v = 1
            elif index == n-1:
                v = -1
            index+=v
        
        return ''.join(res)