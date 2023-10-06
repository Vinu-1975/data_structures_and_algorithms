from heapq import heappush,heappop
def prim(graph,start):
    mst = []
    visited = set()
    pq = [(0,start,None)]
    while pq:
        cost,curr,prev = heappop(pq)

        if curr in visited:
            continue
        visited.add(curr)
        if prev:
            mst.append((prev,curr,cost))
        for neighbor,cost in graph[curr]:
            if neighbor not in visited:
                heappush(pq,(cost,neighbor,curr))
    return mst



graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
mst = prim(graph, 'A')
print(mst)