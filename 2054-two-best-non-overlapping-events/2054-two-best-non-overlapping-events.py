class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        starts = [s for s, _, _ in events]
        @lru_cache(None)
        def dp(i, taken):
            if taken == 2 or i == n:
                return 0
            _, e, v = events[i]
            j = bisect_right(starts, e)
            skip = dp(i + 1, taken)
            take = v + dp(j, taken + 1)
            return max(skip, take)
        return dp(0, 0)