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
    graph_list = {i:{} for i in range(n)}

    for _ in range(m):
        x,y,t = map(int,input().split())
        graph_list[x-1][y-1] = t
        graph_list[y-1][x-1] = t

    distances_pq = dijkstra_priority_queue(graph_list,0)
    print(distances_pq)


