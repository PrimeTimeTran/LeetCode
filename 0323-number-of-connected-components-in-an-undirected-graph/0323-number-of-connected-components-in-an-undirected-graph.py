class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            nx, ny = find(x), find(y)
            if nx != ny:
                parent[nx] = ny
        
        for x,y in edges:
            union(x,y)
            
        return len({find(x) for x in range(n)})