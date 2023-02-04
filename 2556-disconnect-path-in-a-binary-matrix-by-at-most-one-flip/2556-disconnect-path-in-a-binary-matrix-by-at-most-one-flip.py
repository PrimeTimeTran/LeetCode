class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        M, N = len(grid), len(grid[0])
        v= set()
        dirs=[[0,1],[1,0],[-1,0],[0,-1]]
        path = set()
        v.add((0,0))
        path.add((0,0))
        def dfs(x,y):
            if x == M -1 and y == N -1: return True
            for d in dirs:
                nx = x + d[0]
                ny = y + d[1]
                
                if 0 <= nx < M and 0 <=ny < N and (nx,ny) not in v and grid[nx][ny] == 1:
                    v.add((nx,ny))
                    path.add((nx,ny))
                    if dfs(nx,ny):
                        return True
                    path.remove((nx,ny))
            return False
        res =  dfs(0,0)
        if not res: return True
        path.remove((0,0))
        path.remove((M-1,N-1))
        for p in path:
            grid[p[0]][p[1]] = 0
        
        v= set()
        v.add((0,0))

        #2 try again DFS
        return not dfs(0,0)
        