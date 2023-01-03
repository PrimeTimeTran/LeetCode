class Solution:
    def countDigits(self, num: int) -> int:
        # return sum(x % int(y) == 0 for y in str(x))
        res = 0
        for d in str(num):
            if num % int(d) == 0:
                res += 1
        return res