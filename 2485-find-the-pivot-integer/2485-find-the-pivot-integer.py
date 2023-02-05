class Solution:
    def pivotInteger(self, n: int) -> int:
        # return x if (x:=isqrt(x2:=n*(n+1)//2))**2 == x2 else -1 
        x = sqrt(n * (n + 1) // 2)
        return -1 if x % 1 else int(x)
