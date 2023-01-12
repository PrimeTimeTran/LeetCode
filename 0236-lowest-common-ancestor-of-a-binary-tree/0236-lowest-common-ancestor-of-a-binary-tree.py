'''

'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def pqLCA(root):
            if root in (None, p, q):
                return root
            left = pqLCA(root.left)
            right = pqLCA(root.right)
            return root if left and right else left or right
        return pqLCA(root)