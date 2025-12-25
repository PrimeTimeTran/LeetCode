class Solution:
    def rightSideView(self, root):
        res = []
        def dfs(n, depth):
            if not n:
                return
            if depth == len(res):
                res.append(n.val)
            dfs(n.right, depth+1)
            dfs(n.left, depth+1)
        dfs(root, 0)
        return res