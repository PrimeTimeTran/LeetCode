class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(num):
            res = 0
            while num:
                res += 1
                num &= num - 1
            return res
        res = []
        for i in range(n+1):
            res.append(countOnes(i))
        return res
