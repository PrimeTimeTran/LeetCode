class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        
        for u,v,w in roads:
            g[u].append((v,w)); g[v].append((u,w))
            
        seen, self.res = set(), inf
        def dfs(u):
            if u in seen:
                return
            seen.add(u)
            for v, w in g[u]:
                if v not in seen:
                    dfs(v)
                self.res = min(self.res, w)
        
        dfs(1)
        return self.res
            