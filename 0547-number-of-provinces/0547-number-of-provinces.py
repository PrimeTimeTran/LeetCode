'''
Loop through items in list and dfs marking them as seen.
Increment res after each dfs, counting number of islands.
'''

class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        res = 0
        N = len(A)
        seen = set()
        def dfs(n):
            for i, nei in enumerate(A[n]):
                if nei and i not in seen:
                    seen.add(i)
                    dfs(i)
        
        for i in range(N):
            if i not in seen:
                dfs(i)
                res+=1
        return res