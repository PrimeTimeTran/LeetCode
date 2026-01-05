class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            capacity, load, days_needed = (l+r) // 2, 0, 1
            for pack_weight in weights:
                if load + pack_weight > capacity:
                    load = 0
                    days_needed += 1
                load += pack_weight
            if days_needed > days:
                l = capacity + 1
            else:
                r = capacity
        return l