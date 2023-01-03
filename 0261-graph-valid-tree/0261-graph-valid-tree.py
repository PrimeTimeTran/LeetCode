class Solution:
    def validTree(self, n, edges):
        nums = [-1] * n
        for edge in edges:
            if not self.union(nums, edge[0], edge[1]):
                return False
        return len(edges) == n-1

    def union(self, nums, x, y):
        xx = self.find(nums, x)
        yy = self.find(nums, y)
        if xx == yy:  # cycle detected 
            return False
        nums[xx] = yy
        return True

    def find(self, nums, i):
        if nums[i] == -1:
            return i
        return self.find(nums, nums[i])
        