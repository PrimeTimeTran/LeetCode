'''
Create G/adj list using edges.

Iterate from 0 - n-1 finding max path of each node, add vertice and depth to list.

Find lowest value/values of list and return those vertices.
'''

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n <= 2:
            return [i for i in range(n)]

        neighbors = defaultdict(set)
        for a, b in edges:
            neighbors[a].add(b); neighbors[b].add(a)

        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves