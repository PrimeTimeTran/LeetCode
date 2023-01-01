class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        curr, ans = 0, 1
        for d in s:
            if int(d) > k:
                return -1
            curr = 10 * curr + int(d)
            if curr > k:
                ans += 1
                curr = int(d)
        return ans

        count = num = 0
        for digit in s:
            if num > k: return -1
            num = (num * 10) + int(digit)
            if k >= num: continue
            else:
                num = int(digit)
                count += 1
        return count + 1