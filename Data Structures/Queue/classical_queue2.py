class Deque:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(self.size)]
        self.front = -1
        self.rear = -1

    def enque(self, data):
        if (self.rear+1 == self.size):
            print("Queue full")
            return
        if(self.front==-1):
            self.front=0
        self.rear += 1
        self.queue[self.rear] = data

    def Deque(self):
        if (self.front > self.rear):
            print("Queue Empty")
            return
        temp = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        print(temp)

        

    def display(self):
        for i in range(self.front,self.rear+1):
            print(self.queue[i],end=" ")
        print()


if __name__ == '__main__':
    q = Deque(5)
    q.enque(5)
    q.display()
    q.enque(6)
    q.display()
    q.enque(7)
    q.display()
    q.enque(8)
    q.display()
    q.enque(9)
    q.display()
    q.enque(10)
    q.display()

    q.Deque()
    q.display()
    q.Deque()
    q.display()
    q.Deque()
    q.display()
    q.Deque()
    q.display()
    q.Deque()
    q.display()
    q.Deque()
    q.display()
    q.Deque()
    q.display()

    q.enque(5)
    q.display()
