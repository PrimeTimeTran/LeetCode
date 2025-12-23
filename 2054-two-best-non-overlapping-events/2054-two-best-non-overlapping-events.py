class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        # extract start times for binary search
        starts = [s for s, e, v in events]
        @lru_cache(None)
        def dp(i: int, taken: int) -> int:
            if i == n or taken == 2: return 0
            # option 1: skip event i
            best = dp(i + 1, taken)
            # option 2: take event i
            s, e, v = events[i]
            j = bisect_right(starts, e)  # first event with start > e
            best = max(best, v + dp(j, taken + 1))
            return best
        return dp(0, 0)
