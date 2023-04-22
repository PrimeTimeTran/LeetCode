class Solution:
    def canFinish(self, N: int, pre: List[List[int]]) -> bool:
        g = {n:[] for n in range(N)}
        for a,b in pre:
            g[a].append(b)
        seen = set()        
        def dfs(c):
            if g[c] == []:
                return True
            if c in seen:
                return False
            seen.add(c)
            for pre in g[c]:
                if not dfs(pre): return False
            g[c] = []
            return True
        for c in range(N):
            if not dfs(c): return False
        return True