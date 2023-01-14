class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = [i for i in range(n)]
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        def union(x,y):
            nx, ny = find(x), find(y)
            if nx != ny:
                p[nx] = ny
        
        
        for x, y in edges:
            union(x,y)
            
        return len({find(x) for x in range(n)})