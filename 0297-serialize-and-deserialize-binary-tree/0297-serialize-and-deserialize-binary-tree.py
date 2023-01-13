# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        vals = [] 
        def doit(n):
            if n:
                vals.append(str(n.val))
                doit(n.left)
                doit(n.right)
            else:
                vals.append('#')
        doit(root)
        return " ".join(vals)

    def deserialize(self, data):
        vals = data.split()
        def doit(vals):
            v = vals.pop(0)
            if v == '#': return
            root = TreeNode(v)
            root.left = doit(vals)
            root.right = doit(vals)
            return root
        return doit(vals)