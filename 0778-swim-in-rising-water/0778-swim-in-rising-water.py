'''
1. Understand
BFS solution. 
Heap
We want to create a heap which is a list of cells to check, and then check if we've reached the bottom right cell. If that's case, then we jsut need to return the maximum elevation/time in our path to the bottom right cell.

2. Diagram


[0, 5]
[1, 4]

[0, 5]
[1, 1]

3. Pseudocode
    1. Define an answer variable and update during our BFS
    2. Iterate our queue while we havbe it. 
    3. Check if we've reached the bottom right cell, if so return the max we've encountered so far.
    4. For each cell we traverse we also need to traverse neighbors if htey're inbound.
    5. Ensure we don't backtrack over previously visited cells.
4. Code
5. Big O 

Peter's
O(n^2 log n)
O(n^2 * log (n^2)) 

Time:   O(logn^2 * ) where n is the length of the row or column
Space:  O()
'''
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # BFS or DFS

        # 1. Create variables.
        ans, seen, q, n = 0, set(), [[grid[0][0], 0, 0]], len(grid)
        
        # 2. Do work on queue.
        while q:
            elevation, r, c = heappop(q)                            # O(logn)
            
            # 3. Short circuit if appropriate
            if (r,c) in seen: continue
            seen.add((r,c))

            # 4. Update our max elevation we've had to see so far.
            ans = max(ans, elevation)
            if r == c == n-1:
                return ans
            
            # 5. Explore the neighbors of the cell which we're currently processing.
            for dx, dy in [r+1, c], [r-1, c], [r, c+1], [r, c-1]:
                inbounds = 0 <= dx < n and 0 <= dy < n
                if inbounds:
                    
                    # 6. Add neighbor to list of candidates to explore next
                    heappush(q, [grid[dx][dy], dx, dy])             # O(logn)