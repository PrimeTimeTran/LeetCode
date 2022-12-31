'''
1. Constraints
We're given n which is the numbeer of nodes and edges which represents their edges.

We return an integer.


2. Diagram

3. Pseudocode

Create graph using edges.

Iterate over all nodes.
    Process each node if node hasn't been processed. 
        Process node's neighbors.
    Increment count
Return the count of times processes
    

'''

class Solution:
    def countComponents(self, N: int, edges: List[List[int]]) -> int:
        g = {i:[] for i in range(N)}
        
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        count = 0
        seen = set()
        def dfs(n):
            if n in seen:
                return
            seen.add(n)
            
            for nei in g[n]:
                dfs(nei)
        
        for n in range(N):
            if not n in seen:
                dfs(n)
                count+=1
        return count