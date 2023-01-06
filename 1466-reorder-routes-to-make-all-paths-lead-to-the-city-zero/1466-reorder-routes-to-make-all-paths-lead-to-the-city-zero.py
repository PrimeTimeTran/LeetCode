'''
DFS
Use undirected graph compared to given graph/adj list to identify how many roads we're missing.
'''

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = defaultdict(list)        
        
        for a,b in connections:
            g[a].append(b)
            g[b].append(a)
            
        seen = set()
        self.res = 0
        roads = {(a,b) for a, b in connections}
        def dfs(n):
            for nei in g[n]:
                if nei in seen: continue
                if (nei, n) not in roads:
                    self.res +=1
                seen.add(nei)
                dfs(nei)
        seen.add(0)
        dfs(0)
        
        return self.res