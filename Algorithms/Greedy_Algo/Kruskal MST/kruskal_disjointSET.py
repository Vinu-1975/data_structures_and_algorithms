# Disjoint Set (Union-Find) implementation
class DisjointSet:
    """
    find: Looks for the representative of an item's set.
    union: Merges the sets of two items based on their representatives.
    """

    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        # It checks if the item is its own parent. If item is its own parent, it means item is the representative of its set.
        if self.parent[item] != item:
            # If item is not its own parent, then the function calls itself recursively for the parent of item. This is to trace up the tree to find the root (or representative) of the item.
            # While doing this recursive tracing, self.parent[item] = self.find(self.parent[item]) updates the parent of the current item directly to the root (this is the path compression optimization).
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        # If rootX and rootY are different (meaning x and y are from different sets), it proceeds to merge the sets.
        if rootX != rootY:
            # If rootX has a smaller rank than rootY, then rootX's parent becomes rootY. This means the tree with rootX gets attached below the tree with rootY.
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            # If rootY has a rank that's less than or equal to rootX, then rootY's parent becomes rootX. In the case where their ranks are equal, we've essentially increased the height of the tree with rootX by adding the tree with rootY below it, so we increment the rank of rootX by 1.
            else:
                self.parent[rootY] = rootX
                if self.rank[rootX] == self.rank[rootY]:
                    self.rank[rootX] += 1


def kruskal(graph):
    # Create a list of all edges in the graph
    edges = []
    for node, neighbors in graph.items():  #* O(V+E)
        for neighbor, weight in neighbors:
            edges.append((weight, node, neighbor))

    # Sort edges by weight
    edges.sort()  # * O(ElogE)

    # Use disjoint-set to check for cycles
    ds = DisjointSet(graph.keys())

    mst = []
    for edge in edges:  #* O(E)
        weight, node1, node2 = edge
        # We check if its nodes node1 and node2 belong to the same set using the find operation. If they do (ds.find(node1) == ds.find(node2)), adding this edge would create a cycle, so it's skipped.
        if ds.find(node1) != ds.find(node2):
            # If they belong to different sets, adding the edge won't create a cycle. Thus, the edge is added to the mst and the sets containing node1 and node2 are unioned together.
            mst.append(edge)
            ds.union(node1, node2)

    return mst


# Example usage
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1)],
}
mst = kruskal(graph)
print(mst)
