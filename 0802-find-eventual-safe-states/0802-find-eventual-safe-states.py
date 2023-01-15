class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        out_degree = [0] * n
        in_nodes = collections.defaultdict(list) 
        queue = []
        for i in range(n):
            out_degree[i] = len(graph[i])
            if out_degree[i] == 0: queue.append(i)
            for j in graph[i]: in_nodes[j].append(i)  
        for term_node in queue:
            for in_node in in_nodes[term_node]:
                out_degree[in_node] -= 1
                if out_degree[in_node] == 0: queue.append(in_node)
        return sorted(queue)