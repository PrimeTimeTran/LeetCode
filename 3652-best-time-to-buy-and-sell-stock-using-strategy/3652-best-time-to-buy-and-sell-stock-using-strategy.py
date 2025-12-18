# class Solution:
#     def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
#         n = len(prices)
#         profit = sum(map(mul, prices, strategy))                # <-- 1)

#         newProf = profit
#         for idx in range(k):                                    # <-- 2)
#             newProf -= strategy[idx] * prices[idx]
#             if idx >= k // 2:
#                 newProf+= prices[idx]

#         if newProf > profit: profit = newProf

#         for idx in range(n - k):
#             newProf -= (strategy[idx+k] - 1) * prices[idx+k]     # <-- 3a)
#             newProf += strategy[idx] * prices[idx]               # <-- 3b)
#             newProf -= prices[idx + k // 2]                      # <-- 3c)

#             if newProf > profit: profit = newProf

#         return profit

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        sp = [s * p for s, p in zip(strategy, prices)]
        n = len(prices)

        baseline = sum(sp)
        h = k // 2
        old = sum(sp[:k])
        new = sum(prices[h:k])

        maxdiff = max(0, new - old)

        for r in range(k, n):
            l = r - k + 1  
            old += sp[r] - sp[l - 1]
            new += prices[r]
            new -= prices[l - 1 + h]
            maxdiff = max(maxdiff, new - old)

        return baseline + maxdiff