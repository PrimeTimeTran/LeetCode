class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        dir = 1
        q = deque([root])
        
        while q:
            level = []
            for _ in range(len(q)):
                c = q.popleft()    
                if c:
                    level.append(c.val)
                    if c.left:
                        q.append(c.left)
                    if c.right:
                        q.append(c.right)
            if level:
                res.append(level[::dir])
                dir *= (-1)
        return res
            
        
        
        