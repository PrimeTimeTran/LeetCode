'''
BFS
BFS through all combinations stopping on deadends. Add neighbors to Q.
Find neighbors by traversing code index's and adding both -1 and 1, 
yielding the codes with new val injected.

Increment res once for each layer

'''

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(code):
            for i in range(4):
                x = int(code[i])
                for diff in [1,-1]:
                    y = (x+diff+10) % 10
                    yield code[:i]+str(y)+code[i+1:]
            
        deadSet = set(deadends)
        if "0000" in deadSet: return -1
        q = deque(["0000"])
        steps = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target: return steps
                for nei in neighbors(cur):
                    if nei in deadSet: continue
                    deadSet.add(nei)
                    q.append(nei)

            steps+=1

        return -1