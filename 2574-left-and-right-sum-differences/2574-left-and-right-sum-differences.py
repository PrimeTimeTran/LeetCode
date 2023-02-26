class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        l = [0]
        for n in accumulate(nums):
            l.append(n)
        r = [0]
        for n in accumulate(nums[::-1]):
            r.insert(0, n)
        res = []
        del l[-1]
        del r[0]
        for i in range(len(l)):
            er = l[i] - r[i]
            res.append(abs(er))
        return res