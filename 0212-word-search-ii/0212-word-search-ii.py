class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

    def prune(self, word):
        curr, stack = self, []

        for ch in word:
            stack.append(curr)
            curr = curr.children[ch]

        curr.isWord = False

        for n, ch in reversed(list(zip(stack, word))):
            if len(n.children[ch].children) > 0:
                return
            else:
                del n.children[ch]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words: root.addWord(w)
        m, n = len(board), len(board[0])
        res, seen = [], set()

        def dfs(r, c, node, word):
            out = r < 0 or c < 0 or r == m or c == n
            if out: return
            char = board[r][c]
            if char not in node.children or (r, c) in seen: return

            seen.add((r, c))

            node = node.children[char]
            word += char

            if node.isWord: res.append(word); root.prune(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            seen.remove((r, c))

        for r in range(m):
            for c in range(n):
                dfs(r, c, root, "")
                
        return res
