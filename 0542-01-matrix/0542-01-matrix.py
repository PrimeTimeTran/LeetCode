'''
BFS
Iterate cells adding 0 cells to Q and changing others to -1. BFS Q ignorng out of bounds and cells which aren't -1.
For each cell item, increment cell by 1 + current cell value befoore appending new coords.

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
            r, c = q.popleft()
            for i in range(4):
                nr,nc = r+d[i],c+d[i+1]
                o = nr < 0 or nc < 0 or nr == m or nc == n or mat[nr][nc] != -1
                if o or (nr,nc) in seen: continue
                # seen.add((nr,nc))
                mat[nr][nc] = mat[r][c]+1
                q.append((nr,nc))
        return mat