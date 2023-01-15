class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        for i, j, ii, jj in queries: 
            ans[i][j] += 1
            if ii+1 < n: ans[ii+1][j] -= 1
            if jj+1 < n: ans[i][jj+1] -= 1
            if ii+1 < n and jj+1 < n: ans[ii+1][jj+1] += 1
        for i in range(n): 
            prefix = 0 
            for j in range(n): 
                prefix += ans[i][j]
                ans[i][j] = prefix 
                if i: ans[i][j] += ans[i-1][j]
        return ans 