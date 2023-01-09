'''
Because we can visit cities and roads multiple times we search for the min road
any path connected to 1. We're guaranteed to have one path from 1 to n.

DFS
Use G traversal updating min every item. Guard for cycles and move from node to neighbor
using the adj list.

min 5
cur 3


BFS
Use G traversal updating min on every edge. Guard cycles by only adding unseen nodes to q after marking complete.
'''

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        
        for u, v, w in roads:
            g[u].append((v,w))
            g[v].append((u,w))
            
        seen, self.res = set(), inf
        def dfs(n):
            if n in seen:
                return
            seen.add(n)
            for v, dis in g[n]:
                if v not in seen:
                    dfs(v)
                self.res = min(self.res, dis)
        dfs(1)
        return self.res