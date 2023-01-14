class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        g = defaultdict(list)
        for a, b in connections:
            g[a].append(b)
            g[b].append(a)
        
        seen = set()
        def dfs(n):
            if n in seen:
                return 0
            seen.add(n)
            for nei in g[n]:
                dfs(nei)
            return 1
        
        return sum(dfs(i) for i in range(n)) - 1
        
        