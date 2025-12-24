'''
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

Recursively build tree nodes using preorder's 0 index.
Use the index of preorder[0] to identify which index to partition at for recursive calls(paritioning both preorder & inorder).
time: O(n) where n is the length of nodes in our tree
space: O(n) where n is the length of nodes in our tree
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return
        root = TreeNode(preorder[0])
        m = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:m+1], inorder[:m+1])
        root.right = self.buildTree(preorder[m+1:], inorder[m+1:])
        return root