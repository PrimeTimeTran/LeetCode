class Solution:
    def getSum(self, a: int, b: int) -> int:
        # return sum([a,b])
        # return int(math.log2(2**a * 2**b))
        # return operator.add(a,b)
        mask = 0xffffffff
        
        while b & mask != 0:
            c = (a&b) << 1
            a = a^b
            b = c

        return a & mask if b > mask else a