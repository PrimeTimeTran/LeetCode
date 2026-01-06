
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        items = list(range(1, n + 1))
        vals = permutations(items)
        for i, perm in enumerate(vals):
            if i+1 == k:
                return ''.join(map(str, perm))

# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:
#         res = []
#         def back(cur, path):
#             if not cur:
#                 return res.append(path)
#             for i in range(len(cur)):
#                 back(cur[:i] + cur[i+1:], path + [cur[i]])
#         back(list(range(1, n+1)), [])
#         return ''.join(map(str, res[k-1]))
