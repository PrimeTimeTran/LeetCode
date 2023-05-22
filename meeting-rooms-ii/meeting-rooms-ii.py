class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        s,e=0,0
        cur, res =0,0
        starts=sorted(i[0] for i in intervals)
        ends=sorted(i[1] for i in intervals)
        
        while s < len(intervals):
            if starts[s] < ends[e]:
                cur+=1
                s+=1
            else:
                cur-=1
                e+=1
            res = max(res, cur)
        return res