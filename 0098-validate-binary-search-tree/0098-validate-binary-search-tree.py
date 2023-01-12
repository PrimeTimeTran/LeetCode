class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.validBSTPostOrderHelper(root)[0]

    # The return result stores [True/False, max_so_far, min_so_far]
    def validBSTPostOrderHelper(self, root):
        if not root:
            return (True, float('-inf'), float('inf'))

        left_res = self.validBSTPostOrderHelper(root.left)
        right_res = self.validBSTPostOrderHelper(root.right)

        if not left_res[0] or not right_res[0] or root.val <= left_res[1] or root.val >= right_res[2]:
            return (False, 0, 0)

        return (True, max(root.val, right_res[1]), min(root.val, left_res[2]) )