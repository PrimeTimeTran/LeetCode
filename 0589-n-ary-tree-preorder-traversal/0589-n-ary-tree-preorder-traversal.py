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
        def dfs(n):
            if not n: return
            res.append(n.val)
            for nei in n.children:
                dfs(nei)
                
        dfs(root)
        return res