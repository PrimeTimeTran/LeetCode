class Solution:
    def findOrder(self, N: int, P: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        
        for a,b in P:
            g[a].append(b)
        
        res, seen = [], {}
        def dfs(c):
            if c in seen:
                return seen[c]
            seen[c] = False
            for nei in g[c]:
                if not dfs(nei): return False
            seen[c] = True
            res.append(c)
            return True
            
        for c in range(N):
            if not dfs(c): return []
        
        return res