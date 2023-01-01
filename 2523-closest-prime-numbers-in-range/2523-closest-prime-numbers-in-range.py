'''

Iterate range left to right
Identify prime nums, add them to a queue.

If the queue has 2 or more items, calculate min difference between elements


'''

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    return False
            return True
        
        pair = [-1,-1]
        q = []
        diff = float('inf')
        for i in range(left, right+1):
            if isPrime(i):
                q.append(i)
            while len(q) >= 2:
                print(q)
                if abs(q[0]-q[1]) < diff:
                    diff = abs(q[0]-q[1])
                    pair = [q[0],q[1]]
                    if diff <= 2:
                        return pair
                q.pop(0)
        return pair
                
                