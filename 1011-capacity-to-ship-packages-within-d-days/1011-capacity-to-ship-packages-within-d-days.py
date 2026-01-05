class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            capacity, days_needed, current_load = (l + r) // 2, 1, 0
            for pack_weight in weights:
                if current_load + pack_weight > capacity:
                    days_needed += 1
                    current_load = 0
                current_load += pack_weight
            if days_needed > days: 
                l = capacity + 1
            else: 
                r = capacity
        return l