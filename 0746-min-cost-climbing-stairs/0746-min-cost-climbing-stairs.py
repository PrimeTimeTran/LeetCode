class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dic = {}
        def helper(n):
            if n in dic:
                return dic[n]
            if n < 0:
                return 0
            if n == 1 or n == 0:
                return cost[n]
            dic[n] = cost[n] + min(helper(n-1), helper(n-2))
            return dic[n]

        n = len(cost)
        return min(helper(n-1), helper(n-2))