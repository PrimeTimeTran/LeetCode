class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        def union(x,y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY: return False
            parent[rootX] = rootY
            return True
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]