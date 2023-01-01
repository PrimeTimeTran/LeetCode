class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        count = num = 0
        for digit in s:
            if num > k: return -1
            num = (num * 10) + int(digit)
            if k >= num: continue
            else:
                num = int(digit)
                count += 1
        return count + 1