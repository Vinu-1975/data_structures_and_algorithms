
class circularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(self.size)]
        self.front = self.rear = -1

    def Enqueue(self, data):
        # condition for full queue
        if ((self.rear+1) % self.size == self.front):
            print("Queue is full")
        # condition for empty queue
        elif (self.front == -1):
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def Dequeue(self):
        # condition for empty queue
        if (self.front == -1):
            print("Queue is empty")
        # condition for only one element
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):
        if (self.front == -1):
            print("Queue is empty")
        elif (self.rear >= self.front):
            for i in range(self.front, self.rear+1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


if __name__ == '__main__':
    c = circularQueue(5)
    ch = None
    while (ch != 0):
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. display")
        print("Enter your choice...:")
        ch = int(input())
        if (ch == 1):
            print("Enter the data to be enqueued:")
            data = int(input())
            c.Enqueue(data)
        elif(ch ==2):
            d= c.Dequeue()
            print("Dequeued data is:", d)
        elif(ch == 3):
            c.display()
        
