# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder: return None
        n = TreeNode(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < n.val:
            i+=1
        n.left = self.bstFromPreorder(preorder[1:i])
        n.right = self.bstFromPreorder(preorder[i:])
        return n