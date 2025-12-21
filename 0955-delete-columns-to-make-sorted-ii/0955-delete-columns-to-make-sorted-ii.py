'''
1. Understand
Check if the columns are sorted.
If they aren't we know we have to delete this entire column.

But we also have to check remaining columns.
965-delete-columns-to-make-sorted-ii
'''
class Solution:
    def minDeletionSize(self, A):
        res, m, n = 0, len(A), len(A[0])
        # Tracks True/False between whether or not a row and 
        # it's next neighbor have been proven lexigraphically sorted or not previously.
        # 0: Undecided
        # The order between row i and row i+1 is still undecided, so the current column can still break it.
        # 1: Decided
        # The order between row i and row i+1 has already been permanently decided by an earlier column.
        is_sorted = [0] * (m - 1)
        
        # Compare columns/indexes
        for j in range(n):
            is_sorted2 = is_sorted[:]
            
            # Compare rows/strs
            for i in range(m - 1):
                # If this column causes a violation for 
                # a pair whose order is still undecided, then the column must be deleted.
                if A[i][j] > A[i + 1][j] and is_sorted[i] == 0:
                    res += 1
                    break
                # At this column, if this row is proven 
                # smaller than the next row, save that info.
                # In this way we prevent column deletions if later columns 
                # have unordered characters for a pair whose lexicographic order was already decided.
                is_sorted2[i] |= A[i][j] < A[i + 1][j]
            else:
                is_sorted = is_sorted2
        return res