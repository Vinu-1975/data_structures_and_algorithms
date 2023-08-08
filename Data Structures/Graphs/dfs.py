class Graph:

    def __init__(self):
        self.graph = {}

    def add_node(self,node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self,n1,n2):
        if n1 in self.graph and n2 in self.graph:
            self.graph[n1].append(n2)
            self.graph[n2].append(n1)

    def get_neighbours(self,node):
        if node in self.graph:
            return self.graph[node]
        return []
    
    def __str__(self):
        return str(self.graph)
    
    def bfs(self,node):
        visited = []
        queue = []
        queue.append(node)
        visited.append(node)

        while len(queue) > 0:
            m = queue.pop(0)
            for neighbour in self.graph[m]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)
        
        return visited
    
    def dfs(self,node):
        visited = []
        stack = []
        stack.append(node)

        while stack:
            m = stack.pop()
            if m not in visited:
                visited.append(m)
                for neighbour in self.graph[m]:
                    if neighbour not in visited:
                        stack.append(neighbour)

        return visited
    
    



if __name__ == "__main__":
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_node(8)
    g.add_node(9)
    g.add_node(10)

    g.add_edge(1,4)
    g.add_edge(1,2)
    g.add_edge(4,3)
    g.add_edge(2,3)
    g.add_edge(3,10)
    g.add_edge(3,9)
    g.add_edge(2,5)
    g.add_edge(2,7)
    g.add_edge(2,8)
    g.add_edge(5,8)
    g.add_edge(5,6)
    g.add_edge(5,7)
    g.add_edge(7,8)

    # print(g)
    # print(g.bfs(1))
    print(g.dfs(1))
