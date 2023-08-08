class Stack:
    def __init__(self):
        self.l=[]
    def push(self,val):
        self.l.append(val)
    def pop(self):
        self.l.pop()
    def top(self):
        print(self.l[-1])
    def size(self):
        print(len(self.l))
    def isEmpty(self):
        if(len(self.l)==0):
            return True
        return False
    def display(self):
        for i in self.l:
            print(i,end=" ")
        print("")
    
if __name__ == "__main__":
    s=Stack()
    ch = 100
    while (ch != 0):
        print("1. push")
        print("2. pop")
        print("3. top")
        print("4. size")
        print("5. isEmpty")
        print("6. display")
        print("Enter your choice:")
        ch = int(input())
        if (ch == 1):
            val = int(input())
            s.push(val)
        elif (ch == 2):
            s.pop()
        elif (ch == 3):
            s.top()
        elif (ch == 4):
            s.size()
        elif ch==5:
            print(s.isEmpty())
        elif (ch == 6):
            s.display()
