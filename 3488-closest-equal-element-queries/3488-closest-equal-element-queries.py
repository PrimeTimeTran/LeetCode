# 1. Understand
# Find the min in

# 2. Diagram
# 3. Pseudocode
# 4. Code
# 5. Big O

from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums, queries):
        n = len(nums)
        
        # Step 1: map value → sorted indices
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        ans = []
        
        for q in queries:
            indices = pos[nums[q]]
            
            # If only one occurrence → no other match
            if len(indices) == 1:
                ans.append(-1)
                continue
            
            i = bisect.bisect_left(indices, q)
            
            # neighbors in sorted list (circular)
            left = indices[i - 1] if i > 0 else indices[-1]
            right = indices[i + 1] if i < len(indices) - 1 else indices[0]
            
            # compute circular distances
            dist_left = min(abs(q - left), n - abs(q - left))
            dist_right = min(abs(q - right), n - abs(q - right))
            
            ans.append(min(dist_left, dist_right))
        
        return ans