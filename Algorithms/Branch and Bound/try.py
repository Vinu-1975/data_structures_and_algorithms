N Queens

In [22]:
def printsol(s,n):
    for i in range(n):
        for j in range(n):
            if s[i][j] == 1:
                print('q', end=' ')
            else:
                print('.', end=' ')
        print('\n')
def safe(s,row,col):
    for i in range(col):
        if s[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if s[i][j]==1:
            return False
    for i,j in zip(range(row,n,1), range(col,-1,-1)):
        if s[i][j]==1:
            return False
    return True
def nqueenplace(s,col,n):
    if col>=n:
        return True
    for i in range(n): # each row we are moving by fixing the column
        if safe(s,i,col):
            s[i][col]= 1 
            if nqueenplace(s,col+1,n)==True:
                return True 
            s[i][col]=0
    return False

s = [[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]
n=4
if(nqueenplace(s,0,n)):
    print(printsol(s,n))
else:
    print('solution not found')






GRAPH COLORING

In [1]:
def color_houses(houses, num_colors):
    n = len(houses)
    colors = [-1] * n

    def is_safe(house, color):
        for neighbor in houses[house]:
            if colors[neighbor] == color:
                return False
        return True

    def color_util(house):
        if house == n:
            return True

        for color in range(num_colors):
            if is_safe(house, color):
                colors[house] = color

                if color_util(house + 1):
                    return True

                colors[house] = -1

        return False

    if color_util(0):
        print("Solution exists. Assigned colors:", colors)
    else:
        print("No solution exists.")

# Example usage
houses_adjacency = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2]
}


num_colors = 3

color_houses(houses_adjacency, num_colors)





0/1 Knapsack

In [12]:
def knapsack_backtracking(weights, values, capacity):
    n = len(weights)
    max_value = [0]

    def knapsack_util(curr_value, curr_weight, index):
        if index == n:
            max_value[0] = max(max_value[0], curr_value)
            return

        # Include the current item if it doesn't exceed the capacity
        if curr_weight + weights[index] <= capacity:
            knapsack_util(curr_value + values[index], curr_weight + weights[index], index + 1)

        # Exclude the current item and move to the next one
        knapsack_util(curr_value, curr_weight, index + 1)

    knapsack_util(0, 0, 0)
    return max_value[0]

# Example usage
weights = [1,2,3,4,5]
values = [3, 4, 2, 10,7]
capacity =10

result = knapsack_backtracking(weights, values, capacity)
print(f"The maximum value for the 0/1 Knapsack problem is: {result}")





Dynamic Programming:

While the approach involves exploring all possible combinations, it doesn't store intermediate results or solutions. Therefore, this implementation is a pure backtracking approach and not dynamic programming. Dynamic programming typically involves storing and reusing solutions to subproblems to avoid redundant computations. In dynamic programming for the knapsack problem, a table is often used to memoize the solutions to subproblems, leading to improved efficiency.

Subset Sum

In [21]:
has_valid_subset = False

def print_subset_with_sum(current_index, array_size, input_set, target_sum, current_subset):
    global has_valid_subset

    # If the target_sum is zero, then there exists a subset
    if target_sum == 0:
        # Prints the valid subset
        has_valid_subset = True
        print("[", end=" ")
        for element in current_subset:
            print(element, end=" ")
        print("]", end=" ")
        return

    if current_index == array_size:
        # Return if we have reached the end of the array
        return

    # Consider the current element if it is less than or equal to target_sum
    if input_set[current_index] <= target_sum:
        # Push the current element into the subset
        current_subset.append(input_set[current_index])

        # Recursive call for considering the current element
        print_subset_with_sum(current_index + 1, array_size, input_set, target_sum - input_set[current_index], current_subset)

        # Remove the last element after the recursive call to restore the subset's original configuration
        current_subset.pop()

    # Not considering the current element
    print_subset_with_sum(current_index + 1, array_size, input_set, target_sum, current_subset)

