class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        res = 0
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            res += dic.get(curr-k, 0)
            dic[curr] = dic.get(curr, 0) +1
        return res 