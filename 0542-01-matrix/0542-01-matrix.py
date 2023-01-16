'''
BFS
Iterate cells adding 0 cells to Q and changing others to -1. BFS Q ignorng out of bounds, processed cells. 

'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        DIR = [0, 1, 0, -1, 0]
        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = -1
        seen = set()        
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r+DIR[i], c+DIR[i+1]
                out = nr < 0 or nc < 0 or nr == m or nc == n
                if out or mat[nr][nc] != -1: continue
                mat[nr][nc] = 1 + mat[r][c]
                q.append((nr,nc))
        return mat