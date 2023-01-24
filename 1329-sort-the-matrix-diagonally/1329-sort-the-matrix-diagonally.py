class Solution:
    def diagonalSort(self, A: List[List[int]]) -> List[List[int]]:
        n, m = len(A), len(A[0])
        d = defaultdict(list)
        for i in range(n):
            for j in range(m):
                d[i - j].append(A[i][j])
        for k in d:
            d[k].sort(reverse=True)
        for i in range(n):
            for j in range(m):
                A[i][j] = d[i - j].pop()
        return A