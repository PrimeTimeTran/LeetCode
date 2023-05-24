class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
    
        z=[]
        
        for a,b in zip(nums1,nums2):
            z.append([a,b])
        
        z.sort(key=lambda x:-x[1])
        
        heap=[]
        best=total=0
        
        for a,b in z:
            heappush(heap,a)
            total+=a
            if len(heap)==k:
                best=max(best,total*b)
                total-=heappop(heap)

        return best