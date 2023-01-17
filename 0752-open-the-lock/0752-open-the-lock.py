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
                for dir in [-1,1]:
                    y = (dir+x+10) % 10
                    yield code[:i]+ str(y)+code[i+1:]
        deadSet = set(deadends)
        if "0000" in deadSet: return -1
        q = deque(["0000"])
        steps = 0
        while q:
            for _ in range(len(q)):
                code = q.popleft()
                if code == target: return steps
                for nei in neighbors(code):
                    if nei not in deadSet:
                        deadSet.add(nei)
                        q.append(nei)
            steps+=1
        return -1
    