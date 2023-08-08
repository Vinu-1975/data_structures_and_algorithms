class graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self,v):
        if v not in self.graph:
            self.graph[v] = []

    def addEdge(self,v1,v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def removeEdges(self,v1,v2):
        if v1 in self.graph and v2 in self.graph:
            try:
                self.graph[v1].remove(v2)
                self.graph[v2].remove(v1)
            except ValueError:
                pass
    
    def removeVertex(self,v):
        for v in self.graph:
            for neighbour in self.graph[v]:
                self.removeEdge(v,neighbour)

    def DFS(self,v):
        visited = []

        def _DFS(v,visited):
            visited.append(v)
            print(v,end = " ")
            for neighbour in self.graph[v]:
                if neighbour not in visited:
                    _DFS(neighbour,visited)
        _DFS(v,visited)
        print()
        return
    
    def BFS(self,v):
        visited = []
        q = []
        q.append(v)
        visited.append(v)
        while q:
            m = q.pop(0)
            for neighbour in self.graph[v]:
                if neighbour not in visited:
                    q.append(neighbour)
                    visited.append(neighbour)

    def has_cycle_dfs(self):
        visited = []
        for vertex in self.graph:
            if vertex not in visited:
                if self.cyc_util(vertex,None,visited):
                    return True
                
        return False
    def cyc_util(self,vertex,parent,visited):
        visited.append(vertex)
        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                if self.cyc_util(neighbour,vertex,visited):
                    return True
            elif neighbour != parent:
                return True
            
        return False
            
    

    

