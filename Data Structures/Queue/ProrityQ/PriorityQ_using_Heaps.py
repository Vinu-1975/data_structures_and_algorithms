# The above class is a priority queue implementation in Python.
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)

    def enqueue(self, item, priority):
        # `element = (priority, self._index, item)` is creating a tuple with three elements:
        # `priority`, `self._index`, and `item`. This tuple represents an element in the priority
        # queue, where `priority` is the priority level of the element, `self._index` is a unique
        # index assigned to the element, and `item` is the actual item being stored in the queue. This
        # tuple is then appended to the `_queue` list.
        element = (priority, self._index, item)
        self._queue.append(element)
        self._upheap(len(self._queue) - 1)
        self._index += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        self._swap(0, len(self._queue) - 1)
        priority, _, item = self._queue.pop()
        self._downheap(0)
        return item

    def _upheap(self, index):
        parent = (index - 1) // 2
        # This line of code is checking if the parent of the current element exists (i.e., the current
        # element is not the root of the heap) and if the priority of the parent element is greater
        # than the priority of the current element. If both conditions are true, it swaps the
        # positions of the parent and current elements in the heap to maintain the heap property
        # (i.e., the parent element has a higher priority than its children). This process is repeated
        # recursively until the heap property is restored.
        if parent >= 0 and self._queue[parent] > self._queue[index]:
            self._swap(parent, index)
            self._upheap(parent)

    def _downheap(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < len(self._queue) and self._queue[left_child] < self._queue[smallest]:
            smallest = left_child

        if right_child < len(self._queue) and self._queue[right_child] < self._queue[smallest]:
            smallest = right_child

        if smallest != index:
            self._swap(index, smallest)
            self._downheap(smallest)

    def _swap(self, i, j):
        self._queue[i], self._queue[j] = self._queue[j], self._queue[i]

# Create a priority queue
pq = PriorityQueue()

# Enqueue items with priorities
pq.enqueue("Task 1", 3)
pq.enqueue("Task 2", 1)
pq.enqueue("Task 3", 2)

# Dequeue items
while not pq.is_empty():
    item = pq.dequeue()
    print(item)
