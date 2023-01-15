class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
#         q = deque([(headID, 0)])
#         subordinates = defaultdict(list)
#         res = 0
#         for i, v in enumerate(manager):
#             subordinates[v].append(i)
            
#         while q:
#             u, time = q.popleft()
#             res = max(res, time)
#             for v in subordinates[u]:
#                 q.append((v, time + informTime[u]))
#         return res
    
        children = defaultdict(list)
        for i, m in enumerate(manager):
            if m >= 0: children[m].append(i)

        def dfs(i):
            return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
        return dfs(headID)