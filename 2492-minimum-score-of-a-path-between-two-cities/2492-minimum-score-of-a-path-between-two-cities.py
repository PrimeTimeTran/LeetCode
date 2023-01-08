'''
Because we can visit vertices and edges multiple times we simply search for the min road
in the path connected to 1. We're guaranteed to have one path from 1 to n.

DFS / BFS
Use G traversal updating min on every edge.
'''

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        
        for u,v,w in roads:
            g[u].append((v,w))
            g[v].append((u,w))
        
        self.res, seen = inf, set()
        def dfs(n):
            if n in seen:
                return
            for nei, w in g[n]:
                if nei not in seen:
                    seen.add(n)
                    dfs(nei)
                    
                self.res = min(self.res, w)
        dfs(1)
        return self.res
        
        