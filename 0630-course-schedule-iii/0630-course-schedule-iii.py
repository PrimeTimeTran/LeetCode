class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        start =  0
        heap = []
        for dur, end in sorted(courses, key=lambda x: x[1]):
            start += dur
            heapq.heappush(heap, -dur)
            if start > end:
                start += heapq.heappop(heap)
        return len(heap)