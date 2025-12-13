class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        g = { i: 0 for i in range(1, n+1)}
        for a, b in trust:
            g[a] -= 1
            g[b] += 1
        print(g)
        for i in range(1, n+1):
            if n-1 == g[i]: return i
        return -1