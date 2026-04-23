# class Solution:
#     def distance(self, nums: List[int]) -> List[int]:
#         ans, store = [], defaultdict(list)
#         for i, n in enumerate(nums):
#             store[n].append(i)
#         for i, n in enumerate(nums):
#             key_value = store.get(n)
#             if len(key_value) > 1:
#                 cur = 0
#                 for j in key_value:
#                     if j == i: continue
#                     cur +=  abs(i - j)
#                 ans.append(cur)
#             else:
#                 ans.append(0)
#         return ans

from collections import defaultdict

class Solution:
    def distance(self, nums):
        store = defaultdict(list)
        
        # Step 1: group indices
        for i, n in enumerate(nums):
            store[n].append(i)
        
        ans = [0] * len(nums)
        
        # Step 2: process each group
        for indices in store.values():
            prefix = [0]
            
            # build prefix sums
            for x in indices:
                prefix.append(prefix[-1] + x)
            
            m = len(indices)
            
            for k, i in enumerate(indices):
                # left contribution
                left = i * k - prefix[k]
                
                # right contribution
                right = (prefix[m] - prefix[k+1]) - i * (m - k - 1)
                
                ans[i] = left + right
        
        return ans