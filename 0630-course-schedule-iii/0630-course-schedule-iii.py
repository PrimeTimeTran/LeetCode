from heapq import heappush, heappushpop

class Solution:
    def scheduleCourse(self, A: List[List[int]]) -> int:
        pq = []
        start = 0
        for t, end in sorted(A, key= lambda x: x[1]):
            start += t
            heappush(pq, -t)
            if start > end:
                start += heapq.heappop(pq)
        return len(pq)