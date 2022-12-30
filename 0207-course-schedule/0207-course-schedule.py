class Solution:
    def canFinish(self, N: int, pre: List[List[int]]) -> bool:
        g = {i: [] for i in range(N)}
        
        for a,b in pre:
            g[a].append(b)
        
        
        visit = set()
        def dfs(crs):
            if g[crs] == []:
                return True
            if crs in visit:
                return False
            visit.add(crs)
            
            for pre in g[crs]:
                if not dfs(pre): return False
            
            g[crs] = []

            return True
            
        
        
        for c in range(N):
            if not dfs(c): return False
            
        return True