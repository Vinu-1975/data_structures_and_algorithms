import heapq

def dijkstra(graph,k,n):
    shortest_time = { node:float('inf') for node in range(1,n+1)}
    shortest_time[k] = 0
    pq = [(0,k)]
    while pq:
        current_time, current_node = heapq.heappop(pq)

        if current_time > shortest_time[current_node]:
            continue

        for item in graph:
            if item[0] == current_node:
                neighbor,time = item[1],item[2]
                total_time = time + current_time
                if total_time < shortest_time[neighbor]:
                    shortest_time[neighbor] = total_time
                    heapq.heappush(pq,(total_time,neighbor))
    
    return max(shortest_time.values())

graph = [[2,1,1],[2,3,1],[3,4,1]]
# new_graph = {}
# for item in graph:
#     if item[0] in new_graph:
#         new_graph[item[0]].append((item[1],item[2]))
#     else:
#         new_graph[item[0]] = [(item[1],item[2])]
# print(new_graph)
n=4
k=2
print(dijkstra(graph,k,n))