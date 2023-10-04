import heapq

def prim(graph, start):
    mst = []  # List to store edges of the Minimum Spanning Tree
    visited = set()  # Set to keep track of visited nodes
    pq = [(0, start, None)]  # Priority queue initialized with the start node

    while pq:
        cost, current, prev = heapq.heappop(pq)  # Pop the edge with the smallest weight
        if current in visited:
            continue
        visited.add(current)
        if prev is not None:
            mst.append((prev, current, cost))

        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (weight, neighbor, current))

    return mst

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
mst = prim(graph, 'A')
print(mst)  # This will print the edges of the Minimum Spanning Tree
