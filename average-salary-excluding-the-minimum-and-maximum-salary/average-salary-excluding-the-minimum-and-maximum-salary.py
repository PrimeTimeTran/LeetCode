class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        return sum(salary[1:-1])/len(salary[1:-1])
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
