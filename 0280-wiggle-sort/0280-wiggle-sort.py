class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        for i in range(2, len(nums), 2):
            nums[i], nums[i-1] = nums[i-1], nums[i]
        
        return nums

        for i in range(len(nums)):
            nums[i:i+2] = sorted(nums[i:i+2], reverse=i%2)