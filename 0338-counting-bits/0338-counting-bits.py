class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(x):
            res = 0
            while x:
                res+=1
                x &= x - 1
            return res
        res = []
        for i in range(n+1):
            res.append(count(i))
        return res