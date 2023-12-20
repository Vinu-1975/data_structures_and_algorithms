from queue import Queue

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

class Node:
    def __init__(self, level, profit, bound, weight):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight

def bound(node, n, W, items):
    # if weight overcomes the knapsack capacity, return 0 as expected bound
    if node.weight >= W:
        return 0

    # initialize bound on profit by current profit
    profit_bound = node.profit

    # start including items from index 1 more to current item index
    j = node.level + 1
    totweight = node.weight

    # checking index condition and knapsack capacity condition
    while j < n and totweight + items[j].weight <= W:
        totweight += items[j].weight
        profit_bound += items[j].value
        j += 1

    # If k is not n, include last item partially for upper bound on profit
    if j < n:
        profit_bound += (W - totweight) * items[j].ratio

    return profit_bound

def knapsackBranchAndBound(W, items):
    items.sort(key=lambda x: x.ratio, reverse=True)
    Q = Queue()
    n = len(items)

    # initialize dummy node at starting
    v = Node(-1, 0, 0, 0)
    Q.put(v)

    maxProfit = 0

    # One by one extract an item from decision tree
    # compute profit of all children of extracted item
    # and keep saving maxProfit
    while not Q.empty():
        v = Q.get()

        if v.level == -1:
            u_level = 0
        elif v.level != (n - 1):
            u_level = v.level + 1

        # If it's the last node
        if v.level == n-1:
            continue

        # If not last node, consider next item to be added in knapsack
        u = Node(u_level, v.profit + items[u_level].value, 0, v.weight + items[u_level].weight)

        # If cumulated weight is less than W and profit is greater than previous profit, update maxProfit
        if u.weight <= W and u.profit > maxProfit:
            maxProfit = u.profit

        # Get the upper bound on profit to decide whether to add u to Q or not.
        u.bound = bound(u, n, W, items)

        # If bound value is greater than profit, then only push into queue for further consideration
        if u.bound > maxProfit:
            Q.put(u)

        # Do the same thing, but without considering the next item to be added in the knapsack
        u = Node(u_level, v.profit, 0, v.weight)
        u.bound = bound(u, n, W, items)
        if u.bound > maxProfit:
            Q.put(u)

    return maxProfit

# Example usage
items = [Item(10, 60), Item(20, 100), Item(30, 120)]
W = 50
print("Maximum value in Knapsack =", knapsackBranchAndBound(W, items))
