class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10: return num
        while num > 9:
            res = 0
            for c in str(num):
                res += int(c)
            num = res
        return num