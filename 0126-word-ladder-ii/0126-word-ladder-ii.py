'''
BFS
BFS with G of wildcard keys and word values.
Guard for cycles using HM which has word key and layer distance. Add word if unseen or greater than current word.

DFS from endWord to beginWord using parent HM adding all words in the path. When beginword
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
                for nei in g[pat]:
                    if nei not in seen:
                        seen[nei] = seen[word]+1
                        q.append(nei)
                        parent[nei].add(word)
                    elif seen[nei] > seen[word]:
                        parent[nei].add(word)
        ans = []
        def dfs(w, path):
            if w == beginWord:
                ans.append(path[::-1])
            else:
                for nei in parent[w]:
                    dfs(nei, path+[nei])
        dfs(endWord, [endWord])
        return ans
