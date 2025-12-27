# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        vals = []
        def dfs(n):
            if n:
                vals.append(str(n.val))
                dfs(n.left)
                dfs(n.right)
            else:
                vals.append('#')
        dfs(root)
        return ' '.join(vals)
        

    def deserialize(self, data):
        vals = iter(data.split())
        def dfs():
            v = next(vals)
            if v == '#': return
            n = TreeNode(v)
            n.left = dfs()
            n.right = dfs()
            return n
        return dfs()        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))