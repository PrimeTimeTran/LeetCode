# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    res = []
    levels = self.level(root)
    for item in levels:
      res.append(sum(item))
    print(res)
    
    return res.index(max(res)) + 1
    
  def level(self, root):
    res = []
    q = deque([root])
    
    while q:
      lvl = []
      for _ in range(len(q)):
        cur = q.popleft()
        if cur:
          lvl.append(cur.val)
          if cur.left:
            q.append(cur.left)
          if cur.right:
            q.append(cur.right)
      if lvl:
        res.append(lvl)
    return res
        