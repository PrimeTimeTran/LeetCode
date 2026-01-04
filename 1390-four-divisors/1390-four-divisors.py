from math import isqrt

class Solution:
    def sumFourDivisors(self, nums):
        total = 0
        for n in nums:
            divisors = []
            for i in range(1, isqrt(n)+1):
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:
                        divisors.append(n//i)
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                total += sum(divisors)
        return total