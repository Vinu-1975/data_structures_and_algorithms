from heapq import heappush, heappop
def dijkstra(graph,start):

    shortest_path = { vertex:float('inf') for vertex in graph}
    shortest_path[start] = 0
    pq = [(0,start)]
    while pq:
        current_weight, current_vertex = heappop(pq)

        if current_weight > shortest_path[current_vertex]:
            continue

        for neighbor,weight in graph[current_vertex]:
            distance = current_weight + weight
            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                heappush(pq,(distance,neighbor))

    return shortest_path

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
print(dijkstra(graph, 'A'))  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}