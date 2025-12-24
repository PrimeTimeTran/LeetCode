class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(n, l, r):
            if not n: return True
            if not (n.val > l and n.val < r): return False
            return dfs(n.left, l, n.val) and dfs(n.right, n.val, r)
        return dfs(root, -inf, inf)