# Driver code
if _name_ == "_main_":
    # Test case
    input_array = [3, 34, 4, 12, 5, 30]
    target_sum_value = 30
    array_size_value = len(input_array)
    current_subset_list = []

    print("Output:")
    print_subset_with_sum(0, array_size_value, input_array, target_sum_value, current_subset_list)

    if not has_valid_subset:
        print("There is no such subset.")





Hamiltonian Cycle

In [27]:
def is_valid(v, pos, path, graph):
    if graph[path[pos - 1]][v] == 0:
        return False

    if v in path:
        return False

    return True

def hamiltonian_cycle_util(graph, path, pos):
    # to check if you can connect the last vertex back to first one in order to form a cycle
    if pos == len(graph):
        # Check if the last vertex connects to the starting vertex
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    for v in range(1, len(graph)):
        if is_valid(v, pos, path, graph):
            path[pos] = v

            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True

            path[pos] = -1

    return False

def hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0  # Start from the first vertex

    if not hamiltonian_cycle_util(graph, path, 1):
        print("Hamiltonian Cycle does not exist.")
        return None

    print("Hamiltonian Cycle:")
    for vertex in path:
        print(vertex, end=" ")
    print(path[0])  # Complete the cycle

# Example usage
graph_example = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

hamiltonian_cycle(graph_example)







Hamiltonian Path

In [24]:
def is_valid(v, pos, path, graph):
    if graph[path[pos - 1]][v] == 0:
        return False

    if v in path:
        return False

    return True

def hamiltonian_path_util(graph, path, pos):
    if pos == len(graph):
        return True

    for v in range(1, len(graph)):
        if is_valid(v, pos, path, graph):
            path[pos] = v

            if hamiltonian_path_util(graph, path, pos + 1):
                return True

            path[pos] = -1

    return False

def hamiltonian_path(graph):
    path = [-1] * len(graph)
    path[0] = 0  # Start from the first vertex

    if not hamiltonian_path_util(graph, path, 1):
        print("Hamiltonian Path does not exist.")
        return None

    print("Hamiltonian Path:")
    for vertex in path:
        print(vertex, end=" ")
    print()

# Example usage
graph_example = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

hamiltonian_path(graph_example)







BRANCH AND BOUND
0/1 Knapsack

In [32]:
import heapq

class Node:
    def _init_(self, level, value, weight, bound):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound

    def _lt_(self, other):
        return self.bound > other.bound  # Max heap based on bound

def bound(node, n, W, items):
    if node.weight >= W:
        return 0

    value_bound = node.value
    j = node.level + 1
    totweight = node.weight

    while j < n and totweight + items[j][1] <= W:
        totweight += items[j][1]
        value_bound += items[j][0]
        j += 1

    if j < n:
        value_bound += (W - totweight) * items[j][0] / items[j][1]

    return value_bound

def knapsack(items, W):
    items.sort(key=lambda x: x[0]/x[1], reverse=True)  # Sort based on value/weight ratio
    n = len(items)

    queue = []
    heapq.heappush(queue, Node(-1, 0, 0, 0.0))

    max_value = 0

    while queue:
        current = heapq.heappop(queue)

        if current.level == n-1:
            continue

        next_level = current.level + 1

        # Branch including the next item
        next_weight = current.weight + items[next_level][1]
        next_value = current.value + items[next_level][0]

        if next_weight <= W and next_value > max_value:
            max_value = next_value

        next_bound = bound(current, n, W, items)

        if next_bound > max_value:
            heapq.heappush(queue, Node(next_level, next_value, next_weight, next_bound))

        # Branch excluding the next item
        next_bound = bound(Node(current.level, current.value, current.weight, 0), n, W, items)
        if next_bound > max_value:
            heapq.heappush(queue, Node(next_level, current.value, current.weight, next_bound))

    return max_value

# Example usage
items = [(60, 10), (100, 20), (120, 30)]  # Each tuple is (value, weight)
W = 50  # Maximum weight capacity
print("Maximum value:", knapsack(items, W))







Travelling Sales Man

In [33]:
import heapq


def calculate_lower_bound(matrix, path):
    remaining_cities = [i for i in range(len(matrix)) if i not in path]
    if not remaining_cities:
        return 0  # All cities are in the path

    lower_bound = sum(min(matrix[path[i]]) for i in range(len(path) - 1))
    lower_bound += min(matrix[path[-1]][city] for city in remaining_cities)
    return lower_bound


