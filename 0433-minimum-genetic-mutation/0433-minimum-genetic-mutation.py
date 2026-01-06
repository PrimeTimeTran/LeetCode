class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q, bank = deque([(start, 0)]), set(bank)
        while q:
            gm, moves = q.popleft()
            if gm == end:
                return moves
            for i in range(8):
                for c in "ACGT":
                    new_gene = gm[:i] + c + gm[i+1:]
                    if new_gene in bank:
                        bank.remove(new_gene)
                        q.append([new_gene, moves+1])
        return -1