import sys


class Node:
    def __init__(self, assigned, remaining, cost_so_far, cost_matrix):
        self.assigned = assigned  # List of assignments (worker, job)
        self.remaining = remaining  # Remaining workers and jobs
        self.cost_so_far = cost_so_far
        self.lower_bound = self.calculate_lower_bound(cost_matrix)

    def calculate_lower_bound(self, cost_matrix):
        # Lower bound is current cost plus minimum remaining cost
        lb = self.cost_so_far
        for worker in self.remaining:
            lb += min(cost_matrix[worker][j] for j in self.remaining)
        return lb


def jobAssignment(cost_matrix):
    n = len(cost_matrix)
    min_cost = sys.maxsize
    all_workers_jobs = set(range(n))

    def dfs(node):
        nonlocal min_cost
        print("bound:",node.lower_bound)
        if node.lower_bound >= min_cost:
            return  # Pruning

        if len(node.assigned) == n:
            min_cost = min(min_cost, node.cost_so_far)
            return

        worker = len(node.assigned)  # Next worker to assign
        for job in node.remaining:
            print("job:",job)
            new_assigned = node.assigned + [(worker, job)]
            print("assigned:",new_assigned)
            new_remaining = node.remaining.difference({job})
            new_cost_so_far = node.cost_so_far + cost_matrix[worker][job]
            print("new_cost_so_far:",new_cost_so_far)

            next_node = Node(new_assigned, new_remaining, new_cost_so_far, cost_matrix)
            dfs(next_node)

    # Start DFS with initial node
    initial_node = Node([], all_workers_jobs, 0, cost_matrix)
    dfs(initial_node)

    return min_cost


# Example usage
cost_matrix = [[9, 2, 7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 2, 4]]
print("Minimum cost of assignment:", jobAssignment(cost_matrix))
