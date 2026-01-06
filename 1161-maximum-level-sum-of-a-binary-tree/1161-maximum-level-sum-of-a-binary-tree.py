# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
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
            if level:
                res.append(level)
        ans, cur_max = 1, -inf
        for i, level in enumerate(res):
            total = sum(level)
            if total > cur_max:
                cur_max = total
                ans = i + 1
        return ans

        