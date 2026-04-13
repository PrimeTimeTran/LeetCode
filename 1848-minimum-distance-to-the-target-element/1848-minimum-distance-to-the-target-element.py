# 1. Understand
# Find the min distance between start and i when nums[i] == target.

# 2. Diagram
# 3. Pseudocode
# 4. Code
# 5. Big O
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        store = defaultdict(list)
        starts = defaultdict(list)
        
        for i, n in enumerate(nums):
            if n == target:
                starts[n].append(i)
            store[n].append(i)

        cur = inf

        for key, items in starts.items():
            for val in items:
                abs_diff = abs(val - start)
                if cur > abs_diff:
                    cur = abs_diff
        return cur