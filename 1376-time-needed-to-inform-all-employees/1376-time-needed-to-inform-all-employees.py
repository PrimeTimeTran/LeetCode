class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Bottom up 
        @cache
        def t(i):
            return 0 if i==-1 else t(manager[i])+informTime[i]
        return max(map(t,range(n)))
    
        # bottom up dfs
        def dfs(i):
            if manager[i] != -1:
                informTime[i] += dfs(manager[i])
                manager[i] = -1
            return informTime[i]
        return max(map(dfs, range(n)))
    
#         dfs        
#         children = [[] for i in range(n)]
#         for i, m in enumerate(manager):
#             if m >= 0: children[m].append(i)

#         def dfs(i):
#             return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
#         return dfs(headID)