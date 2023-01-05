class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = defaultdict(list)
        def helper(idx, zeros, ones):
            if idx == len(strs):
                return 0
            if (idx,zeros,ones) in dp:
                return dp[(idx,zeros,ones)]
            
            dp[(idx,zeros,ones)] = helper(idx+1, zeros, ones)
            
            numZeros, numOnes = strs[idx].count('0')+zeros, strs[idx].count('1')+ones
            if numZeros <= m and numOnes <= n:
                p = 1 + helper(idx+1, numZeros, numOnes)
                dp[(idx,zeros,ones)] = max(dp[(idx,zeros,ones)], p)
            return dp[(idx,zeros,ones)]
            
        return helper(0,0,0)