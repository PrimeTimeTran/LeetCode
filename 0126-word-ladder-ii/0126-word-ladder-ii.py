'''
BFS
BFS using G with wildcard keys and word values.
Use HM to count layers to ensure we can safely add this word without entering loop.
If so, add word to parent HM.

After BFS, DFS from endWord to beginWord adding all their words in the sequence. When beginword
found return the reversed path.

'''
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for w in wordList:
            for j in range(len(w)):
                pat = w[:j] + "*" + w[j+1:]
                g[pat].append(w)

        q = deque([beginWord])
        seen = {beginWord: 1}
        parent = defaultdict(set)

        while q:
            word = q.popleft()
            if word == endWord:
                break
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i+1:]
                for w in g[pat]:
                    if w not in seen:
                        seen[w] = seen[word] + 1
                        parent[w].add(word)
                        q.append(w)
                    elif seen[w] > seen[word]:
                        parent[w].add(word)

        ans = []
        def dfs(word, path):
            if word == beginWord:
                ans.append(path[::-1])
            for next_word in parent[word]:
                dfs(next_word, path+[next_word])
        dfs(endWord, [endWord])
        return ans
