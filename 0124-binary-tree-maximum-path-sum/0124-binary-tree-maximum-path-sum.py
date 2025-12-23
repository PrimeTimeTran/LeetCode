class Solution:
  def maxPathSum(self, root):
    self.ans = root.val
    def maxSum(root):
      if not root:
          return 0
      l, r = max(maxSum(root.left), 0), max(maxSum(root.right), 0)
      self.ans = max(self.ans, root.val + l + r)
      return root.val + max(l, r)
    maxSum(root)
    return self.ans