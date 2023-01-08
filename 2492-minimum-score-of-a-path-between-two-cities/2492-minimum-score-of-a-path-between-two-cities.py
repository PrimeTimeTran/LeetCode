'''
Because we can visit cities and roads multiple times we search for the min road
any path connected to 1. We're guaranteed to have one path from 1 to n.

DFS
Use G traversal updating min on every edge. Guard for cycles and move from node to neighbor
using the adj list.

BFS
Use G traversal updating min on every edge. Guard cycles

'''

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        
        for u,v,w in roads:
            g[u].append((v,w))
            g[v].append((u,w))
        
        # self.res, seen = inf, set()
        # def dfs(n):
        #     if n in seen:
        #         return
        #     seen.add(n)
        #     for nei, w in g[n]:
        #         if nei not in seen:
        #             dfs(nei)
        #         self.res = min(self.res, w)
        # dfs(1)
        q = deque([1])
        seen = set()
        self.res = inf
        while q:
            u = q.popleft()
            for v, d in g[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
                self.res = min(self.res, d)
        
        return self.res
        
        