class Solution:
    def canFinish(self, N: int, P: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in P:
            g[a].append(b)
        seen = {}
        def dfs(n):
            if n in seen: return seen[n]
            seen[n] = False
            for p in g[n]:
                if not dfs(p): return False
            seen[n] = True
            return True
        for i in range(N):
            if not dfs(i):
                return False
        return True
