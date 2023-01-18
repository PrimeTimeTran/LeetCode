'''
BFS
BFS neighbors of input code comparing to target. If target == code return steps.
Find neighbors of a code using it's index and diff of [-1,1] and modulo trick.
yielding the codes with new val injected inside.
'''

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(code):
            for i in range(4):
                x = int(code[i])
                for diff in [-1,1]:
                    y = (x+diff+10) % 10
                    yield code[:i]+str(y)+code[i+1:]
        
        dead = set(deadends)
        if '0000' in dead: return -1
        steps, q = 0, deque(['0000'])
        
        while q:
            for _ in range(len(q)):
                code = q.popleft()
                if code == target: return steps
                for nei in neighbors(code):
                    if nei not in dead:
                        dead.add(nei)
                        q.append(nei)
            steps+=1
        return -1
        