class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l, ones, result = 0, 0, ""
        for r in range(len(s)):
            if s[r] == "1":
                ones += 1

            while ones > k:
                if s[l] == "1":
                    ones -= 1
                l += 1
            if ones == k:
                while s[l] == "0":
                    l += 1
                cur = s[l:r + 1]

                if (
                    result == ""
                    or len(cur) < len(result)
                    or (len(cur) == len(result) and cur < result)
                ):
                    result = cur

        return result