from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def addNode(self,u):
        self.graph[u] = []

    def __str__(self):
        return str(self.graph)
    
    def m(self):
        return max(self.graph)



    
if __name__ == "__main__":
    g = Graph()
    g.addEdge('a', 'b')
    g.addEdge('a', 'c')
    g.addEdge('b', 'c')
    g.addEdge('c', 'a')
    g.addEdge('c', 'd')
    g.addEdge('d', 'd')

    print(g)

    print(g.m())