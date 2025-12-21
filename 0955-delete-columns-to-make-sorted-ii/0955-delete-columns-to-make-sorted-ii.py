'''
1. Understand
Check if the columns are sorted.
If they aren't we know we have to delete this entire column.

But we also have to check remaining columns.

'''
class Solution:
    def minDeletionSize(self, A):
        m, n = len(A), len(A[0])
        ans = 0
        cur = [""] * m
        for j in range(n):
            cur2 = cur[:]
            for i in range(m):
                cur2[i] += A[i][j]
            if all(cur2[i] <= cur2[i+1] for i in range(m-1)):
                cur = cur2
            else:
                ans+=1
        return ans

# class Solution:
#     def minDeletionSize(self, A):
#         res, n, m = 0, len(A), len(A[0])
#         is_sorted = [0] * (n - 1)
#         # Iterate chars
#         for j in range(m):
            
#             is_sorted2 = is_sorted[:]
#             # Iterate strs
#             for i in range(n - 1):
#                 # once sorted, always sorted
#                 # BAD CASE → column must be deleted
#                 if A[i][j] > A[i + 1][j] and is_sorted[i] == 0:
#                     res += 1
#                     break
#                 # GOOD / NEUTRAL CASE → accumulate sorted info
#                 is_sorted2[i] |= A[i][j] < A[i + 1][j]
#             else:
#                 # ← this runs ONLY if we never hit 'break'
#                 is_sorted = is_sorted2
#         return res

# from functools import lru_cache

# class Solution:
#     def minDeletionSize(self, A):
#         n, m = len(A), len(A[0])

#         @lru_cache(None)
#         def dp(col, is_sorted):
#             # Base case
#             if col == m:
#                 return 0

#             # Option 1: delete this column
#             best = 1 + dp(col + 1, is_sorted)

#             # Option 2: keep this column (if valid)
#             new_is_sorted = list(is_sorted)
#             for i in range(n - 1):
#                 if A[i][col] > A[i + 1][col] and is_sorted[i] == 0:
#                     break  # invalid column
#                 if A[i][col] < A[i + 1][col]:
#                     new_is_sorted[i] = 1
#             else:
#                 # no break → valid
#                 best = min(best, dp(col + 1, tuple(new_is_sorted)))

#             return best

#         return dp(0, tuple([0] * (n - 1)))


# from functools import lru_cache

# class Solution:
#     def minDeletionSize(self, A):
#         n, m = len(A), len(A[0])

#         @lru_cache(None)
#         def dfs(col, mask):
#             if col == m:
#                 return 0

#             # Option 1: delete column
#             res = 1 + dfs(col + 1, mask)

#             # Option 2: keep column if valid
#             new_mask = mask
#             for i in range(n - 1):
#                 bit = (mask >> i) & 1
#                 if A[i][col] > A[i + 1][col] and bit == 0:
#                     break
#                 if A[i][col] < A[i + 1][col]:
#                     new_mask |= (1 << i)
#             else:
#                 res = min(res, dfs(col + 1, new_mask))

#             return res

#         return dfs(0, 0)
