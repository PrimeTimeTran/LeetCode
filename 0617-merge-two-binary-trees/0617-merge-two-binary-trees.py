# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        # if p and q:
        #     root = TreeNode(p.val + q.val)
        #     root.left = self.mergeTrees(p.left, q.left)
        #     root.right = self.mergeTrees(p.right, q.right)
        #     return root
        # else:
        #     return p or q
        
        if p and q:
            c = TreeNode(p.val + q.val)
            c.left = self.mergeTrees(p.left, q.left)
            c.right = self.mergeTrees(p.right, q.right)
            return c
        else:
            return p or q
            
