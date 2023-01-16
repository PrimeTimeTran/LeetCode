'''
BFS 
Create G and then BFS with accumulated time and manager node. Use manager node + time on each append to calculate
how long it takes to tell this employee. Update global max with each item.
'''
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        for i, m in enumerate(manager):
            g[m].append(i)

        def dfs(u):
            return max([dfs(v) for v in g[u]] or [0]) + informTime[u]
        return dfs(headID)