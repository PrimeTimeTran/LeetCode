"""
"""

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def dfs(n):
            if n:
                self.res.append(n.val)
                
                dfs(n.left)
                dfs(n.right)
                
        dfs(root)
        return self.res