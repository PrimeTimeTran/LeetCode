class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def dfs(node):
            return dfs(node.left) | dfs(node.right) | {node.val} if node else set()
        q1 = dfs(root1)
        return any(target - a in q1 for a in dfs(root2))