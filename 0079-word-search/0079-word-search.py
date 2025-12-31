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
        seen, m, n = set(), len(board), len(board[0])
        def dfs(r, c, idx):
            if idx == len(word): return True
            inbounds = 0 <= r < m and 0 <= c < n
            if inbounds and word[idx] == board[r][c]:
                tmp = board[r][c]
                board[r][c] = '.'
                idx+=1
                res = (
                    dfs(r+1,c, idx) or 
                    dfs(r-1,c, idx) or
                    dfs(r,c+1, idx) or 
                    dfs(r,c-1, idx)
                )
                board[r][c] = tmp
                return res
        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False