from bisect import bisect_left

class Solution:
    def findLatestStep(self, arr, m):
        n = len(arr)
        # Special case:
        # If m == n, the entire array is one group at the final step
        if m == n:
            return n
        # `zeros` stores positions that are currently 0 (removed)
        # We add sentinels at 0 and n+1 to avoid edge checks
        zeros = [0, n + 1]

        # We go backwards: from step n-1 down to 0
        for i in range(n - 1, -1, -1):
            pos = arr[i]

            # Find where `pos` would be inserted in `zeros`
            # This gives us the nearest zero on the left and right
            idx = bisect_left(zeros, pos)

            left_zero = zeros[idx - 1]
            right_zero = zeros[idx]

            # Lengths of the two segments that would exist
            # BEFORE we remove `pos`
            left_len = pos - left_zero - 1
            right_len = right_zero - pos - 1
            # If either side had length m,
            # then step `i` was the latest valid step
            if left_len == m or right_len == m:
                return i
            # Insert pos into zeros (maintain sorted order)
            zeros.insert(idx, pos)
        return -1