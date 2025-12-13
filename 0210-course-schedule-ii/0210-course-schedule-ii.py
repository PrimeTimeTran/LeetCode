class Solution:
    def findOrder(self, N: int, P: List[List[int]]) -> List[int]:
        seen, g, res = {}, defaultdict(list), []
        for a, b in P: g[a].append(b)
        def dfs(n):
            if n in seen: return seen[n]
            seen[n] = False
            for pre in g[n]:
                if not dfs(pre):
                    return False
            seen[n] = True
            res.append(n)
            return seen[n]
        for i in range(N):
            if not dfs(i):
                return []
        return res