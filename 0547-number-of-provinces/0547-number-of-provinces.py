class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        res = 0 
        N = len(A)
        seen = set()
        
        def dfs(n):
            for i, nei in enumerate(A[n]):
                if nei and i not in seen:
                    seen.add(i)
                    dfs(i)
        
        
        for n in range(N):
            if n not in seen:
                dfs(n)
                res+=1
        return res