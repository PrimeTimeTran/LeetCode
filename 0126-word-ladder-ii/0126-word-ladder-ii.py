'''
BFS
BFS with G of wildcard keys and word values.
Guard for cycles using HM which has word key and layer distance. Add word if unseen or greater than current word.

DFS from endWord to beginWord with parent HM adding all words in the path. When beginword
found return the reversed path.
'''
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for w in wordList:
            for j in range(len(w)):
                pat = w[:j] + "*" + w[j+1:]
                g[pat].append(w)
        
        seen = { beginWord: 1 }
        q = deque([beginWord])
        parent = defaultdict(set)
        
        while q:
            for _ in range(len(q)):
                w = q.popleft()    
                if w == endWord: break
                for j in range(len(w)):
                    pat = w[:j] + "*" + w[j+1:]
                    for nei in g[pat]:
                        if nei not in seen:
                            seen[nei] = seen[w]+1
                            parent[nei].add(w)
                            q.append(nei)
                        elif seen[nei] > seen[w]:
                            parent[nei].add(w)
        res = []
        def dfs(w, p):
            if w == beginWord:
                res.append(p[::-1])
            else:
                for nei in parent[w]:
                    dfs(nei, p+[nei])
        dfs(endWord, [endWord])
        return res
                
        