def branch_and_bound_tsp(distance_matrix):
    # Priority queue for the nodes to explore
    queue = []
    heapq.heappush(queue, (0, [0]))  # Starting with the first city

    best_cost = float('inf')
    best_path = []

    while queue:
        cost, path = heapq.heappop(queue)

        if len(path) == len(distance_matrix) and cost < best_cost:
            best_cost = cost
            best_path = path
            continue

        for next_city in range(len(distance_matrix)):
            if next_city not in path:
                new_path = path + [next_city]
                new_cost = cost + distance_matrix[path[-1]][next_city]

                if new_cost < best_cost:
                    lower_bound = calculate_lower_bound(distance_matrix, new_path)
                    if lower_bound < best_cost:
                        heapq.heappush(queue, (new_cost, new_path))

    return best_path, best_cost


# Example usage
distance_matrix = [[0, 20, 30, 10, 11], [15, 0, 16, 4, 2], [3, 5, 0, 2, 4], [14, 6, 18, 0, 3], [16, 4, 7, 16, 0]]
path, cost = branch_and_bound_tsp(distance_matrix)
print("Path:", path)
print("Cost:", cost)






Job Assignment

In [35]:
import numpy as np
#from itertools import permutations
def cost(matrix, assignment):
    total_cost = 0
    for i, j in enumerate(assignment):
        total_cost += matrix[i, j]
    return total_cost
def bound(matrix, assignment):
    # Calculate the cost of the current assignment plus the minimum possible additional cost
    total_cost = cost(matrix, assignment)
    # Calculate the minimum cost for unassigned jobs
    for i in range(len(assignment), matrix.shape[0]):
        min_cost = np.min(matrix[i, np.setdiff1d(range(matrix.shape[1]), assignment)])
        total_cost += min_cost
    return total_cost
def branch_and_bound(matrix):
    n = matrix.shape[0]
    # Initialize variables
    best_cost = float('inf')
    best_assignment = None
    stack = [(0, [])]  
    while stack:
        level, assignment = stack.pop()
        if level == n:
            current_cost = cost(matrix, assignment)
            if current_cost < best_cost:
                best_cost = current_cost
                best_assignment = assignment
        else:
            for j in range(n):
                if j not in assignment:
                    new_assignment = assignment + [j]
                    current_bound = bound(matrix, new_assignment)
                    # Only explore if the bound is less than the best cost
                    if current_bound < best_cost:
                        stack.append((level + 1, new_assignment))
    return best_assignment
# Example usage
#matrix = np.array([[9, 2, 7,8], [6, 4, 3 ,7], [5, 8, 1, 8],[7, 6, 9, 4]])
matrix = np.array([[11, 4, 9,10], [8, 6, 5,9], [7, 10, 3,10],[9,8,11,6]])
assignment = branch_and_bound(matrix)
print("Optimal Assignment:", assignment)
print("Optimal Cost:", cost(matrix, assignment))







Job Scheduling

In [36]:
from queue import PriorityQueue

class Job:
    def _init_(self, job_id, deadline, penalty):
        self.job_id = job_id
        self.deadline = deadline
        self.penalty = penalty

    def _lt_(self, other):
        return self.penalty > other.penalty 

def job_sequencing_with_deadlines(jobs, max_deadline):
    job_queue = PriorityQueue()
    for job in jobs:
        job_queue.put(job)

    job_sequence = [-1] * max_deadline
    
    while not job_queue.empty():
        job = job_queue.get()
        for d in range(job.deadline - 1, -1, -1):
            if job_sequence[d] == -1:
                job_sequence[d] = job.job_id
                break

    return job_sequence

jobs = [Job("a", 2, 100), Job("b", 1, 19), Job("c", 2, 27), Job("d", 1, 25), Job("e", 3, 15)]
max_deadline = max(job.deadline for job in jobs)
scheduled_jobs = job_sequencing_with_deadlines(jobs, max_deadline)
print("Job sequence:", scheduled_jobs)