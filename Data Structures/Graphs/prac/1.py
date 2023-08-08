class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self,v):
        if v not in self.graph:
            self.graph[v] = []

    def addEdge(self,v1,v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def removeEdge(self,v1,v2):
        if v1 in self.graph and v2 in self.graph:
            try:
                self.graph[v1].remove(v2)
                self.graph[v2].remove(v1)
            except ValueError:
                pass
    
    def removeVertex(self,v):
        if v in self.graph:
            for neighbour in self.graph[v]:
                self.removeEdge(v,neighbour)

    def DFS(self,start_vertex):
        visited = []

        def _DFS(start_vertex,visited):
            visited.append(start_vertex)
            print(start_vertex,end=" ")
            for neighbour in self.graph[start_vertex]:
                if neighbour not in visited:
                    _DFS(neighbour,visited)
        _DFS(start_vertex,visited)
        print()
        return
            
    
    def BFS(self,start_vertex):
        visited = []
        q = []
        q.append()
        while q:
            m = q.pop(0)
            for neighbour in self.graph[m]:
                if neighbour not in visited:
                    q.append(neighbour)
                    visited.append(neighbour)

    def detect_cycle_dfs(self,start_vertex):
        visited = {}
        for vertex in self.graph:
            visited[vertex] = False

        for vertex in self.graph:
            if not visited[vertex]:
                if self.detect_cycle_util(vertex,None,visited):
                    return True
        return False
    
    def detect_cycle_util(self,vertex,parent,visited):
        visited[vertex] = True
        for neighbour in self.graph[vertex]:
            if not visited[neighbour]:
                if self.detect_cycle_util(neighbour,parent,visited):
                    return True
            elif neighbour != parent:
                return True
        return False
            


if __name__ == "__main__":
    G = Graph()
    G.addVertex('A')
    G.addVertex('B')
    G.addVertex('C')
    G.addVertex('D')
    G.addVertex('E')
    G.addVertex('F')

    G.addEdge('A','B')
    G.addEdge('A','C')
    G.addEdge('A','D')
    G.addEdge('B','E')
    G.addEdge('B','F')
    G.addEdge('C','F')

    G.DFS('A')
    # print(G.BFS('A'))

    # print(G.detect_cycle_dfs('A'))