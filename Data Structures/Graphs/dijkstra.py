import sys
from heapq import heappush, heappop, heapify

def djikstra(graph, src, dest):
    inf = sys.maxsize
    node_data = {
        'A': {'cost': inf, 'pred': []},
        'B': {'cost': inf, 'pred': []},
        'C': {'cost': inf, 'pred': []},
        'D': {'cost': inf, 'pred': []},
        'E': {'cost': inf, 'pred': []},
        'F': {'cost': inf, 'pred': []}
    }

    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(len(node_data)):  # Corrected the range from 5 to 6
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for neighbour in graph[temp]:
                if neighbour not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][neighbour]
                    if cost < node_data[neighbour]['cost']:
                        node_data[neighbour]['cost'] = cost
                        node_data[neighbour]['pred'] = node_data[temp]['pred'] + [temp]  # Corrected the list concatenation
                    heappush(min_heap, (node_data[neighbour]['cost'], neighbour))  # Added the neighbour as the second element
            heapify(min_heap)
            if len(min_heap) > 0:  # Added this check to handle the case when there are no more reachable vertices
                temp = min_heap[0][1]

    print("shortest distance:", node_data[dest]['cost'])  # Corrected the print statements
    print("shortest path:", node_data[dest]['pred'] + [dest])


if __name__ == "__main__":
    graph = {
        'A': {'B': 2, 'C': 4},
        'B': {'A': 2, 'C': 3, 'D': 8},
        'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
        'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
        'E': {'C': 5, 'D': 11, 'F': 1},
        'F': {'D': 22, 'E': 1}
    }

    djikstra(graph, 'A', 'F')