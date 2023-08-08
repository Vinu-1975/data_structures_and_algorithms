class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def get_neighbors(self, node):
        if node in self.graph:
            return self.graph[node]
        else:
            return []

    def __str__(self):
        return str(self.graph)


# Example usage:
g = Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_edge(1, 2)
g.add_edge(2, 3)

print(g)  # Output: {1: [2], 2: [1, 3], 3: [2]}

neighbors = g.get_neighbors(2)
print(neighbors)  # Output: [1, 3]
