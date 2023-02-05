class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        nums = [-num for num in gifts]
        heapify(nums)
        
        while k:
            tmp = math.isqrt(-heappop(nums))
            heappush(nums, -tmp)
            k -= 1
            
        return -sum(nums)
        while k > 0:
            gifts.sort()
            gifts[-1] = math.floor(math.sqrt(gifts[-1]))
            k-=1
        return sum(gifts)