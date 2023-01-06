class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b in connections:
            g[a].append(b)
            g[b].append(a)
            
        seen = set()
        seen.add(0)
        self.res = 0
        roads = {(a,b) for a,b in connections}
        def dfs(n):
            for nei in g[n]:
                if nei in seen: continue
                if (nei,n) not in roads:
                    self.res += 1
                seen.add(nei)
                dfs(nei)
        
        dfs(0)
        return self.res