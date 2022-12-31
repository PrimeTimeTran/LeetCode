class Solution:
    def countComponents(self, N: int, edges: List[List[int]]) -> int:
        g = {i:[] for i in range(N)}
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        count = 0
        seen = set()
        def dfs(n):
            if n in seen:
                return
            seen.add(n)
            for nei in g[n]:
                dfs(nei)
        for n in range(N):
            if not n in seen:
                dfs(n)
                count+=1
        return count