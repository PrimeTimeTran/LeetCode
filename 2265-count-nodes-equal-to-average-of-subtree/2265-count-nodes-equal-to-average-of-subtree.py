class Pair(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.count = 0

        def postOrder(root):
            if root is None:
                return Pair(0, 0)

            left = postOrder(root.left)
            right = postOrder(root.right)

            total_sum = left.first + right.first + root.val
            node_count = left.second + right.second + 1

            if total_sum // node_count == root.val:
                self.count += 1

            return Pair(total_sum, node_count)

        postOrder(root)

        return self.count