class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        res = 0
        n = len(A)      
        seen = set()
        
        def dfs(i):
            for j, connected in enumerate(A[i]):
                if connected and j not in seen:
                    seen.add(j)
                    dfs(j)
        
        for i in range(n):
            if i not in seen:
                dfs(i)
                res+=1
        return res