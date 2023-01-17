class Solution:
    def racecar(self, target: int) -> int:
        # pos, speed, moves
        q = deque([[0, 1, 0]])
        
        
        while q: 
            m, s, p  = q.popleft()
            
            if p == target: return m
            
            q.append([m+1, s*2, p+s])
            
            passed = p+s > target and s > 0 or p+s < target and s < 0
            if passed:
                s = -1 if s > 0 else 1
                q.append([m+1, s, p])