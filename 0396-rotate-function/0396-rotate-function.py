# f(k) = [4, 3, 2, 6]
# F(0) = [          ] -> [4, 3, 2, 6]
# F(1) = [          ] -> [6, 4, 3, 2] 
# F(2) = [          ] -> [2, 6, 4, 3] 
# F(3) = [          ] -> [4, 3, 2, 6]

# FROM [4, 3, 2, 6]:

# k=0 → [4, 3, 2, 6] -> rotate 0 times -> get this arr -> [4, 3, 2, 6]
# k=1 → [6, 4, 3, 2] -> rotate 1 times -> get this arr -> [6, 4, 3, 2]
# k=2 → [2, 6, 4, 3] -> rotate 2 times -> get this arr -> [2, 6, 4, 3]
# k=3 → [3, 2, 6, 4] -> rotate 3 times -> get this arr -> [3, 2, 6, 4]
# k=4 → [4, 3, 2, 6] -> rotate 4 times -> get this arr -> [4, 3, 2, 6]
# k=5 → [6, 4, 3, 2] -> rotate 5 times -> get this arr -> [6, 4, 3, 2]
# k=6 → [2, 6, 4, 3] -> rotate 6 times -> get this arr -> [2, 6, 4, 3]

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # Solution 1. O (n^2)
        # ans, n = 0, len(nums)
        # for i in range(n):
        #     idx = total = 0
        #     for d in range(n):
        #         val = nums[(i + d) % n]
        #         total += d * val
        #     if total > ans:
        #         ans = total
        # return ans

        # F(k)=F(k−1)+S−n⋅nums[n−k]

        # Solution 2. O (n^2)
        n, S = len(nums), sum(nums)
        F = sum(i * v for i, v in enumerate(nums))
        best = F
        for k in range(1, n):
            F = F + S - n * nums[n - k]
            best = max(best, F)
        return best