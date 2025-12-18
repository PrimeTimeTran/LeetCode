'''
1. Understand
2. Diagram
3. Pseudocode
4. Code
5. BigO
Time:    O()
Space:   O()
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        seen = set()
        def dfs(r, c, count):
            if count == len(word):
                return True
            inbounds = 0 <= r < m and 0 <= c < n
            if inbounds and word[count] == board[r][c]:
                tmp = board[r][c]
                board[r][c] = '.'
                count+=1
                res = (
                    dfs(r+1,c, count) or 
                    dfs(r-1,c, count) or
                    dfs(r,c+1, count) or 
                    dfs(r,c-1, count)
                )
                board[r][c] = tmp
                return res
        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False