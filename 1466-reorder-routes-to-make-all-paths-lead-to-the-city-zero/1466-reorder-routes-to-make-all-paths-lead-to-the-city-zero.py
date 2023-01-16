'''
DFS
Create optimistic G usng connections. Create set, roads, of actual roads using connections.
DFS from 0 node checking if neighbor/city has road to n in roads. If not, increment res. 
Add city to seen to prevent loops and dfs it. Guard cycle by continuing on seen cities.
'''
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = defaultdict(list)
        
        for a,b in connections:
            g[a].append(b); g[b].append(a)
        
        self.res = 0
        seen = set([0])
        roads = {(a,b) for a,b in connections}
        
        def dfs(n):
            for c in g[n]:
                if c in seen: continue
                if (c,n) not in roads:
                    self.res +=1
                seen.add(c)
                dfs(c)
        dfs(0)        
        return self.res