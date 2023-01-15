class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = deque([(headID, 0)])
        g = defaultdict(list)
        res = 0
        for i, v in enumerate(manager):
            g[v].append(i)
            
        while q:
            u, time = q.popleft()
            res = max(res, time)
            for v in g[u]:
                q.append((v, time + informTime[u]))
        return res