'''
1. Understand
2. Diagram
3. Pseudocode
Create a counter which counts the number of instances of a number in our list

4. Code
5. BigO
'''
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        memo, max_val, count = {}, max(nums), Counter(nums)

        points = [count[i] * i for i in range(max_val + 1)]
        @lru_cache(None)
        def dfs(i):
            if i > max_val: return 0
            skip = dfs(i+1)
            take = points[i] + dfs(i+2)
            return max(skip, take)
        return dfs(0)