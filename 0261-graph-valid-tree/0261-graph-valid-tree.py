class Solution:
    def validTree(self, n, edges):
        if n - 1 != len(edges):
            return False
        parent = {i: i for i in range(n)}
        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]

        for x, y in edges:
            set1, set2 = find(x), find(y)
            if set1 == set2:
                return False
            parent[set1] = set2

        return True