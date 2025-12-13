'''
PQ from initial r & c. 
Use set to filter seen cells.
Store PQ popped cell's color in tmp before changing it to the input color.
For neighbors of a popped cell, check if it's inbounds and if it's the tmp color. If it is, add it to the PQ.
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        q = [[sr, sc, image[sr][sc]]]
        seen = set()

        while q:
            r, c, tmp = heappop(q)
            image[r][c] = color
            for dr, dc in [r+1,c],[r-1,c],[r,c+1],[r,c-1]:
                if (dr,dc) in seen: continue
                seen.add((dr, dc))
                inbounds = 0 <= dr < m and 0 <= dc < n
                if inbounds and image[dr][dc] == tmp:
                    heappush(q, [dr, dc, tmp])
        return image