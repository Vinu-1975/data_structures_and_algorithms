import sys

def TSP(graph, v, currPos, n, count, cost, ans):
    # Last node and path back to the start node
    if count == n and graph[currPos][0]:
        ans = min(ans, cost + graph[currPos][0])
        return ans

    # BACKTRACKING STEP
    # Loop to traverse the adjacency list
    # of currPos node and increasing the count
    # by 1 and cost by graph[currPos][i] value
    for i in range(n):
        if v[i] == False and graph[currPos][i]:
            # Mark as visited
            v[i] = True
            ans = TSP(graph, v, i, n, count + 1, cost + graph[currPos][i], ans)
            # Mark ith node as unvisited
            v[i] = False

    return ans

# Driver Code
if __name__ == '__main__':
    # n is the number of nodes i.e. V
    n = 4
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]

    # Boolean array to check if a node
    # has been visited or not
    v = [False for i in range(n)]
    
    # Mark 0th node as visited
    v[0] = True

    ans = sys.maxsize

    # Find the minimum weight Hamiltonian Cycle
    ans = TSP(graph, v, 0, n, 1, 0, ans)

    # ans is the minimum weight Hamiltonian Cycle
    print(ans)
