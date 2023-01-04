'''
len(edges) == n - 1
No cycles



Union find or DFS




'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        parent = {i:i for i in range(n)}
        
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
        
        
        
        g = defaultdict(list)
        
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        seen = set()
        def dfs(n, p):
            if n in seen:
                return False
            seen.add(n)
            
            for nei in g[n]:
                if nei == p: continue
                if not dfs(nei, n): return False
                    
            return True
        
        return dfs(0,-1) and len(seen) == n