'''

Iterate through courses
Increment the start time by the duration of each course
Add the course's duration to a maxheap
If the new start time is greater than the end time, remove current duration from time/heap
'''
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        pq = []
        start = 0
        
        for dur, end in sorted(courses, key = lambda x: x[1]):
            start += dur
            heapq.heappush(pq, -dur)
            if start > end:
                start += heapq.heappop(pq)
        
        return len(pq)