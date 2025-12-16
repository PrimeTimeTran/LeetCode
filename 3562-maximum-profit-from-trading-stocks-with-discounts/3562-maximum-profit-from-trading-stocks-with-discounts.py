fmax = lambda x, y: x if x > y else y

def merge(A, B):
    C = [-inf] * len(A)
    for i, a in enumerate(A):
        for j in range(len(A) - i):
            C[i + j] = fmax(C[i + j], a + B[j])
    return C

class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:
        g = [[] for _ in range(n)]
        for u, v in hierarchy:
            u -= 1
            v -= 1
            g[u].append(v)
        def dfs(u, p):
            dp0 = [0] * (budget + 1)
            dp1 = [0] * (budget + 1)
            for v in g[u]:
                if v != p:
                    res0, res1 = dfs(v, u)
                    dp0, dp1 = merge(dp0, res0), merge(dp1, res1)

            ans0 = dp0[:]
            ans1 = dp0[:]

            cost = present[u]
            for b in range(cost, budget + 1):
                ans0[b] = fmax(ans0[b], dp1[b - cost] + future[u] - cost)

            cost >>= 1
            for b in range(cost, budget + 1):
                ans1[b] = fmax(ans1[b], dp1[b - cost] + future[u] - cost)

            return ans0, ans1

        return max(dfs(0, -1)[0])


# class Solution:
#     def maxProfit(self, n, present, future, hierarchy, budget):
#         tree = [[] for _ in range(n)]
#         for u, v in hierarchy:
#             tree[u - 1].append(v - 1)
#         dp = [[[0] * (budget + 1) for _ in range(2)] for _ in range(n)]
#         print(dp)
#         def merge(A, B):
#             C = [-10**9] * (budget + 1)
#             for i in range(budget + 1):
#                 if A[i] < 0: continue
#                 for j in range(budget - i + 1):
#                     C[i + j] = max(C[i + j], A[i] + B[j])
#             return C
#         def dfs(u):
#             for v in tree[u]:
#                 dfs(v)
#             for parentBought in (0, 1):
#                 price = present[u] // 2 if parentBought else present[u]
#                 profit = future[u] - price

#                 skip = [0] * (budget + 1)
#                 for v in tree[u]:
#                     skip = merge(skip, dp[v][0])

#                 take = [-10**9] * (budget + 1)
#                 if price <= budget:
#                     base = [0] * (budget + 1)
#                     for v in tree[u]:
#                         base = merge(base, dp[v][1])
#                     for b in range(price, budget + 1):
#                         take[b] = base[b - price] + profit

#                 for b in range(budget + 1):
#                     dp[u][parentBought][b] = max(skip[b], take[b])
#         dfs(0)
#         print(dp)
#         return max(dp[0][0])