"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(r):
            if not r:
                return None
            
            for nei in r.children:
                dfs(nei)
            res.append(r.val)
        dfs(root)
        return res