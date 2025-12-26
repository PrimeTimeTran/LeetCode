'''
1. Understand
2. Diagram
3. Pseudocode
4. Code
5. BigO
Time:    O()
Space:   O()
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo = {}
        def dp(cur):
            if cur in memo:
                return memo[cur]
            res = []
            if not cur:
                return [[]]
            for i in range(1, len(cur)+1):
                if cur[:i] == cur[:i][::-1]:
                    for rest in dp(cur[i:]):
                        res.append([cur[:i]] + rest)
            memo[cur] = res
            return res
        return dp(s)