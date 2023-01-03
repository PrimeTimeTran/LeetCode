# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def dfs(n, v):                                                 # a recursive function for the
            if n: dfs(n.left, v), v.append(n.val), dfs(n.right, v)     # inorder traversal of BST
        
        nums = []                                                      # [1] collect values from BST  
        dfs(root, nums)                                                #     in sorted order
        
        results, n = [], len(nums)
        
        for q in queries:                                              # [2] make queries using the binary
            i = bisect_left(nums, q)                                   #     search, then consider several
            if i < n and nums[i] == q : results.append([q,q])          #     conditions on the returned 
            else:                                                      #     insertion position
                if   i == 0 : results.append([-1,nums[0]])
                elif i == n : results.append([nums[-1],-1])
                else        : results.append([nums[i-1], nums[i]])
                    
        return results