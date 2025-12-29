class Solution:
    def maxPathSum(self, root):
        self.res = root.val
        def dfs(n):
            if not n: return 0
            l, r = max(dfs(n.left), 0), max(dfs(n.right), 0)
            self.res = max(self.res, n.val + l + r)
            return n.val + max(l, r)
        dfs(root)
        return self.res