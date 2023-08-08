import heapq

def dijkstra(graph,src,dst):
    node_data = {}
    for item in graph:
        node_data[item] = {'cost':float("inf"),'pred':[]}

    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(len(node_data)):
        if temp not in visited:
            visited.append(temp)
            minHeap = []
            for neighbour in graph[temp]:
                if neighbour not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][neighbour]
                    if cost < node_data[neighbour]['cost']:
                        node_data[neighbour]['cost'] = cost
                        node_data[neighbour]['pred'] = node_data[temp]['pred'] + [temp]
                    heapq.heappush(minHeap,(node_data[neighbour]['cost'],neighbour))
            heapq.heapify(minHeap)
            if len(minHeap) > 0:
                temp = minHeap[0][1]
    print("SHortest Distance : ",node_data[dst]['cost'])
    print("Shortest Path : ",node_data[dst]['pred'] + [temp])

if __name__ == "__main__":
    graph = {
        "A": {"B": 2, "C": 4},
        "B": {"A": 2, "C": 3, "D": 8},
        "C": {"A": 4, "B": 3, "E": 5, "D": 2},
        "D": {"B": 8, "C": 2, "E": 11, "F": 22},
        "E": {"C": 5, "D": 11, "F": 1},
        "F": {"D": 22, "E": 1},
    }

    dijkstra(graph, "A", "F")
