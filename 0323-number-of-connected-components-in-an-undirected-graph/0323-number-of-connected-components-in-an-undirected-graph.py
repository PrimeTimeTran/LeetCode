class Solution:
    def countComponents(self, N: int, edges: List[List[int]]) -> int:
        g = {i:[] for i in range(N)}
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        def dfs(n):
            if n in seen:
                return
            seen.add(n)
            for nei in g[n]:
                dfs(nei)
        res = 0
        seen = set()
        for n in range(N):
            if n not in seen:
                dfs(n)
                res += 1
        return res