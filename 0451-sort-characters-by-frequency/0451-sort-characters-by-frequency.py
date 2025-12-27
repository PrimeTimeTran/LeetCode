class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_keys = sorted(count, key=count.get, reverse=True)
        res = ''
        for k in sorted_keys:
            res += (count[k] * k)
        return res
