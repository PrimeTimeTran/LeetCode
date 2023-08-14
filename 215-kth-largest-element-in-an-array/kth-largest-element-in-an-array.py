class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    # ans = heapq.nlargest(k, nums) # run time O(n+klgn)
    # return ans[-1]
    
    heapq.heapify(nums)
        
    for _ in range(len(nums)-k):
        heapq.heappop(nums)

    return nums[0]
  