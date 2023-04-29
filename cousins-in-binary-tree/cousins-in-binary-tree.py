# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.xDepth = 0
        self.yDepth = 0
        self.xpar = None
        self.ypar = None
        def dfs(n, d, p):
            if n.val == x:
                self.xDepth = d
                self.xpar = p
                return
            if n.val == y:
                self.yDepth = d
                self.ypar = p
                return
            if n.left:
                dfs(n.left, d+1, n.val)
            if n.right:
                dfs(n.right, d+1, n.val)
        dfs(root, 1, root.val)
        return self.xDepth == self.yDepth and self.ypar != self.xpar