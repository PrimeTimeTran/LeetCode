class Solution:
    def racecar(self, target: int) -> int:
        q = deque([[0,0,1]])
        while q:
            move, pos, speed = q.popleft()
            if pos == target:
                return move
            q.append([move+1, pos+speed, speed*2])
            if pos+speed > target and speed > 0 or pos+speed < target and speed < 0:
                speed = -1 if speed > 0 else 1
                q.append([move+1,pos,speed])
            