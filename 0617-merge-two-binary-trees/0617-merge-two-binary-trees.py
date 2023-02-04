# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        if p and q:
            r = TreeNode(p.val+q.val)
            r.left = self.mergeTrees(p.left, q.left)
            r.right = self.mergeTrees(p.right,q.right)
            return r
        else: 
            return p or q