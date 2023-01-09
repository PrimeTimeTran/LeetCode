"""
"""

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(n):
            if n:
                res.append(n.val)
                dfs(n.left)
                dfs(n.right)
                
        dfs(root) 
        return res