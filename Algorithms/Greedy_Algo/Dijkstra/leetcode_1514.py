from heapq import heappush, heappop

def dijkstra(edges,succProb,n,start,end):
    graph = {v:list() for v in range(n)}

    for i in range(len(edges)):
        if edges[i][0] in graph:
            graph[edges[i][0]].append((edges[i][1],succProb[i]))
        if edges[i][1] in graph:
            graph[edges[i][1]].append((edges[i][0],succProb[i]))

    max_prob = {v:0 for v in range(n)}
    max_prob[start] = 1
    pq = [(-1,start)]
    while pq:
        current_probability, current_vertex = heappop(pq)
        current_probability = -current_probability
        if current_probability < max_prob[current_vertex]:
            continue
        for neighbor,prob in graph[current_vertex]:
            new_prob = prob * current_probability
            if new_prob > max_prob[neighbor]:
                max_prob[neighbor] = new_prob
                heappush(pq,(-new_prob,neighbor))
    return max_prob[end]

edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
n = 3
start = 0
end = 2
print(dijkstra(edges,succProb,n,start,end))