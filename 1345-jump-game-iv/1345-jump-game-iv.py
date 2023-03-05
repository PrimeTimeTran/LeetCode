class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d, t = defaultdict(list), len(arr) - 1
        for i, n in enumerate(arr):
            d[n] += i,
            
        q, seen = [(0, 0)], defaultdict(lambda:inf)
        seen[0] = 0
        for i, h in q:
            if i == t: return h
            for j in [i+1, i-1, *d[arr[i]]]:
                if i != j and 0 <= j <= t and seen[j] > h+1:
                    seen[j] = h+1
                    q += (j, h+1),
            d.pop(arr[i])