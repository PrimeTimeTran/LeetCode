class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q, res = [root], []
        while q: 
            level = []
            for _ in range(len(q)):
                cur = q.pop(0)
                if cur:
                    level.append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            if level:
                res.append(level)
        return res