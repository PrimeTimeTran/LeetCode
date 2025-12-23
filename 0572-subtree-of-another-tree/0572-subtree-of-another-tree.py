class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root:
            if self.isSameTree(root, subRoot): return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not (p and q and p.val == q.val): return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)