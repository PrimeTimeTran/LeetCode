class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]

        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if x == y:
                continue
            else:
                diff = y - x
                heapq.heappush(stones, diff)

        return abs(stones[0]) if len(stones) > 0 else 0