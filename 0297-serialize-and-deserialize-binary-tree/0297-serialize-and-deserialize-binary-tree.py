class Codec:
    def serialize(self, root):
        vals = []
        def dfs(n):
            if n:
                vals.append(str(n.val))
                dfs(n.left)
                dfs(n.right)
            else:
                vals.append("#")
        dfs(root)
        return " ".join(vals)
    def deserialize(self, data):
        vals = iter(data.split())
        def dfs():
            val = next(vals)
            if val == '#': return
            n = TreeNode(val)
            n.left = dfs()
            n.right = dfs()
            return n
        return dfs()