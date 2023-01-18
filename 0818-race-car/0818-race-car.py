class Solution:
    def racecar(self, target: int) -> int:
        # pos, speed, moves
        q = deque([[0,1,0]])
        
        
        while q:
            p, s, m = q.popleft()
            if p == target: return m
            
            q.append([p+s,s*2,m+1])
            if p+s > target and s > 0 or p+s < target and s < 0:
                s = -1 if s > 0 else 1
                q.append([p,s,m+1])