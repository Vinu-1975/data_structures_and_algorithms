class IndexedPriorityQueue:
    def __init__(self):
        self.heap = list()
        self.hash = dict()

    def is_empty(self):
        return len(self.heap) == 0

    def isContain(self, key):
        return key in self.hash

    def insert(self, key, priority):
        if self.isContain(key):
            print("Key already present !!")
            return

        self.heap.append([key, priority])
        self.hash[key] = len(self.heap) - 1
        self.bubbleUP(len(self.heap) - 1)

    def bubbleUP(self, idx):
        parent_idx = (idx - 1) // 2
        while idx > 0 and self.heap[parent_idx][1] > self.heap[idx][1]:
            self.heap[parent_idx], self.heap[idx] = (
                self.heap[idx],
                self.heap[parent_idx],
            )
            self.hash[self.heap[parent_idx][0]] = parent_idx
            self.hash[self.heap[idx][0]] = idx

            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def delete(self, key):
        if not self.isContain(key):
            print("key not found")
            return

        idx = self.hash[key]
        self.heap[idx], self.heap[len(self.heap) - 1] = (
            self.heap[len(self.heap) - 1],
            self.heap[idx],
        )
        self.hash[self.heap[idx][0]] = idx
        self.hash[self.heap[len(self.heap) - 1][0]] = len(self.heap) - 1
        self.heap.pop()
        del self.hash[key]
        self.bubbleUP(idx)
        self.bubbleDOWN(idx)

    def bubbleDOWN(self, idx):
        while True:
            left_child = 2 * idx + 1
            right_child = 2 * idx + 2
            smallest_idx = idx

            if (
                left_child < len(self.heap)
                and self.heap[left_child][1] < self.heap[smallest_idx][1]
            ):
                smallest_idx = left_child
            if (
                right_child < len(self.heap)
                and self.heap[right_child][1] < self.heap[smallest_idx][1]
            ):
                smallest_idx = right_child

            if idx == smallest_idx:
                break

            self.heap[idx], self.heap[smallest_idx] = (
                self.heap[smallest_idx],
                self.heap[idx],
            )
            idx = smallest_idx

    def name(self):
        print(self.heap)

    def age(self):
        print(self.hash)

    def update(self, index, priority):
        if not self.contains(index):
            raise ValueError("Index is not in the priority queue.")
        
        idx = self.hash[index]
        old_priority = self.heap[idx][1]
        self.heap[idx][1] = priority

        if priority < old_priority:
            self.bubbleUP(idx)
        elif priority > old_priority:
            self.bubbleDOWN(idx)

    def get_min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty.")
        
        return self.heap[0][0]

    def get_min_priority(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty.")
        
        return self.heap[0][1]


pq = IndexedPriorityQueue()

# Insert elements with priorities
pq.insert("A", 5)
pq.insert("B", 4)
pq.insert("C", 2)
pq.insert("D", 1)

# Update the priority of an element
# pq.update(2, 3)

# Delete an element
# pq.delete("C")

# Get the element with minimum priority
min_element = pq.get_min()
min_priority = pq.get_min_priority()

print("Min element:", min_element)  
print("Min priority:", min_priority)  

pq.name()
pq.age()
