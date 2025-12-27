'''
“A natural alternative is greedy — for example, always picking the highest-value event first. However, that fails because the highest-value event may span a long time range and prevent us from selecting a second event, even when two smaller-value non-overlapping events together yield a higher total. Since local choices affect future feasibility, the problem lacks the greedy-choice property, which is why a DP approach is appropriate.”
'''
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n, starts = len(events), [s for s, _, _ in events]
        def dp(i, pluck):
            if i == n or pluck == 2:
                return 0
            s, e, v = events[i]
            j = bisect_right(starts, e)
            skip = dp(i+1, pluck)
            take = v + dp(j, pluck+1)
            return max(skip, take)
        return dp(0, 0)