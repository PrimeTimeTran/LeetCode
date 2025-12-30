class Solution:
    def maxPathSum(self, root):
        self.res = root.val
        def dfs(n):
            if not n: return 0
            l, r = max(0, dfs(n.left)), max(0, dfs(n.right))
            self.res = max(self.res, n.val + l + r)
            return n.val + max(l, r)
        dfs(root)
        return self.res