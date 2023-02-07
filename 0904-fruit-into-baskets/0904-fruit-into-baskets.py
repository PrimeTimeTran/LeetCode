class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        count, L = {}, 0
        for R, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[tree[L]] -= 1
                if count[tree[L]] == 0: del count[tree[L]]
                L += 1
        return R - L + 1