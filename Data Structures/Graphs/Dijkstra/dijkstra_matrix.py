
def dijkstra(graph,start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n

    for _ in range(n):
        u = min_distance(distances,visited)
        visited[u] = True

        for v in range(n):
            if not visited[v] and graph[u][v] and distances[u] + graph[u][v] < distances[v]:
                distances[v] = distances[u] + graph[u][v]
        
    return distances

def min_distance(distances,visited):
    min_val = float('inf')
    min_idx = -1

    for i in range(len(distances)):
        if not visited[i] and distances[i] < min_val:
            min_val = distances[i]
            min_idx = i
    return min_idx

import heapq

def dijkstra_priority_queue(graph,start):
    distances = { vertex: float('inf') for vertex in graph }
    distances[start] = 0

    pq = [(0,start)]
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq,(distance,neighbor))
    
    return distances

if __name__ == "__main__":
    n,m = map(int,input().split())
    graph_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        x,y,t = map(int,input().split())
        graph_matrix[x-1][y-1] = t
        graph_matrix[y-1][x-1] = t

    distances_matrix = dijkstra(graph_matrix,0)
    print(distances_matrix)
