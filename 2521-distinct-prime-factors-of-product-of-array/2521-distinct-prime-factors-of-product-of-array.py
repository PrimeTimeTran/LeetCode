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