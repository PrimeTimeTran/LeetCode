class Solution:
    def hammingDistance(self, n1: int, n2: int) -> int:
        x = n1 ^ n2
        res = 0
        while x:
            res+=1
            x &= x-1
        return res