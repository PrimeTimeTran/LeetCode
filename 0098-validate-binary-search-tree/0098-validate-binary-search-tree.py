class Solution:
    def isValidBST(self, root):
        def valid(root):
            if not root:
                return (True, float('-inf'), float('inf'))

            left_res = valid(root.left)
            right_res = valid(root.right)

            if not left_res[0] or not right_res[0] or root.val <= left_res[1] or root.val >= right_res[2]:
                return (False, 0, 0)

            return (True, max(root.val, right_res[1]), min(root.val, left_res[2]) )
        self.prev = None
        return valid(root)[0]

    # The return result stores [True/False, max_so_far, min_so_far]
