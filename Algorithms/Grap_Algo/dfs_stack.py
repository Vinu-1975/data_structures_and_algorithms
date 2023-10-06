class Graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self,x):
        self.graph[x] = []
    
    def add_edge(self,x,y):
        if x in self.graph and y in self.graph:
            self.graph[x].append(y)
    
    def DFS(self,start):
        visited = set()
        stack=[start]
        result=[]
        while stack:
            m=stack.pop()
            if m not in visited:
                result.append(m)
                visited.add(m)
                for neighbor in self.graph[m]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result


if __name__ == "__main__":
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_vertex('E')

    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('D', 'E')

    print(g.DFS('A'))  # Expected: ['A', 'B', 'C']
    print(g.DFS('D'))  # Expected: ['D', 'E']
    # g = Graph()
    # g.add_vertex('A')
    # g.add_vertex('B')
    # g.add_vertex('C')
    
    # g.add_edge('A', 'B')
    # g.add_edge('B', 'C')
    # g.add_edge('C', 'C')  # Loop at 'C'
    
    # print(g.DFS('A'))  # Expected: ['A', 'B', 'C']
