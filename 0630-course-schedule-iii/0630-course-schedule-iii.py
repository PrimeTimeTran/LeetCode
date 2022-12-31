'''
1. Constraints
We receive a 2d list where the elements are [duration, endDay]

We want to return an int, indicating maximum number of courses we can take.


Diagram
courses = [[100,200],[1000,1250],[200,1300],[2000,3200]]
1, 100 <= 200
2, 1100 <= 1250
3, 1300 <= 1300
4, 3300 <= 3200
res = 3



2. Pseudocode

- Sort our courses lastDay
- Iterate through courses and increment start time by course time. 0 + 100 + 1000 + 200 ... n-1


'''

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        pq = []
        start = 0
        for t, end in sorted(courses, key = lambda x: x[1]):
            start += t
            heapq.heappush(pq, -t)
            if start > end:
                start += heapq.heappop(pq)
        return len(pq)