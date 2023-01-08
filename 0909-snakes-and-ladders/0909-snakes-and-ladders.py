class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r, c]

        q = deque()
        q.append([1, 0])
        visit = set()
        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                nxtSquare = square + i
                r, c = intToPos(nxtSquare)
                if board[r][c] != -1:
                    nxtSquare = board[r][c]
                if nxtSquare == length * length:
                    return moves + 1
                if nxtSquare not in visit:
                    visit.add(nxtSquare)
                    q.append([nxtSquare, moves + 1])
        return -1
