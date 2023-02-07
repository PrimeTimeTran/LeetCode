class Solution:
    def canFinish(self, N: int, P: List[List[int]]) -> bool:
        g = defaultdict(list)
        
        for a, b in P:
            g[a].append(b)
            
        vis = set()
        def dfs(c):
            if g[c] == []: return True
            if c in vis:
                return False 
            vis.add(c)
            for nei in g[c]:
                if not dfs(nei): return False
            g[c] = []
            return True
        
        for i in range(N):
            if not dfs(i): return False
                
        return True