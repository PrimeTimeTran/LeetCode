class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        
        for a, b in edges:
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
        for i in range(n):
            if i not in seen:
                dfs(i)
                res+=1
        return res