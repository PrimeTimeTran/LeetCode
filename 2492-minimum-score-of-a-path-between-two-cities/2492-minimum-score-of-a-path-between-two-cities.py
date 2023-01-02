class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b, d in roads:
            g[a].append((b,d))
            g[b].append((a,d))
        
        self.res = float('inf')
        seen = set()
        
        def dfs(n):
            # if n in seen:
            #     return 
            seen.add(n)
            for des, d in g[n]:
                if des not in seen:
                    dfs(des)
                self.res = min(self.res, d)
        dfs(1)
        return self.res
    
        g = defaultdict(dict)
        for a,b,d in roads:
            g[a][b] = g[b][a] = d
            
        q = deque([1])
        res = float('inf')
        seen = set()
        while q:
            cur = q.popleft()
            for des, d in g[cur].items():
                if des not in seen:
                    seen.add(des)
                    q.append(des)
                res = min(res, d)
        
        return res