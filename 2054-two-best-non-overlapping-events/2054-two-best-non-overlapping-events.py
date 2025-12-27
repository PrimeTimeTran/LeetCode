class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        starts = [s for s, e, v in events]
        @lru_cache(None)
        def dp(i, total):
            if total == 2 or i == n: return 0
            s, e, v = events[i]
            j = bisect_right(starts, e)
            skip = dp(i+1, total)
            take = v + dp(j, total+1)
            return max(skip, take)
        return dp(0, 0)