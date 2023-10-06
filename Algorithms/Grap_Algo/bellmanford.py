def bellman_ford(graph, source):
    # Initialize distance from source to all other vertices as INFINITE
    distance = {vertex: float('infinity') for vertex in graph}
    distance[source] = 0

    # Relax all edges V-1 times (where V is the number of vertices)
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                if distance[vertex] != float('infinity') and distance[vertex] + weight < distance[neighbor]:
                    distance[neighbor] = distance[vertex] + weight

    # Check for negative weight cycles. If we get a shorter path on V-th iteration, 
    # then there is a cycle.
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            if distance[vertex] != float('infinity') and distance[vertex] + weight < distance[neighbor]:
                print("Graph contains a negative weight cycle!")
                return None

    return distance

# Example graph
graph = {
    'A': [('B', -1), ('C', 4)],
    'B': [('C', 3), ('D', 2), ('E', 2)],
    'C': [],
    'D': [('B', 1), ('C', 5)],
    'E': [('D', -3)]
}

print(bellman_ford(graph, 'A'))
