class Queue:
    def __init__(self, size):
        self.queue = []
        self.max = size
        self.rear = -1
        self.front = -1

    def Enqueue(self, val):
        if (self.rear == self.max-1):
            print("Queue is full")
            return
        
        if (self.front == -1 and self.rear == -1):
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1
        self.queue.append(val)

    def Dequeue(self):
        if (self.front == -1 and self.front > self.rear):
            print("Queue is Empty!")
            return
        val = self.queue[self.front]
        self.queue.pop(self.front)
        self.front += 1
        return val
    
    # def frontt(self):
    #     return self.queue[self.front]
    
    # def rearr(self):
    #     print(self.rear)
    #     g = self.queue[self.rear]
    #     print(g)
        # return g
    
    def isFull(self):
        return len(self.queue) == self.max
    
    def isEmpty(self):
        return len(self.queue) == 0
    def __str__(self):
        return f'{self.queue}'
    
if __name__ == '__main__':
    q = Queue(5)
    print(q.isEmpty())
    print(q.isFull())
    q.Enqueue(4)
    q.Enqueue(5)
    q.Enqueue(6)
    q.Enqueue(7)
    q.Enqueue(8)
    q.Enqueue(9)
    print(q)

    q.Dequeue()
    print(q)

    # q.rearr()
    # print(q.rear())

