# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         res = []
#         def back(rem, strings):
#             if not rem:
#                 res.append(strings)
#             for i in range(1, len(rem)+1):
#                 if rem[:i] == rem[:i][::-1]:
#                     back(rem[i:], strings+[rem[:i]])
#         back(s, [])
#         return res

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def back(cur, path):
            if not cur:
                res.append(path)
            for i in range(1, len(cur)+1):
                if cur[:i] == cur[:i][::-1]:
                    back(cur[i:], path+[cur[:i]])
        back(s, [])
        return res