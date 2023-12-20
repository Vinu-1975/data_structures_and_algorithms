import sys
from heapq import heappush, heappop


class Node:
    def __init__(self, vertex, level, path, reduced_matrix, cost):
        self.vertex = vertex
        self.level = level
        self.path = path
        self.reduced_matrix = reduced_matrix
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


def copyMatrix(matrix):
    return [row[:] for row in matrix]


def reduceMatrix(matrix):
    # Row Reduction
    row_reduce = [min(row) if min(row) != sys.maxsize else 0 for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != sys.maxsize:
                matrix[i][j] -= row_reduce[i]

    # Column Reduction
    col_reduce = [
        min([matrix[i][j] for i in range(len(matrix))])
        if min([matrix[i][j] for i in range(len(matrix))]) != sys.maxsize
        else 0
        for j in range(len(matrix))
    ]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != sys.maxsize:
                matrix[i][j] -= col_reduce[j]

    # Calculate total reduction cost
    reduction_cost = sum(row_reduce) + sum(col_reduce)
    return reduction_cost


def TSPBranchAndBound(graph):
    n = len(graph)
    initial_reduced_matrix = copyMatrix(graph)
    initial_cost = reduceMatrix(initial_reduced_matrix)

    initial_path = [0]
    heap = []
    heappush(heap, Node(0, 0, initial_path, initial_reduced_matrix, initial_cost))

    min_cost = sys.maxsize
    best_path = []

    while heap:
        current = heappop(heap)

        if current.level == n - 1:
            last_edge_cost = current.reduced_matrix[current.vertex][0]
            if (
                last_edge_cost != sys.maxsize
                and current.cost + last_edge_cost < min_cost
            ):
                min_cost = current.cost + last_edge_cost
                best_path = current.path + [0]
            continue

        for i in range(n):
            if current.reduced_matrix[current.vertex][i] != sys.maxsize:
                new_path = current.path + [i]
                new_matrix = copyMatrix(current.reduced_matrix)

                # Set visited edges as infinity
                for j in range(n):
                    new_matrix[current.vertex][j] = sys.maxsize
                    new_matrix[j][i] = sys.maxsize
                new_matrix[i][0] = sys.maxsize  # Set edge to start node as infinity

                new_cost = (
                    current.cost
                    + current.reduced_matrix[current.vertex][i]
                    + reduceMatrix(new_matrix)
                )
                new_node = Node(i, current.level + 1, new_path, new_matrix, new_cost)

                # Add new node to heap
                heappush(heap, new_node)

    return min_cost, best_path


# Example usage
graph = [
    [sys.maxsize, 10, 15, 20],
    [10, sys.maxsize, 35, 25],
    [15, 35, sys.maxsize, 30],
    [20, 25, 30, sys.maxsize],
]

min_cost, path = TSPBranchAndBound(graph)
print(f"Minimum cost: {min_cost}")
print(f"Path: {path}")
