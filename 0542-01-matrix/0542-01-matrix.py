'''
BFS
Iterate cells adding 0 cells to Q and changing others to -1. BFS Q on inbound and non 0 cells.
For each cell item, increment cell by 1 + current cell value before appending new coords.
'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = -1
                    
        d = [0,-1,0,1,0]
        seen = set()
        while q:
            r,c = q.popleft()
            
            for i in range(4):
                nr,nc = r+d[i], c+d[i+1]
                inbounds = 0<=nr<m and 0<=nc<n
                if inbounds and (nr,nc) not in seen and mat[nr][nc] != 0:
                    seen.add((nr,nc))            
                    mat[nr][nc] = mat[r][c]+1
                    q.append((nr,nc))
                    
        return mat