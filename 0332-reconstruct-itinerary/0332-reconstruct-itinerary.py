class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         g = defaultdict(list)
#         for a, b in sorted(tickets)[::-1]:
#             g[a].append(b)
        
#         route = []
#         def visit(airport):
#             while g[airport]:
#                 visit(g[airport].pop())
#             route.append(airport)
#         visit('JFK')
#         return route[::-1]

    def _DFS(self, graph, node):
        neighbors = graph[node]
        while neighbors:
            nei = neighbors.pop(0)
            self._DFS(graph, nei)
        self.itinerary.append(node)
    
    def _makeGraph(self, edges):
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
        return g

    def findItinerary(self, tickets):
        tickets.sort(key= lambda x: x[1])
        g = self._makeGraph(tickets)
        self.itinerary = []
        self._DFS(g, "JFK")
        return self.itinerary[::-1]