class Solution:
    def findOrder(self, N: int, P: List[List[int]]) -> List[int]:
        res, g, seen = [], defaultdict(list), {}
        for u, v in P: g[u].append(v)
        def dfs(c):
            if c in seen: return seen[c]
            seen[c] = False
            if not all(dfs(p) for p in g[c]): return False
            seen[c] = True
            res.append(c)
            return True
        return [] if not all(dfs(c) for c in range(N)) else res 
