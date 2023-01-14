class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        g = defaultdict(list)
        seen = set()
        n = len(A)
        def dfs(j):
            for i, nei in enumerate(A[j]):
                if nei and i not in seen:
                    seen.add(i)
                    dfs(i)
            
        res = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                res+=1
        return res