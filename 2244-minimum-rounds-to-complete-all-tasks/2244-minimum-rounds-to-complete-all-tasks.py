class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks).values()
        if 1 in cnt: return -1
        return sum([ceil(v/3) for v in cnt])