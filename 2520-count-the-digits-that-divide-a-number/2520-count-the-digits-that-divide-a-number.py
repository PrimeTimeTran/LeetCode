class Solution:
    def countDigits(self, x: int) -> int:
        return sum(x % int(y) == 0 for y in str(x))

        digits = [int(d) for d in str(num)]
        res = 0
        for d in digits:
            if num % d == 0:
                res += 1
        return res