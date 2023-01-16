class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        for i, u in enumerate(manager):
            g[u].append(i)
        
        q = deque([[0, headID]])
        res = 0
        while q:
            t, u = q.popleft()
            res = max(res, t)
            for v in g[u]:
                q.append([t+informTime[u], v])
        return res