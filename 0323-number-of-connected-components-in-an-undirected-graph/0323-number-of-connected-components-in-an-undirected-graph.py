'''
Define find. Define union. Union with edges and return len of set found items.

'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            rx,ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
        
        
        for x,y in edges:
            union(x,y)
        
        
        return len({find(i) for i in range(n)})