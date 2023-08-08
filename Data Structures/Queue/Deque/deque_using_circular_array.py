
class Deque:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(self.size)]
        self.front = -1
        self.rear = -1  

    def isFull(self):
        return ((self.rear+1) % self.size == self.front)

    def isEmpty(self):
        return (self.front == -1)

    def insertFront(self, data):
        if self.isFull():
            print("Queue is full")
            return
        # if queue is initially empty
        if self.front == -1:
            self.front = 0
            self.rear = 0
        # if front is at first position
        elif (self.front == 0):
            self.front = self.size - 1
        # decrement front end by 1
        else:
            self.front -= 1
        self.queue[self.front] = data

    def insertRear(self,data):
        if self.isFull():
            print("Queue is full")
            return
        
        #if queue is initially empty
        if(self.front == -1):
            self.front = 0
            self.rear = 0

        #rear is at last position of queue
        elif(self.rear == self.size - 1):
            self.rear = 0

        # increment rear by 1
        else:
            self.rear += 1

        self.queue[self.rear] = data

    def deleteFront(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        
        #queue has only one element
        if(self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            #back to initial position
            if(self.front == self.size - 1):
                self.front = 0
            #increment front by 1
            else:
                self.front = self.front + 1

    def deleteRear(self):
        if(self.isEmpty()):
            print("Queue is empty")
            return
        
        #queue has only one element
        if(self.front == self.rear):
            self.front = self.rear = -1
        elif(self.rear == 0):
            self.rear = self.size - 1
        else:
            self.rear = self.rear - 1

    def display(self):
        if(self.front == -1):
            print("Queue is empty")
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



if __name__ == "__main__":
    q = Deque(5)
    q.insertFront(4)
    q.display()
    q.insertFront(2)
    q.display()
    q.insertRear(6)
    q.display()
    q.insertRear(7)
    q.display()
    q.insertRear(9)
    q.display()

    q.insertRear(9)
    q.display()

    q.deleteFront()
    q.display()
    q.deleteRear()
    q.display()

    q.insertFront(30)
    q.display()
    q.insertRear(40)
    q.display()

            
