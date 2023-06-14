# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        output = []
        self.inorder(root,output)
        mini_diff = float('inf')
        for i in range(1,len(output)):
            mini_diff = min(mini_diff,output[i]-output[i-1])
        return mini_diff
        
    def inorder(self,root,output):
        if root == None:
            return 
        else:
            self.inorder(root.left, output)
            output.append(root.val)
            self.inorder(root.right, output)