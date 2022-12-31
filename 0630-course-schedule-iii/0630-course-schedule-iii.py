'''
1. Constraints 
We receive an 2d array of [duration, date]

2. Diagram

courses = [[100,200],[1000,1250],[200,1300],[2000,3200]]
output = 3


1, 100, 101
3, 1000, 1100
2, 200, 1300
4, 2000, 3300

3. Pseudocode

Sort courses on end date
Iterate over courses and add their duration time to a start time.
If the duration time exceeds the end time, remove the most recently added time.

'''

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        time = 0
        pq = []
        for dur, end in sorted(courses, key= lambda x: x[1]):
            time += dur
            heapq.heappush(pq, -dur)
            while time > end:
                time += heapq.heappop(pq)
                
        return len(pq)
            
        
        
        
        