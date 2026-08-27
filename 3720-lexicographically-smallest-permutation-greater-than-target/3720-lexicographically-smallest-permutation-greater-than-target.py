# class Solution:
#     def lexGreaterPermutation(self, s: str, target: str) -> str:
#         res = []
#         def dp(i, cur, res):
#             if i == len(s):
#                 res.append("".join(cur))
#                 return
#             for j in range(i, len(s)):
#                 cur[i], cur[j] = cur[j], cur[i]
#                 dp(i + 1, cur, res)
#                 cur[i], cur[j] = cur[j], cur[i]
#         dp(0, list(s), res)
#         res.sort()
#         i = bisect.bisect_right(res, target)
#         return res[i] if i < len(res) else ""
from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        counts = Counter(s)
        # Try making the permutation greater at the latest possible position.
        for i in range(len(target) - 1, -1, -1):
            # Consume target[:i]
            prefix_counts = Counter(target[:i])
            # If target[:i] requires characters we don't have, this prefix
            # can't be used.
            if any(prefix_counts[c] > counts[c] for c in prefix_counts):
                continue
            remaining = counts - prefix_counts
            # Find the smallest character available that is > target[i].
            bigger = [c for c in remaining if c > target[i]]
            if bigger:
                c = min(bigger)
                remaining[c] -= 1
                if remaining[c] == 0:
                    del remaining[c]
                suffix = []
                for char in sorted(remaining):
                    suffix.append(char * remaining[char])
                return target[:i] + c + "".join(suffix)
        return ""