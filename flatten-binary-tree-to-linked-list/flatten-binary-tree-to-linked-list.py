# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.previous_right = None
        def helper(root = root):
            if root:
                helper(root.right)
                helper(root.left)
                root.right, self.previous_right = self.previous_right, root
                root.left = None
        helper()
        
        if not root: return []

        res = []

        def dfs(n):
            if n:
                res.append(n.val)
                dfs(n.left)
                dfs(n.right)
        dfs(root)

        r = TreeNode(res.pop(0), None)
        while res:
            t = TreeNode(res.pop(0), None)
            t.left = None
            r.right = t
            r = t

        return r