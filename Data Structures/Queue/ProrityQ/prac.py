class IndexedPriorityQueue:
    def __init__(self):
        self.heap = []
        self.index_map = {}

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def contains(self, index):
        return index in self.index_map

    def insert(self, index, priority):
        if self.contains(index):
            raise ValueError("Index is already in the priority queue.")
        
        entry = [priority, index]
        self.heap.append(entry)
        self.index_map[index] = len(self.heap) - 1
        self._up_heapify(len(self.heap) - 1)

    def delete(self, index):
        if not self.contains(index):
            raise ValueError("Index is not in the priority queue.")
        
        idx = self.index_map[index]
        self._swap(idx, len(self.heap) - 1)
        self.heap.pop()
        del self.index_map[index]
        self._up_heapify(idx)
        self._down_heapify(idx)

    def update(self, index, priority):
        if not self.contains(index):
            raise ValueError("Index is not in the priority queue.")
        
        idx = self.index_map[index]
        old_priority = self.heap[idx][0]
        self.heap[idx][0] = priority

        if priority < old_priority:
            self._up_heapify(idx)
        elif priority > old_priority:
            self._down_heapify(idx)

    def get_min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty.")
        
        return self.heap[0][1]

    def get_min_priority(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty.")
        
        return self.heap[0][0]

    def _up_heapify(self, idx):
        parent_idx = (idx - 1) // 2

        while idx > 0 and self.heap[idx][0] < self.heap[parent_idx][0]:
            self._swap(idx, parent_idx)
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def _down_heapify(self, idx):
        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            smallest_child_idx = idx

            if left_child_idx < len(self.heap) and self.heap[left_child_idx][0] < self.heap[smallest_child_idx][0]:
                smallest_child_idx = left_child_idx

            if right_child_idx < len(self.heap) and self.heap[right_child_idx][0] < self.heap[smallest_child_idx][0]:
                smallest_child_idx = right_child_idx

            if smallest_child_idx == idx:
                break

            self._swap(idx, smallest_child_idx)
            idx = smallest_child_idx

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.index_map[self.heap[i][1]] = i
        self.index_map[self.heap[j][1]] = j

    def name(self):
        print(self.heap)

    def age(self):
        print(self.index_map)

# Create an indexed priority queue
pq = IndexedPriorityQueue()

# Insert elements with priorities
pq.insert("A", 5)
pq.insert("B", 4)
pq.insert("C", 2)
pq.insert("D", 1)

# Update the priority of an element
# pq.update(2, 3)

# Delete an element
pq.delete("C")

# Get the element with minimum priority
min_element = pq.get_min()
min_priority = pq.get_min_priority()

print("Min element:", min_element)  # Output: 4
print("Min priority:", min_priority)  # Output: 1

pq.name()
pq.age()