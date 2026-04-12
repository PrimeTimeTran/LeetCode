# 1. Understand
#   - We have two cells/fingers starting at a cost of 0. From there, type every character in the word in sequence until the list is exhausted
#   - 4 Cardinal directions each cost 1. Diagonal moves arent allowed.
#   - Return the lowest possible output given the requirements.

# 2. Diagram
import string

# 3. Pseudocode
# 4. Code
# 5. Big O Time/Space
class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            r1, c1 = pos[a]
            r2, c2 = pos[b]
            return abs(r1 - r2) + abs(c1 - c2)

        keyboard = [
            list("ABCDEF"),
            list("GHIJKL"),
            list("MNOPQR"),
            list("STUVWX"),
            list("YZ")
        ]

        pos = {}
        for r in range(len(keyboard)):
            for c in range(len(keyboard[r])):
                pos[keyboard[r][c]] = (r, c)
        
        # a = pos[word[0]]
        
        # def dp(total, idx):
        #     if idx == len(word):
        #         return total
        #     finger1 = dist(word[idx], word[idx+1])
        #     finger2 = dist(word[idx-1], word[idx+1]) if idx != 0 else inf
        #     return min(finger1, finger2) + dp(total, idx+1)

        # value = dp(0, 0)
        # print('value ', value)
        # # for char in word:
import string
from collections import defaultdict

class Solution:
    def minimumDistance(self, word: str) -> int:
        keyboard = [
            list("ABCDEF"),
            list("GHIJKL"),
            list("MNOPQR"),
            list("STUVWX"),
            list("YZ")
        ]

        pos = {}
        for r in range(len(keyboard)):
            for c in range(len(keyboard[r])):
                pos[keyboard[r][c]] = (r, c)

        def dist(a, b):
            if a is None:
                return 0
            r1, c1 = pos[a]
            r2, c2 = pos[b]
            return abs(r1 - r2) + abs(c1 - c2)

        dp = { (None, None): 0 }

        for ch in word:
            new_dp = defaultdict(lambda: float('inf'))
            for (f1, f2), cost in dp.items():
                # move finger1 to ch
                new_dp[(ch, f2)] = min(
                    new_dp[(ch, f2)],
                    cost + dist(f1, ch)
                )
                # move finger2 to ch
                new_dp[(f1, ch)] = min(
                    new_dp[(f1, ch)],
                    cost + dist(f2, ch)
                )
            dp = new_dp
        return min(dp.values())