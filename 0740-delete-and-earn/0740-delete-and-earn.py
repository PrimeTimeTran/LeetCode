'''
1. Understand
2. Diagram
3. Pseudocode
Create a counter which counts the number of instances of a number in our list

4. Code
5. BigO
'''
class Solution:
    def deleteAndEarn(self, nums):
        count, max_val = Counter(nums), max(nums)
        points = [count[i] * i for i in range(max_val + 1)]
        prior = prev = 0
        for p in points:
            prior, prev = prev, max(prior + p, prev)
        return prev
