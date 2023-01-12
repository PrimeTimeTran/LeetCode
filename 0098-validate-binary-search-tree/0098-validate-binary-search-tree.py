class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(n, l, r):
            if not n:
                return True

            if n.val > l and n.val < r:
                return valid(n.left, l, n.val) and valid(n.right, n.val, r)
            return False

        return valid(root, float('-inf'), float('inf'))
