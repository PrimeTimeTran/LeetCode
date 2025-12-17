class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0: return False
        while num & 1 == 0:
            num >>= 1
        for p in [3, 5]:
            while num % p == 0:
                num /= p
        return num == 1