class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0 
        p = intervals[0][1]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s >= p:
                p = e
            else:
                res+=1
                p = min(p, e)
        
        return res