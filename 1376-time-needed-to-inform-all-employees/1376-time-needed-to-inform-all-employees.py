class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        for i, u in enumerate(manager):
            g[u].append(i)
        
        q = deque([(headID, 0)])
        res = 0
        while q:
            u, time = q.popleft()
            res = max(time, res)
            for v in g[u]:
                q.append((v, time+informTime[u]))
        return res
            