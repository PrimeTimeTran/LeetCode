class Solution:
    def neighbour(self, a, b):
        cnt = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                cnt += 1
        return cnt == 1
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord in wordList:
            return []
        
        wordList.insert(0, beginWord)
        for i in range(1, len(wordList)):
            if wordList[i] == wordList[0]:
                wordList[i] = wordList[-1]
                wordList.pop()
                break
                
        wti = dict()
        for i in range(len(wordList)):
            wti[wordList[i]] = i 
        
        edges = [[] for _ in range(len(wordList))]

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                    if self.neighbour(wordList[i], wordList[j]):
                        edges[i].append(j)
                        edges[j].append(i)
    
        # BFS
        start_node, target_node = 0, wti[endWord]
        r, min_step = 0, float('inf')
        vis = [float('inf') for _ in range(len(wordList))]
        vis[start_node] = 0
        q = [start_node]
        while q:
            sz = len(q)
            for i in range(sz):
                fr = q.pop(0)
                if fr == target_node:
                    min_step = min(min_step, r)
                else:
                    for j in edges[fr]:
                        if r+1 < vis[j]:
                            vis[j] = r + 1
                            q.append(j)
            r += 1
        
        if min_step == float('inf'):
            return []
        
        q2 = [[wordList[target_node]]]
        r = min_step
        while r:
            sz = len(q2)
            for i in range(sz):
                seq = q2.pop(0)
                back = seq[-1]
                curr = wti[back]
                for j in edges[curr]:
                    if vis[j] == r - 1:
                        seq.append(wordList[j])
                        q2.append(seq[:])
                        seq.pop()
            r -= 1
        ans = []
        while q2:
            ans.append(q2.pop(0)[::-1])
        return ans