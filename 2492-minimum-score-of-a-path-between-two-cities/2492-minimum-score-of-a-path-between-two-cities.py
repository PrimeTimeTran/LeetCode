class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(dict)
        for a,b, d in roads:
            g[a][b] = g[b][a] = d
        
        self.res = float('inf')
        seen = set()
        
        
        def dfs(n):
            if n in seen:
                return 
            seen.add(n)
            for des, d in g[n].items():
                if des not in seen:
                    dfs(des)
                self.res = min(self.res, d)
            
        dfs(1)
        
        return self.res