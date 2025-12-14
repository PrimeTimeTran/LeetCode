class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY: return False
            parent[rootX] = rootY
            return True
        for u, v in edges:
            if not union(u,v):
                return [u, v]