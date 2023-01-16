class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        d = [0,1,0,-1,0]
        
        m,n = len(image), len(image[0])
        
        old = image[sr][sc]
        image[sr][sc] = color
        
        q = deque([[sr,sc]])
        seen = set((sr,sc))
        
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr,nc = r+d[i], c+d[i+1]
                out = nr < 0 or nc < 0 or nr == m or nc == n
                if out or (nr,nc) in seen: continue
                seen.add((nr,nc))
                if image[nr][nc] == old:
                    image[nr][nc] = color
                    q.append([nr,nc])
                    
        return image