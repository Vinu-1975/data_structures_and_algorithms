class circularQueue():

    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        #condition for full queue
        if ((self.rear+1) % self.size == self.front):
            print("Queue is full")
        #condition for empty queue
        elif(self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            #next position of rear
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if(self.front == -1):
            print("Queue is empty")
        elif(self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front=(self.front + 1) % self.size
            return temp
    
    def display(self):
        if(self.front == -1):
            print('Queue is Empty')
            return
        if(self.rear>=self.front):
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        else:
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()

        
if __name__ == '__main__':
    q = circularQueue(5)
    q.enqueue(5)
    q.display()
    q.enqueue(6)
    q.display()
    q.enqueue(7)
    q.display()
    q.enqueue(8)
    q.display()
    q.enqueue(9)
    q.display()
    q.enqueue(10)
    q.display()

    c=q.dequeue()
    print(c)
    q.display()
    c=q.dequeue()
    print(c)
    q.display()
    c=q.dequeue()
    print(c)
    q.display()

    q.enqueue(20)
    q.display()
