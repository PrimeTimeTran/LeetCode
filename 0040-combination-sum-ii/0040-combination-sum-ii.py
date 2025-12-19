class Solution:
    def combinationSum2(self, C: List[int], T: int) -> List[List[int]]:
        res = []
        C.sort()
        def back(start, path, total):
            if total == T:
                return res.append(path[:])
            if total > T or start == len(C):
                return
            for i in range(start, len(C)):
                if i > start and C[i] == C[i-1]: continue
                path.append(C[i])
                back(i+1, path, total+C[i])
                path.pop()
            return res
        return back(0, [], 0)