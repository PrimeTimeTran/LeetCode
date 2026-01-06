
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        items = list(range(1, n + 1))
        vals = itertools.permutations(items)
        for i, perm in enumerate(vals):
            if i+1 == k:
                return ''.join(map(str, perm))
        # res = []
        # def back(cur, path):
        #     if not cur:
        #         return res.append(path)
        #     for i in range(n+1):
        #         back(cur[:i] + cur[i+1:], [cur[i]] + path)
        # back(list(range(1, n+1)), [])
        # print(res)
