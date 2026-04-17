class Solution:
    def minMirrorPairDistance(self, nums):
        from collections import defaultdict
        import bisect

        def mirror(x):
            return int(str(x)[::-1])

        pos = defaultdict(list)

        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = float('inf')

        for i, x in enumerate(nums):
            m = mirror(x)

            if m not in pos:
                continue

            arr = pos[m]

            # binary search for first index > i
            k = bisect.bisect_right(arr, i)

            if k < len(arr):
                ans = min(ans, arr[k] - i)

        return ans if ans != float('inf') else -1