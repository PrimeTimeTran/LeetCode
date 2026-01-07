# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.res = total = 0
        def dfs(n):
            if not n: return 0
            l,r = dfs(n.left), dfs(n.right)
            self.res = max(self.res, l * (total - l), r * (total-r))
            return n.val + l + r
        total = dfs(root)
        dfs(root)
        return self.res % (10**9 + 7)