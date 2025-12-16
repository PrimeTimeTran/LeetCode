class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        max_int = 0x7fffffff

        while b != 0:
            c = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = c
        return a if a <= max_int else ~(a ^ mask)