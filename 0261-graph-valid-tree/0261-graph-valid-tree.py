'''
[0,1]
[0, 1, 2, 3, 4]

'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False

        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for x,y in edges:
            rx,ry = find(x), find(y)
            
            if rx == ry:
                return False
            
            parent[rx] = ry
            
        return True
            