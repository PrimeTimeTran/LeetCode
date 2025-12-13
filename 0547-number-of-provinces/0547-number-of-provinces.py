class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        def union(x, y):
            parent[find(x)] = find(y)
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    union(i, j)
        return len({find(i) for i in range(n)})
        