class SegTree:
    def __init__(self, nums: List[int], k: int):
        self.k = k
        self.n = len(nums)
        s = 1
        while s < self.n:
            s <<= 1
        self.s = s
        self.tree = [([0 for _ in range(k)], 1) for _ in range(2 * s)]
        for i in range(self.n):
            a_mod = nums[i] % k
            cnt = [0 for _ in range(k)]
            cnt[a_mod] = 1
            prod = a_mod
            self.tree[s + i] = (cnt, prod)
        for p in range(s - 1, 0, -1):
            self.tree[p] = self.merge(self.tree[2 * p], self.tree[2 * p + 1])

    def merge(self, l, r):
        cnt_a, prod_a = l
        cnt_b, prod_b = r
        k = self.k
        cnt = cnt_a.copy()
        for r_b, c in enumerate(cnt_b):
            if c:
                r = (prod_a * r_b) % k
                cnt[r] += c
        prod = (prod_a * prod_b) % k
        return cnt, prod

    def update(self, idx, val):
        pos = self.s + idx
        a_mod = val % self.k
        cnt = [0] * self.k
        cnt[a_mod] = 1
        prod = a_mod
        self.tree[pos] = (cnt, prod)
        pos //= 2
        while pos:
            self.tree[pos] = self.merge(self.tree[2 * pos], self.tree[2 * pos + 1])
            pos //= 2

    def query(self, l, r):
        l += self.s
        r += self.s
        cnt_l, prod_l = [0]*self.k, 1
        cnt_r, prod_r = [0]*self.k, 1
        while l < r:
            if l & 1:
                cnt_l, prod_l = self.merge((cnt_l, prod_l), self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                cnt_r, prod_r = self.merge(self.tree[r], (cnt_r, prod_r))
            l //= 2
            r //= 2
        return self.merge((cnt_l, prod_l), (cnt_r, prod_r))


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        st = SegTree(nums, k)
        res = []
        for idx, val, start, x in queries:
            st.update(idx, val)
            cnt_seg, _ = st.query(start, len(nums))
            res.append(cnt_seg[x])
        return res