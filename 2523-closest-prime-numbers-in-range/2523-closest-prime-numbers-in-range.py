def isPrime(num):
    flag = False
    if num == 1:
        print(num, "is not a prime number")
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if flag:
            return False
        else:
            return True
        
        
def primesBetween(a, b):
    primes = []
    if (a == 1):
        a+=1
        if (b >= 2):
            a+=1
    if (a == 2):
        print(a,end=" ")
     
    if (a % 2 == 0):
        a+=1
    for i in range(a,b+1,2):
        flag = 1
        j = 2
        while(j * j <= i):
            if (i % j == 0):
                flag = 0
                break
            j+=1
        if (flag == 1):
            primes.append(i)
    return primes

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def solve(start, end):
            prime = [True for i in range(end + 1)] # initially mark all numbers as prime
            p = 2
            
            while(p * p <= end):
                if prime[p]:
                    for i in range(p * p, end + 1, p):
                        prime[i] = False # mark all multiples except for the first number as non-prime
                p += 1
            
            res = deque()
            ans = []
            
            for p in range(max(2, start), end + 1):
                if prime[p]:
                    res.append(p)
                    if len(res) == 2:
                        ans.append((res[1] - res[0],  res[0], res[1]))
                        res.popleft()
            ans.sort()
            return (ans[0][1],ans[0][2]) if ans else [-1, -1]
        
        return solve(left, right)