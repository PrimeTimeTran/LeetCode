class Solution:
    def average(self, salary: List[int]) -> float:
        smallest, largest = min(salary), max(salary)
        total = 0
        for s in salary:
            if s != smallest and s != largest:
                total += s

        return total / (len(salary)-2)