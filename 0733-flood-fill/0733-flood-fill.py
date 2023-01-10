class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image), len(image[0])
        q = deque([[sr,sc]])
        seen = set((sr,sc))
        old = image[sr][sc]
        image[sr][sc] = color
        d = [0,1,0,-1,0]
        
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr,nc = r+d[i], c+d[i+1]
                out = nr < 0 or nc < 0 or nr == m or nc == n or (nr,nc) in seen
                if out: continue
                seen.add((r,c))
                if image[nr][nc] == old:
                    image[nr][nc] = color
                    q.append([nr,nc])
                    
        return image