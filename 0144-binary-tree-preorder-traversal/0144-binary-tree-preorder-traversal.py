# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
root, left, right

res, helper method

        10
      /    \
     5      15
   /  \    /   \  
  1    3  11    16

10,5,1,3,15,11,16

recursion
check if n
    if n, add to res
    call helper method with left
    call helper method with right

return res

"""

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # def dfs(n):
        #     if n:
        #         res.append(n.val)
        #         dfs(n.left)
        #         dfs(n.right)
        # dfs(root)
    
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
        return res



