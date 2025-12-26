'''
1. Understand
2. Diagram
3. Pseudocode
4. Code
5. BigO
Time: O()
Space: O()
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, o = len(s1), len(s2), len(s3)
        if m + n != o:
            return False
        def dp(i, j):
            if i == m and j == n: return True
            res, k = False, i + j
            if i < m and s1[i] == s3[k]:
                res = res or dp(i+1, j)
            if j < n and s2[j] == s3[k]:
                res = res or dp(i, j+1)
            return res
        return dp(0, 0)