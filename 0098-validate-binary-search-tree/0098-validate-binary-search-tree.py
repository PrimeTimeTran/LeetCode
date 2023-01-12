class Solution:
    def isValidBST(self, root):
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
