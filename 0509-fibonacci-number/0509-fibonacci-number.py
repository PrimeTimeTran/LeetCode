class Solution:
    def fib(self, n: int, memo = {}) -> int:
        if n < 2:
            return n
        if n in memo:
            return memo[n]
        memo[n] = self.fib(n-1)+self.fib(n-2)
        return memo[n]