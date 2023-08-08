#finding minimum using auxiliary stack

class Stack:
    def __init__(self):
        self.s = []
        self.aux = []

    def push(self,val):
        self.s.append(val)

        if not self.aux:
            self.aux.append(val)
        else:
            if val <= self.aux[-1]:
                self.aux.append(val)

    def getMin(self):
        if not self.aux:
            print("stack underflow")
            exit(1)
        return self.aux.pop()
    
if __name__ == "__main__":
    s = Stack()
    s.push(2)
    s.push(4)
    s.push(7)
    s.push(5)
    s.push(1)

    print(s.getMin())