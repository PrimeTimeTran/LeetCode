class Solution:
    def pivotInteger(self, n: int) -> int:
        return x if (x:=isqrt(x2:=n*(n+1)//2))**2 == x2 else -1 
        
        total = n * (n + 1) // 2
        res = 0
        
        for i in range(1, n + 1):
            total -= i - 1
            res += i
            
            if res == total:
                return i
        return -1