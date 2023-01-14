# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def dfs(n):
            if not n:
                return 0
            l = max(dfs(n.left), 0)
            r = max(dfs(n.right), 0)
            self.res = max(self.res, n.val + l + r)
            return max(l,r)+ n.val
        dfs(root)
        return self.res