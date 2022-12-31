"""
- Copy Node

- Copy neighbors, append neighbors to copy

- Return copy

"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        seen = {}
        def dfs(n):
            if n in seen:
                return seen[n]
            copy = Node(n.val)
            seen[n] = copy
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
                
            return copy
        
        return dfs(node) if node else None