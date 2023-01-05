'''
Create a graph using roads. 
DFS from node 1 looking for smallest score road.

'''

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        
        for a,b,d in roads:
            g[a].append((b,d))
            g[b].append((a,d))
        
        self.res = inf
        seen = set()
        def dfs(n):
            if n in seen:
                return
            for nei, d in g[n]:
                if nei not in seen:
                    seen.add(n)
                    dfs(nei)
                self.res = min(self.res, d)
        
        dfs(1)
        return self.res