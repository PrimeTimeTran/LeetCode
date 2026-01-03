class Solution:
    def numOfWays(self, n):
        a121, a123, mod = 6, 6, 10**9 + 7
        for i in range(n - 1):
            a121, a123 = a121 * 3 + a123 * 2, a121 * 2 + a123 * 2
        return (a121 + a123) % mod
# class Solution:
#     def numOfWays(self, n: int) -> int:
#         MOD = 10**9 + 7
#         colors = [0, 1, 2]
#         patterns = []
#         for a in colors:
#             for b in colors:
#                 for c in colors:
#                     if a != b and b != c:
#                         patterns.append((a, b, c))

#         compat = {p: [] for p in patterns}
#         for p in patterns:
#             for q in patterns:
#                 if all(p[i] != q[i] for i in range(3)):
#                     compat[p].append(q)

#         # dp
#         dp = {p: 1 for p in patterns}  # first row

#         for _ in range(n - 1):
#             new_dp = {p: 0 for p in patterns}
#             for p in patterns:
#                 for q in compat[p]:
#                     new_dp[q] = (new_dp[q] + dp[p]) % MOD
#             dp = new_dp

#         return sum(dp.values()) % MOD
