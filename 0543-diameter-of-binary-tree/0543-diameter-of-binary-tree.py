class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(n):
            if not n: return 0
            l, r = dfs(n.left), dfs(n.right)
            self.res = max(self.res, l + r)
            return 1 + max(l, r)
        dfs(root)
        return self.res