def isSafe(graph, color):
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] and color[i] == color[j]:
                return False
    return True


def graphColoring(graph, m, i, color):
    if i == len(graph):
        if isSafe(graph, color):
            return True
        return False

    for j in range(1, m + 1):
        color[i] = j
        if graphColoring(graph, m, i + 1, color):
            return True
        color[i] = 0

    return False


def solveGraphColoring(graph, m):
    color = [0] * len(graph)
    if not graphColoring(graph, m, 0, color):
        return None
    return color


# Example usage
graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3  # Number of colors
coloring = solveGraphColoring(graph, m)
print("Coloring of the graph:" if coloring else "Solution does not exist", coloring)
