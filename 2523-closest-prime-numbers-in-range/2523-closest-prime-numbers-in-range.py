class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(n):
            if n < 2: return False
            for i in range(2, n // 2 +1):
                if n % i == 0:
                    return False
            return True
                
        q = []
        diff = float('infinity')
        pair = [-1,-1]
        
        for i in range(left, right+1):
            if isPrime(i):
                q.append(i)
            while len(q) >= 2:
                if abs(q[0] - q[1]) < diff:
                    diff = abs(q[0] - q[1])
                    pair = [q[0], q[1]]
                    if diff <= 2: return pair
                q.pop(0)
        return pair