class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0 
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start, new_end = intervals[i]
            if start >= prev_end:
                prev_end = new_end
            else:
                res += 1
                prev_end = min(prev_end, new_end)
        
        return res