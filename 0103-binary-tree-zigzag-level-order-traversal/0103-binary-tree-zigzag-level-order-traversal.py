'''
if not root: return []
queue = deque([root])
result, direction = [], 1

while queue:
    level = []
    for i in range(len(queue)):
        node = queue.popleft()
        level.append(node.val)
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
    result.append(level[::direction])
    direction *= (-1)
return result
'''
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
        print(res)
        return res
            
        
        
        