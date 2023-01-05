'''
target = 6
pos = 6
speed = -2
moves = 5

AAARA


BFS

'''

class Solution:
    def racecar(self, target: int) -> int:
        # moves, speed, pos
        q = deque([[0,1,0]])
        
        while q:
            moves, speed, pos = q.popleft()
            
            # Check if pos == target, if so return
            if pos == target:
                return moves
            
            q.append([moves+1, speed*2, pos+speed])
            
            # Check if past target, if so, reverse direction
            if pos+speed > target and speed > 0 or pos+speed < target and speed < 0:
                speed = -1 if speed > 0 else 1
                
                q.append([moves+1, speed, pos])
            