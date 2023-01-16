'''
DFS
Create G and DFS from headID. Return DFS call to headID an return local max in recursive DFS

BFS 
Create G and then BFS with accumulated time and manager node. Use manager node + time on each append to calculate
how long it takes to tell this employee. Update global max with each item.
'''
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        for v, u in enumerate(manager):
            g[u].append(v)
            
        res = 0
        q = deque([[0, headID]])
        while q:
            t, u = q.popleft()
            res = max(res, t)
            for v in g[u]:
                q.append((t+informTime[u], v))
        return res
        