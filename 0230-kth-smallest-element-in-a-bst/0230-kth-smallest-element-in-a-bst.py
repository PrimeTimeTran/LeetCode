'''
Perform iterative inorder traversal (left → node → right).
The stack stores ancestors while descending left; each pop visits the next
smallest node in sorted order, allowing us to count up to the k-th smallest.
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n, cur, stack = 0, root, []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n+=1
            if n == k: return cur.val
            cur = cur.right