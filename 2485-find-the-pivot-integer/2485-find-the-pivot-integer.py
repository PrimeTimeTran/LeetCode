class Solution:
    def pivotInteger(self, n: int) -> int:
        return x if (x:=isqrt(x2:=n*(n+1)//2))**2 == x2 else -1 
      