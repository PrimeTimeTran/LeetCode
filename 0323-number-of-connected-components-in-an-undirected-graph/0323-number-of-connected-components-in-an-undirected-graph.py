class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            rx, ry = find(x), find(y)
            
            if parent[rx] != parent[ry]:
                parent[rx] = ry
            
        for x,y in edges:
            union(x,y)
        
        return len({find(x) for x in range(n)})