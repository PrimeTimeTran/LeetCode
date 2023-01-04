class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = collections.defaultdict(list)
        words = set(wordList)
        if endWord not in words: return []
        words.discard(beginWord)
        q = {beginWord}
        while q:
            nq = set()
            for word in q:
                for c in "abcdefghijklmnopqrstuvwxyz":
                    for i in range(len(word)):
                        nw = word[:i] + c + word[i+1:]
                        if nw in words:
                            graph[nw].append(word)
                            nq.add(nw)
            words -= set(graph.keys())
            q = nq
            
        # use DFS to reconstruct the path from end to begin
        def dfs(word):
            if word == beginWord:
                return [[beginWord]]
            res = []
            for w in graph[word]:
                res += [k + [word] for k in dfs(w)]
            return res
			
        return dfs(endWord)