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
        
        q = deque([[0, headID]])
        res = 0
        while q:
            w, u = q.popleft()
            res = max(res, w)
            for v in g[u]:
                q.append([informTime[u]+w, v])
        return res