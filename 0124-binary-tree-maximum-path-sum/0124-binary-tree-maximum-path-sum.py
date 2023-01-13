# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def onePath(n):
            if not n:
                return 0
            l = max(onePath(n.left), 0)
            r =  max(onePath(n.right), 0) 
            self.res = max(self.res, l+r+n.val)
            return n.val+max(l,r)
        
        onePath(root)
        return self.res