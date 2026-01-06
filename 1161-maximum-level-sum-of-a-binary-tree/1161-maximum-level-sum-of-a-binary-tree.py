# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        i, ans, cur_max = 0, 1, -inf
        q, res = deque([root]), []
        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                if cur:
                    level.append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            total = sum(level)
            if total > cur_max:
                cur_max = total
                ans = i + 1
            i+=1
        return ans