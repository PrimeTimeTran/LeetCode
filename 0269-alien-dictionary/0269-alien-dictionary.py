'''
Topological Sort
Create graph using chars of word of words.
Iterate words 2 at a time, guarding for matching prefixes having a longer word before a shorter. Return "" if true.
Loop through chars of w1 looking for first differing char. The first differing char add it to word one's list in the graph.
Topsort of graph with loop detection.
Return the reverse joined res because to create lexicographically increasing order string.
'''

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Kahn's BFS
        indegree, graph = {c: 0 for word in words for c in word}, collections.defaultdict(set)
        for i in range(1, len(words)):
            is_prefix = True
            for a, b in zip(words[i-1], words[i]):
                if a == b:
                    continue
                if b not in graph[a]: 
                    indegree[b] += 1
                is_prefix = False
                graph[a].add(b)
                break
            if is_prefix == True and len(words[i-1]) > len(words[i]):
                return ""
        res = ""
        # start w 0 indegree nodes
        queue = deque([c for c in indegree if indegree[c]==0])
        while queue:
            c = queue.popleft()
            res += c
            for n in graph[c]:
                indegree[n] -= 1
                if indegree[n]==0: 
                    queue.append(n)
        return res if len(res) == len(indegree) else ''  