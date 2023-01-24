class Solution:
    def kthSmallest(self, g: List[List[int]], k: int) -> int:
        minHeap = []
        for r in g:
            for el in r:
                heapq.heappush(minHeap, el)
        go = heapq.nsmallest(k, minHeap)
        return go[-1]