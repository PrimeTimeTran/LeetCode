# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        def dfs(items):
            if not items:
                return
            root = TreeNode(items[0])
            m = len(items)
            for i in range(1, len(items)):
                n = items[i]
                if n > root.val:
                    m = i
                    break
            root.left = dfs(items[1:m])
            root.right = dfs(items[m:])
            return root
        return dfs(preorder)

        # if not preorder:
        #     return None
        # root = TreeNode(preorder[0])
        # i = 1
        # while i < len(preorder) and preorder[i] < root.val:
        #     i += 1
        # root.left = self.bstFromPreorder(preorder[1:i])
        # root.right = self.bstFromPreorder(preorder[i:])
        # return root
        

# class Solution:
#     def bstFromPreorder(self, preorder):
#         self.i = 0
#         def dfs(bound=float('inf')):
#             if self.i == len(preorder) or preorder[self.i] > bound:
#                 return None
#             val = preorder[self.i]
#             self.i += 1
#             root = TreeNode(val)
#             root.left = dfs(val)
#             root.right = dfs(bound)
#             return root
#         return dfs()
