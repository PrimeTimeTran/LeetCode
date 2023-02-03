class Solution:
    def floodFill(self, image: List[List[int]], r: int, c: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        
        old = image[r][c]
        image[r][c] = color
        
        d = [0,-1,0,1,0]
        
        q = deque([[r,c]])
        seen = set()
        while q: 
            r, c = q.popleft()
            
            for i in range(4):
                nr, nc = d[i]+r, d[i+1]+c
                inbounds = 0 <= nr < m and 0 <= nc < n
                if inbounds and image[nr][nc] == old and (nr,nc) not in seen:
                    seen.add((nr,nc))
                    image[nr][nc] = color
                    q.append((nr,nc))
        return image