class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {0: [], 1: [TreeNode(0)]}
        
        def helper(n):
            if n not in memo:
                memo[n] = [TreeNode(0, left, right)
                           for i in range(1, n, 2)
                           for left in helper(i)
                           for right in helper(n - i - 1)]
            return memo[n]
        
        return helper(n)