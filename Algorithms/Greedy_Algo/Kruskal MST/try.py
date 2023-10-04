
class DisjointSet:
    def __init__(self,vertex):
        self.parent = {v:v for v in vertex}
        self.rank = {v:0 for v in vertex}

    def find(self,item):
        if self.parent[item]!=item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                if self.rank[rootY] == self.rank[rootX]:
                    self.rank[rootX] += 1




def kruskal(graph):
    edges = []
    for node,neighbors in graph.items():
        for neighbor,cost in neighbors:
            edges.append((cost,node,neighbor))
    edges.sort()
    mst = []
    ds = DisjointSet(graph.keys())

    for edge in edges:
        weight,n1,n2 = edge
        if ds.find(n1) != ds.find(n2):
            mst.append(edge)
            ds.union(n1,n2)
    return mst

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1)],
}
mst = kruskal(graph)
print(mst)