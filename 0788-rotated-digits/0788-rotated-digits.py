class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for num in range(1, n + 1):
            same = True
            for d in str(num):
                if d in '347':
                    break
                if d in '2569':
                    same = False
            else:
                if not same:
                    count += 1
        return count