class Solution:
    def countRoutes(self, locations, start, finish, fuel):
        MOD = 1000000007
        n = len(locations)
        
        dp = [[0] * (fuel + 1) for _ in range(n)]
        for f in range(fuel + 1):
            dp[finish][f] = 1
        
        for f in range(fuel + 1):
            for city in range(n):
                for nextCity in range(n):
                    if nextCity != city and f >= abs(locations[nextCity] - locations[city]):
                        dp[city][f] = (dp[city][f] + dp[nextCity][f - abs(locations[nextCity] - locations[city])]) % MOD
        
        return dp[start][fuel]