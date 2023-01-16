'''
DFS
Create complete G usng connections. Create set, roads, of actual roads using connections.
DFS from 0 node checking if neighbor/city has road to n in roads. If not, increment res. 
Add city to seen to prevent loops and dfs it. Guard cycle by continuing on seen cities.
'''
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b in connections:
            g[a].append(b)
            g[b].append(a)
            
        roads = {(a,b) for a,b in connections}
        self.res = 0
        seen = set([0])
        def dfs(n):
            for nei in g[n]:
                if nei in seen: continue
                if (nei,n) not in roads:
                    self.res += 1
                seen.add(nei)
                dfs(nei)
        dfs(0)
        return self.res