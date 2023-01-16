'''
DFS
DFS from 0 node passing in previous node in each recursive call.
Guard cycles with a set and continue of nei == p. If DFS isn't successful, return false.
Return true if the loop completes with no return.

UF
Create parent list to hold representatives.
Define find, union,
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges): return False
        parent = [i for i in range(n)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]            
        
        for x,y in edges:
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[rx] = ry
        
        return True