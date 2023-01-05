'''
1. Constraints

2. Diagram


3. Pseudocode
Create graph using edges.
Create a topilogical sort using DFS and return it's reversed version.

'''

class Solution:
    def findOrder(self, N: int, P: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for a,b in P:
            g[a].append(b)
            
        seen = {}
        def dfs(n):
            if n in seen:
                return seen[n]
            seen[n] = False
            
            for nei in g[n]:
                if not dfs(nei): return False
            res.append(n)
            seen[n] = True
            return True
            
        res = []
        for c in range(N):
            if not dfs(c): return []
            
        return res