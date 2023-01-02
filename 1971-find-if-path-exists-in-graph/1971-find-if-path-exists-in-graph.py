
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # s = source
        # d = destination
        # g = collections.defaultdict(list)
        # for a,b in edges:
        #     g[a].append(b)
        #     g[b].append(a)
        # vis = set()
        # def dfs(n):
        #     if n == d: return True
        #     if n in vis: return False
        #     vis.add(n)  
        #     for v in g[n]:
        #         if dfs(v): return True
        #     return False
        # return dfs(s)
    
        g = {i:[] for i in range(n)}
        
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            
        
        seen = set()
        
        def dfs(nei):
            if nei in seen:
                return False
            if nei == destination:
                return True
            seen.add(nei)
            for neighbor in g[nei]:
                if dfs(neighbor):
                    return True
            return False
        
        # for nei in g[source]:
        #     if dfs(nei):
        #         return True
        return dfs(source)
    
    