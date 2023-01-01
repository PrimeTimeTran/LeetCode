'''
1. Constraints
We receieve input array and must an integer.



2. Pseudocode

Process each number looking for it's prime factors.
If the number contains a prime factor, add it to a set.



'''

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()
        def process(num):
            n = num
            for i in range(2, num+1):
                if n % i == 0:
                    while n % i == 0:
                        n /= i
                        s.add(i)
                if n == 1:
                    return
            
        
        for n in nums:
            process(n)
            
        return len(s)