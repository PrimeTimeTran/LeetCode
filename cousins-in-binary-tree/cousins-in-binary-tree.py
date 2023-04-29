# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root, x, y):
        def dept(node, d, par):
            if not node: return 
			# if we find node with value x, then keep its depth and parent in a and aparent variables
            if node.val == x:
                self.a = d
                self.aparent= par
			# if we find node with value y, then keep its depth and parent in b and bparent variables
            elif node.val == y:
                self.b = d
                self.bparent= par
            dept(node.left, d+1, node)
            dept(node.right, d+1, node)
        dept(root, 0, None)
        # return True if a and b are equal and their parents are not same
        return self.a == self.b and self.aparent != self.bparent