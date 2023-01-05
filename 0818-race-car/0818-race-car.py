'''

'''

class Solution:
    def racecar(self, target: int) -> int:
        # moves, speed, pos
        q = deque([[0,1,0]])
        
        while q:
            moves, speed, pos = q.popleft()
            
            if pos == target:
                return moves
            
            q.append([moves+1, speed*2, pos+speed])
            
            overshotTarget = pos+speed > target and speed > 0 or pos+speed < target and speed < 0
            if overshotTarget:
                speed = -1 if speed > 0 else 1
                q.append([moves+1, speed, pos])
            