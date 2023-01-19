class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return list(itertools.permutations(nums))
        
        # return nums and [p[:i] + [nums[0]] + p[i:]
        #                  for p in self.permute(nums[1:])
        #                  for i in range(len(nums))] or [[]]
        
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