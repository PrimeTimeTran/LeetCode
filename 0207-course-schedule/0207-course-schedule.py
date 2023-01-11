'''
Create graph using edges. Loop over courses for classes we cannot finish using a DFS.
DFS checks class has no prerequisite, hasn't been seen, and adds if True to both. 
Next it recursively DFS on it's prerequisites. If recurse True up, it sets prerequisites to []
and returns true.






'''
class Solution:
    def canFinish(self, N: int, P: List[List[int]]) -> bool:
        g = defaultdict(list)

        for a, b in P:
            g[a].append(b)
        
        seen = set()
        def dfs(n):
            if g[n] == []:
                return True
            if n in seen:
                return False
            
            seen.add(n)
            for pre in g[n]:
                if not dfs(pre): return False
                
            g[n] = []
            return True
        
        for c in range(N):
            if not dfs(c): return False
        
        return True