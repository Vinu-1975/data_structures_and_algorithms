


class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        
    def addEdge(self,v1,v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def __str__(self):
        return f"{self.graph}"
    
    def removeVertex(self,vertex):
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                self.removeEdge(vertex,neighbour)
    
    def removeEdge(self,v1,v2):
        if v1 in self.graph and v2 in self.graph:
            try:
                self.graph[v1].remove(v2)
                self.graph[v2].remove(v1)
            except ValueError:
                pass
    
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
        q.append(start_vertex)
        visited.append(start_vertex)
        while q:
            m = q.pop(0)
            for neighbour in self.graph[m]:
                if neighbour not in visited:
                    q.append(neighbour)
                    visited.append(neighbour)
        return visited
    
    def bfs_has_cycle(self, start_vertex):

        self.visited = {}
        self.parent = {}
        for i in self.adj_list:

            self.visited[i] = False
            self.parent[i] = None

        queue = []
        queue.append(start_vertex)
        self.visited[start_vertex] = True


        while len(queue) != 0:
            m = queue.pop(0)
            # print(m, end="->")
            for neighbour in self.adj_list[m]:
                if not self.visited[neighbour]:
                    self.visited[neighbour] = True
                    self.parent[neighbour] = m

                    queue.append(neighbour)
                elif neighbour != self.parent[m]:
                    
                    return True
        return False

    def dfs_has_cycle(self):
        visited = {}
        for v in self.graph:
            visited[v] = False

        for v in self.graph:
            if not visited[v]:
                if self.dfs_has_cycle_util(v, None, visited):
                    return True
        return False

    def dfs_has_cycle_util(self, vertex, parent, visited):
        visited[vertex] = True
        for neighbour in self.graph[vertex]:
            if not visited[neighbour]:
                if self.dfs_has_cycle_util(neighbour, vertex, visited):
                    return True
            elif neighbour != parent:
                return True
        return False
    
    def topologicalSortDFS(self):
        visited = set()
        stack = []

        def dfs(vertex):
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(vertex)

        for vertex in self.graph:
            if vertex not in visited:
                dfs(vertex)

        return stack[::-1]
    
    def find_dag_root(self):
        # Initialize the set of potential root vertices
        roots = set(self.graph.keys())

        # Remove vertices with incoming edges
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if neighbor in roots:
                    roots.remove(neighbor)

        # Check if there is a single root or no root
        if len(roots) == 1:
            return roots.pop()
        else:
            return None



if __name__ == "__main__":
    G = Graph()
    # G.addVertex('A')
    # G.addVertex('B')
    # G.addVertex('C')
    # G.addVertex('D')
    # G.addVertex('E')
    # G.addVertex('F')

    #cycles detection
    # G.addEdge('A','B')
    # G.addEdge('A','C')
    # G.addEdge('A','D')
    # G.addEdge('B','E')
    # G.addEdge('B','F')
    # G.addEdge('C','F')

    # G.addEdge('A','B')
    # G.addEdge('A','C')
    # G.addEdge('C','D')
    # G.addEdge('B','D')
    # G.addEdge('D','E')

    # G.DFS('A')
    # print(G.BFS('A'))

    G.addVertex(1)
    G.addVertex(2)
    G.addVertex(3)
    G.addVertex(4)
    G.addVertex(5)
    G.addVertex(6)

    #topological sorting
    G.addEdge(1,2)
    G.addEdge(1,3)
    G.addEdge(2,4)
    G.addEdge(3,4)
    G.addEdge(4,5)
    G.addEdge(4,6)
    G.addEdge(2,5)
    G.addEdge(3,6)

    print(G.dfs_has_cycle())
    print(G.topologicalSortDFS())
    # print(G.topological_sort())
    print(G.find_dag_root())
