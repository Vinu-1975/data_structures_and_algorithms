class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def enQueue(self,x):
        self.s1.append(x)

    def deQueue(self):

        if len(self.s1) == 0 and len(self.s2) == 0:
            print("Q is empty")
            return
        
        if len(self.s2)==0:
            while(self.s1):
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        return self.s2.pop()
        
    def display(self):
        print(self.s1)
        print(self.s2)
        


if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    q.display()

