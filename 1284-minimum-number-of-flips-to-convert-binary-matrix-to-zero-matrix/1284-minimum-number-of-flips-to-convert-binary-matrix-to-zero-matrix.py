class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        def flip(a):
            if all(x == 0 for v in a for x in v):
                return 0
            astr = str(list(chain.from_iterable(a)))
            if astr in cache:
                return cache[astr]
            if astr in visited: return math.inf
            visited.add(astr)
            res = math.inf
            for i in range(len(a)):
                for j in range(len(a[0])):
                    temp = deepcopy(a)
                    temp[i][j] ^= 1
                    for xoff, yoff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        x, y = i + xoff, j + yoff
                        if 0 <= x < len(a) and 0 <= y < len(a[0]):
                            temp[x][y] ^= 1
                    res = min(res, 1 + flip(temp))
            visited.remove(astr)
            cache[astr] = res
            return res
        visited, cache = set(), {}
        res = flip(mat)
        return -1 if res == math.inf else res


