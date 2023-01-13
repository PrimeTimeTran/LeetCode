'''
Check left node smaller and right node larger of every parent in tree.
Preorder: Action, Left, Right
Inorder: Left, Action, Right
Postorder: Left, Right, Action
'''
class Solution:
    def isValidBST(self, root):
        # PRE
#         def valid(n, left, right):
#             if not n: return True
            
#             if n.val > left and n.val < right:
#                 return valid(n.left, left, n.val) and valid(n.right, n.val, right)
#             return False
                
#         return valid(root, -inf, inf)

        # POST
        def valid(n, left, right):
            if not n: return True

            leftValid = valid(n.left, left, n.val)
            rightValid = valid(n.right, n.val, right)
            
            if not leftValid or not rightValid:
                return False

            if n.val > left and n.val < right:
                return True 
            return False
        
        return valid(root, -inf, inf)
