def bellman_ford(graph,source):
    distance = {vertex:float('inf') for vertex in graph}
    distance[source] = 0

    for i in range(len(graph) - 1):
        for vertex in graph:
            for neighbor,weight in graph[vertex]:
                if distance[vertex] != float('inf') and distance[vertex] + weight < distance[neighbor]:
                    distance[neighbor] = distance[vertex] + weight
    
    for vertex in graph:
        for neighbor,weight in graph[vertex]:
            if distance[vertex]!=float('inf') and distance[vertex] + weight < distance[neighbor]:
                print("NEgative cycle found")
                return None
            
    return distance


graph = {
    'A': [('B', -1), ('C', 4)],
    'B': [('C', 3), ('D', 2), ('E', 2)],
    'C': [],
    'D': [('B', 1), ('C', 5)],
    'E': [('D', -3)]
}

print(bellman_ford(graph, 'A'))