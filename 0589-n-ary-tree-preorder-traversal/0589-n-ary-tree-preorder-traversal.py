"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(r):
            if not r:
                return None
            res.append(r.val)
            for nei in r.children:
                dfs(nei)
        dfs(root)
        return res