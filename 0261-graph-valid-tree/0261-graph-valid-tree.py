'''
DFS
DFS from root node marking nodes seen as we go. Pass in previous to prevent a loop
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(list)
        
        for a,b in edges:
            g[a].append(b); g[b].append(a)
        
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