class Solution:
    def goodNodes(self, n: TreeNode, minimum=-inf) -> int:
        return self.goodNodes(n.left, max(minimum, n.val)) + self.goodNodes(n.right, max(minimum, n.val)) + (n.val >= minimum) if n else 0