class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        if 1 in counter.values(): return -1
        return sum([ceil(v/3) for v in counter.values()])