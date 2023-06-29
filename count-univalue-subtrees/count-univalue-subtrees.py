# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(node, acc):
            if not node:
                return acc
            left = dfs(node.left, acc)
            right = dfs(node.right, acc)
            acc = left.union(right)
            acc.add(node.val)
            self.count += (len(acc) == 1)
            
            return acc
        
        dfs(root, set())
        
        return self.count