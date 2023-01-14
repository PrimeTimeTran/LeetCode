class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        G = [set() for i in range(n)]
        for i, j in connections:
            G[i].add(j)
            G[j].add(i)
        seen = set()

        def dfs(i):
            if i in seen: return 0
            seen.add(i)
            for j in G[i]: dfs(j)
            return 1

        return sum(dfs(i) for i in range(n)) - 1