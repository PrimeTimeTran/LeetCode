class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def back(start, path):
            if len(path) == k:
                res.append(path)
            for i in range(start, n+1):
                back(i+1, path+[i])
            return res
        return back(1, [])