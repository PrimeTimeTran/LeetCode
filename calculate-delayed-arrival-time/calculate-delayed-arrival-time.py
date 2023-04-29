class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        total = (arrivalTime + delayedTime)
        return total % 24 if total > 24  else 0 if total == 24 else total
    