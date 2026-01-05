class Solution:
    def shipWithinDays(self, weights: List[int], day_limit: int) -> int:
        l, r = max(weights), sum(weights)
        def is_feasible(cap, load = 0, days = 1):
            for pkg_weight in weights:
                if load + pkg_weight > cap:
                    days+=1
                    load = 0
                load += pkg_weight
            return days <= day_limit
        while l < r:
            m = (l+r) // 2
            if is_feasible(m):
                r = m
            else:
                l = m + 1
        return l