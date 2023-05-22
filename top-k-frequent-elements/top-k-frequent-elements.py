class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        i=0
        res = []
        for key, v in c.most_common():
            if i == k:
                break
            i+=1
            res.append(key)
        return res
    
        # # O(1) time 
        # if k == len(nums):
        #     return nums
        
        # # 1. build hash map : character and how often it appears
        # # O(N) time
        # count = Counter(nums)   
        # # 2-3. build heap of top k frequent elements and
        # # convert it into an output array
        # # O(N log k) time
        # return heapq.nlargest(k, count.keys(), key=count.get) 
    
        # vals = {}
        # for n in nums:
        #     vals[n] = vals.get(n,0)+1
        # arr = sorted(vals, key = vals.get, reverse = True)
        # return arr[:k]