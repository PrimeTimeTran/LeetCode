class Solution:
    def goodNodes(self, n: TreeNode, minimum=-inf) -> int:
        if not n: return 0
        newMax = max(minimum, n.val)
        l, r = self.goodNodes(n.left, newMax), self.goodNodes(n.right, newMax)
        return l + r + (n.val >= minimum)