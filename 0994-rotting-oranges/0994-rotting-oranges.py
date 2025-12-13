class Solution:
    def orangesRotting(self, g: List[List[int]]) -> int:
        R, C = len(g), len(g[0])
        q, t, fresh, seen = [], 0, 0, set()

        for r in range(R):
            for c in range(C):
                if g[r][c] == 2:
                    heappush(q, (0, r, c))
                elif g[r][c] == 1:
                    fresh += 1
        while q:
            time, r, c = heappop(q)
            t = max(t, time)
            for dr, dc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                if (
                    0 <= dr < R and 0 <= dc < C and
                    g[dr][dc] == 1 and
                    (dr, dc) not in seen
                ):
                    seen.add((dr, dc))
                    g[dr][dc] = 2
                    fresh -= 1
                    heappush(q, (time + 1, dr, dc))
        return t if fresh == 0 else -1
