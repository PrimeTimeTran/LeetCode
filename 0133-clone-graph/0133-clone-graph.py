"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        seen = {}
        def dfs(n):
            if n in seen:
                return seen[n]
            c = Node(n.val)
            seen[n] = c
            for nei in n.neighbors:
                c.neighbors.append(dfs(nei))
            return c
            
        return dfs(node) if node else None