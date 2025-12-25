# Using a loop check if we can travel down the tree either left or right.
# In order to go down the left our cur.val must be > p.val and q.val
# To go down the right our cur.val must be < p.val and q.val
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            val = root.val
            if val > p.val and val > q.val:
                root = root.left
            elif val < p.val and val < q.val:
                root = root.right
            else:
                return root