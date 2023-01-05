class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        seen = set()
        def dfs(n):
            if n in seen:
                return 
            seen.add(n)
            for nei in g[n]:
                dfs(nei)
        
        res = 0
        for n in range(n):
            if n not in seen:
                dfs(n)
                res+=1
        return res