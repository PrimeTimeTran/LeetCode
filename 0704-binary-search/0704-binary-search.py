class Solution:
    def search(self, A: List[int], T: int) -> int:
        l, r = 0, len(A)-1
        
        while l<=r:
            m = (l+r) //2
            if A[m] == T: return m
            
            if A[m] > T:
                r = m - 1
            else:
                l = m + 1
            
        return -1