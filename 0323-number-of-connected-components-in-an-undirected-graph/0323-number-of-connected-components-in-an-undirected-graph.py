class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        def find(p):
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry 
        
        for x, y in edges:
            union(x, y)
        return len({find(i) for i in range(n)})