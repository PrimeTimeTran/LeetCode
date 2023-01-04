class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(dict)
        for a,b,d in roads:
            g[a][b] = g[b][a] = d
            
        seen = set()
        self.res = float('infinity')
        def dfs(n):
            if n in seen:
                return
            seen.add(n)
            for nei, d in g[n].items():
                if nei not in seen:
                    dfs(nei)
                self.res = min(self.res, d)
        
        dfs(1)
        return self.res
        