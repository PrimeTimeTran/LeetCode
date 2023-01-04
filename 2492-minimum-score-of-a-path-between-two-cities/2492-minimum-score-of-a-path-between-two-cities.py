'''
DFS: 
From node one traverse through neighbors using adj list comparing roads to find the minimum score road.
Guard against cycles by checking if road seen with a set.

'''

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b,d in roads:
            g[a].append((b,d))
            g[b].append((a,d))
            
            
        seen = set()
        self.res = float('infinity')
        
        def dfs(n):
            if n in seen:
                return
            seen.add(n)
            for nei, d in g[n]:
                if nei not in seen:
                    dfs(nei)
                self.res = min(self.res, d)
        
        dfs(1)
        return self.res
        
        
        