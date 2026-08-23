class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        balance = 0
        # Add contributions from the left half
        for i in range(mid):
            c = num[i]
            balance += 4.5 if c == '?' else int(c)
        # Subtract contributions from the right half
        for i in range(mid, n):
            c = num[i]
            balance -= 4.5 if c == '?' else int(c)
        # If the net balance is anything other than 0, Alice wins
        return balance != 0.0