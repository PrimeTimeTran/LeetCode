class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        heap = []
        heappush(heap,-nums[1])
        heappush(heap,-nums[2])

        for num in nums[3:]:
            heappushpop(heap,-num)

        return nums[0] - heap[0] - heap[1]