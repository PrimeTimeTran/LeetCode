class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
          
        self.invertTree(root.left)
        self.invertTree(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp
        return root