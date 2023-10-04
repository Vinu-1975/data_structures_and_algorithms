# Disjoint Set (Union-Find) implementation
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                if self.rank[rootX] == self.rank[rootY]:
                    self.rank[rootX] += 1

def kruskal(graph):
    # Create a list of all edges in the graph
    edges = []
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            edges.append((weight, node, neighbor))
    
    # Sort edges by weight
    edges.sort()

    # Use disjoint-set to check for cycles
    ds = DisjointSet(graph.keys())

    mst = []
    for edge in edges:
        weight, node1, node2 = edge
        if ds.find(node1) != ds.find(node2):
            mst.append(edge)
            ds.union(node1, node2)

    return mst

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
mst = kruskal(graph)
print(mst)
