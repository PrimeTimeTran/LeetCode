class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b in connections:
            g[a].append(b)
            g[b].append(a)
        
        self.res = 0
        roads = {(a,b) for a,b in connections}
        seen = set([0])
        def dfs(n):
            for c in g[n]:
                if c in seen:
                    continue
                if (c,n) not in roads:
                    self.res+=1
                seen.add(c)
                dfs(c)
                
        
        dfs(0)
        return self.res