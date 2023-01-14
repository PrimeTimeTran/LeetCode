class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L = 0 
        R = 0
        while R < len(prices):
            if prices[R] > prices[L]:
                profit = prices[R] - prices[L]
                res = max(res, profit)            
            else:
                L = R    
            R+=1
        return res