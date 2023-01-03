class Solution:
    def validTree(self, n, edges):
        if n - 1 != len(edges):
            return False
        parent = {i: i for i in range(n)}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for x, y in edges:
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[rx] = ry
        return True