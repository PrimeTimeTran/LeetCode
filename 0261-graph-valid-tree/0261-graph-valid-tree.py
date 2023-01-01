class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = {i: [] for i in range(n)}
        
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        seen = set()
        
        def dfs(n, prev):
            if n in seen:
                return False
            seen.add(n)
            for nei in g[n]:
                if nei == prev:
                    continue
                if not dfs(nei, n): return False
            return True
        
        return dfs(0, -1) and len(seen) == n