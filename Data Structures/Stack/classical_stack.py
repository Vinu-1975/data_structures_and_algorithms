class Stack:
    def __init__(self):
        self.top = -1
        self.stack = [None for i in range(4)]
        self.size = 4

    def push(self, val):
        if (self.size == self.top+1):
            print("Stack is Full")
            return
        self.top += 1
        self.stack[self.top] = val

    def pop(self):
        if(self.top == -1):
            print("STack is Empty")
            return
        val = self.stack[self.top]
        self.top-=1
        return val

    def top(self):
        return self.stack[self.top]
    
    def isEmpty(self):
        return self.top<1
