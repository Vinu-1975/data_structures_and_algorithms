class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self,index):
        return (index - 1)//2
    
    def left_child(self,index):
        return 2*index+1
    
    def right_child(self,index):
        return 2*index+2
    
    def has_left_child(self,index):
        return self.left_child(index) < len(self.heap)
    
    def has_right_child(self,index):
        return self.right_child(index) < len(self.heap)
    
    def swap(self,index1,index2):
        self.heap[index1],self.heap[index2] = self.heap[index2],self.heap[index1]

    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def heapify_up(self,index):
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.swap(self.heap[self.parent(index)],self.heap[index])
            index = self.parent(index)

    def remove_max(self):
        if len(self.heap) == 0:
            raise Exception("Heap is empty")
        
        max_value = self.heap[0]
        self.heap[0] = self.heap(len(self.heap)-1)
        self.heap.pop()
        self.heapify_down(0)
        return max_value
    
    def heapify_down(self,index):
        while self.has_left_child(index):
            max_child_index = self.left_child(index)
            if self.has_right_child(index) and self.heap[self.right_child(index)] > self.heap[self.left_child(index)]:
                max_child_index = self.right_child(index)

            if self.heap[index] > self.heap[max_child_index]:
                break

            self.swap(index, max_child_index)
            index = max_child_index

    def __str__(self):
        return str(self.heap)

# Example usage
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(30)
max_heap.insert(5)

print(max_heap)  # Output: [30, 20, 10, 5]

print(max_heap.remove_max())  # Output: 30
print(max_heap)  # Output: [20, 5, 10]