'''
courses = [[100,200],[1000,1250],[200,1300],[2000,3200]]

100+1000= 1100
1100 + 200 = 1300
1300 + 2000 = 3300



'''

from heapq import heappush, heappushpop

class Solution:
    def scheduleCourse(self, A: List[List[int]]) -> int:
        pq = []
        start = 0
        for t, end in sorted(A, key= lambda x: x[1]):
            start += t
            heappush(pq, -t)
            while start > end:
                start += heapq.heappop(pq)
                
        return len(pq)