class Solution:
    def canFinish(self, N: int, P: List[List[int]]) -> bool:
        g = defaultdict(list)
        
        for a, b in P:
            g[a].append(b)
            
        seen = set()
        def dfs(n):
            if g[n] == []:
                return True
            if n in seen:
                return False
            seen.add(n)
            for nei in g[n]:
                if not dfs(nei): return False
            g[n] = []
            return True
        
        for c in range(N):
            if not dfs(c): return False
        return True