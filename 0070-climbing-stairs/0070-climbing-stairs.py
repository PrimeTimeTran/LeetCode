class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        one,two=1,2

        for _ in range(3, n+1):
            tmp = one + two
            one = two
            two = tmp
        return two