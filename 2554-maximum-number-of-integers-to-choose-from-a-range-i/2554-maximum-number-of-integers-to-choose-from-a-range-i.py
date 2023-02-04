class Solution:
    def maxCount(self, banned: List[int], n: int, k: int) -> int:
        banned = set(banned)
        nums = [i for i in range(1, n+1) if i not in banned]
        cum = 0
        count=0
        for i in nums:
            if i + cum <= k:
                cum+=i
                count+=1
            else:
                return count
        return count