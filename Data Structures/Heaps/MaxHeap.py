class MaxHeap:
    arr = []
    maxSize = 0
    heapSize = 0

    def __init__(self,size):
        self.maxSize = size
        self.arr = [None] * size
        self.heapSize = 0

    def parent(self,i):
        return (i-1)//2

    def insert(self,x):

        if self.heapSize == self.maxSize:
            print("Heap is FULL")
            return
        
        i = self.heapSize
        self.heapSize+=1
        self.arr[i] = x

        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)


    def delete(self,i):

        self.increaseKey(i,float("inf"))
        self.removeMax()

    def increaseKey(self,i,newVal):

        self.arr[i] = newVal

        while i!=0 and self.arr[self.parent(i)] < self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)

    def removeMax(self):

        if self.heapSize <=0:
            return None
        if self.heapSize == 1:
            self.heapSize -= 1
            return self.arr[0]
        
        root = self.arr[0]
        self.arr[0] = self.arr[self.heapSize - 1]
        self.heapSize -= 1

        self.MaxHeapify(0)

        return root
    
    def lChild(self,i):
        return 2*i + 1
    
    def rChild(self,i):
        return 2*i + 2

    def MaxHeapify(self,i):
        l = self.lChild(i)
        r = self.rChild(i)
        largest = i
        if l < self.heapSize and self.arr[l] > self.arr[i]:
            largest = l
        if r < self.heapSize and self.arr[r] > self.arr[largest]:
            largest = r

        if largest != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp
            self.MaxHeapify(largest)
    def prent(self):
        print(self.arr)


if __name__ == "__main__":
	
	print('The minHeap is ')
	minHeap = MaxHeap(15)
	minHeap.insert(5)
	minHeap.insert(3)
	minHeap.insert(17)
	minHeap.insert(10)
	minHeap.insert(84)
	minHeap.insert(19)
	minHeap.insert(6)
	minHeap.insert(22)
	minHeap.insert(9)
	# minHeap.minHeap()

	# minHeap.Print()
	# print("The Min val is " + str(minHeap.remove()))
	minHeap.prent()
        


