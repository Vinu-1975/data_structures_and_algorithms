

import sys

class GraphColoring:
    def __init__(self, graph, num_colors):
        self.graph = graph
        self.num_colors = num_colors
        self.V = len(graph)
        self.color = [-1] * self.V

    def isSafe(self, v, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and self.color[i] == c:
                return False
        return True

    def graphColoringUtil(self, m, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, c):
                self.color[v] = c
                if self.graphColoringUtil(m, v + 1):
                    return True
                self.color[v] = -1

        return False

    def graphColoring(self):
        if self.graphColoringUtil(self.num_colors, 0):
            return self.color
        return None

# Example usage
graph = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]
num_colors = 3

coloring = GraphColoring(graph, num_colors)
result = coloring.graphColoring()
result



