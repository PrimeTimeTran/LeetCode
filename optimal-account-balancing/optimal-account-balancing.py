class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:

        tuplify = lambda balance: tuple(sorted((k, v) for k, v in balance.items()))

        @lru_cache(None)
        def dfs(balances):
            if not balances:
                return 0
            res = math.inf
            balances = {k: v for k, v in balances}
            for size in range(2, len(balances) + 1):
                for group in itertools.combinations(balances.keys(), size):
                    if sum(balances[k] for k in group) == 0:
                        remaining_balances = {k: v for k, v in balances.items() if k not in group}
                        res = min(res, size - 1 + dfs(tuplify(remaining_balances)))
            return res

        balances = collections.defaultdict(int)
        for u, v, z in transactions:
            balances[u] += z
            balances[v] -= z
        return dfs(tuplify({k: v for k, v in balances.items() if v}))