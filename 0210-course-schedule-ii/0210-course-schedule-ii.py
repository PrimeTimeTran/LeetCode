class Solution:
    def findOrder(self, N: int, P: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        
        for a,b in P:
            g[a].append(b)
            
        res, seen = [], {}
        def dfs(n):
            if n in seen:
                return seen[n]
            seen[n] = False
            for p in g[n]:
                if not dfs(p): return False
            seen[n] = True
            res.append(n)
            return True
        
        for c in range(N):
            if not dfs(c): return []
        
        return res