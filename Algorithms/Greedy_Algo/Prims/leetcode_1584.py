from heapq import heappush,heappop

def manhattan_distance(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
p1 = tuple(points[0])
graph = {tuple(vertex):[v for v in points if v!=vertex] for vertex in points}
# start = graph[tuple(p1)]
mst = []
visited = set()
pq = [(0,p1,None)]
i=0
while pq:
    cost,curr,prev = heappop(pq)
    # print(cost,curr,prev)
    if curr in visited:
        continue
    visited.add(curr)
    if prev:
        mst.append((prev,curr,cost))
    for item in graph[curr]:
        neighbor = tuple(item)
        cost = manhattan_distance(curr,neighbor)
        # print(neighbor,cost)
        if neighbor not in visited:
            heappush(pq,(cost,neighbor,curr))
    
print(mst)
total_cost = sum(edge[2] for edge in mst)
print(total_cost)