'''
Guard invalid input
'''
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = defaultdict(list)
        
        def word2repres(word):
            return [word[0 : i] + '?' + word[i + 1 ::] for i in range(len(word))]
        
        wordList = wordList + [beginWord]
        for word in wordList:
            for r in word2repres(word):
                graph[r].append(word)
        
        queue = deque([beginWord])
        visited = set([beginWord])
        parents = defaultdict(list)
        res = []
        while queue:
            layer = set()
            for i in range(len(queue)):
                word = queue.popleft()
                for r in  word2repres(word):
                    for neigh in graph[r]:
                        if neigh not in visited:
                            layer.add(neigh)
                            parents[neigh].append(word)
            queue.extend(layer)
            visited.update(layer)
        
        def dfs(node, curr):
            if node == beginWord:
                res.append(curr[::-1])
                return
            for par in parents[node]:
                curr.append(par)
                dfs(par, curr)
                curr.pop()
        
        dfs(endWord, [endWord])
        return res