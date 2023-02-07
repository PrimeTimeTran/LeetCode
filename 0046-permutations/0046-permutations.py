class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
        
        res = []
        if len(nums) == 0:
            return [[]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for p in perms:
                p.append(n)
            res.extend(perms)
            nums.append(n)

        return res