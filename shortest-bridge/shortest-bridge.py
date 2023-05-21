class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        i, j = next((i, j) for i in range(m) for j in range(n) if A[i][j])
        
        # dfs 
        stack = [(i, j)]
        seen = set(stack)
        while stack: 
            i, j = stack.pop()
            seen.add((i, j)) # mark as visited 
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n and A[ii][jj] and (ii, jj) not in seen: 
                    stack.append((ii, jj))
                    seen.add((ii, jj))
        
        # bfs 
        ans = 0
        queue = list(seen)
        while queue:
            newq = []
            for i, j in queue: 
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in seen: 
                        if A[ii][jj] == 1: return ans 
                        newq.append((ii, jj))
                        seen.add((ii, jj))
            queue = newq
            ans += 1