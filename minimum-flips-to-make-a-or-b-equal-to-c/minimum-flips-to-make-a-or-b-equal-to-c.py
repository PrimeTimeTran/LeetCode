class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ab, equal, ans = a | b, (a | b) ^ c, 0
        for i in range(31):
            mask = 1 << i
            if equal & mask > 0:
              # ans += 1 if (ab & mask) < (c & mask) or (a & mask) != (b & mask) else 2
                ans += 2 if (a & mask) == (b & mask) and (c & mask) == 0 else 1
        return ans