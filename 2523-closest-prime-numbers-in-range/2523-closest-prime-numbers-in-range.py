'''
Move through range left to right adding prime numbers to a list.
If the number is prime and the list is greater than 2 items, compare to current minimum res.
If smaller update res and reset pairs. Also check if minimum is smaller than 3, is so return cause twin primes
are the smallest possible.

'''

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(n):
            if n < 2: return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
            
        q = []    
        pairs = [-1,-1]
        res = float('infinity')
        
        for i in range(left, right+1):
            if isPrime(i):
                q.append(i)
            if len(q) > 1:
                if abs(q[0] - q[1]) < res:
                    pairs = [q[0], q[1]]
                    res = abs(q[0] - q[1])
                    if res < 3:
                        return pairs
                q.pop(0)
        return pairs