class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while (temp.next is not None):
            temp = temp.next
        temp.next = newNode

    def pop(self):
        if self.head is None:
            print("Stack is empty!")
            return
        temp = self.head
        temp2 = None
        while(temp.next is not None):
            temp2 = temp
            temp = temp.next
        temp2.next = None

    def display(self):
        temp = self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp = temp.next
        print("")
    
    def top(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        print(temp.data)

    def size(self):
        cnt = 0
        temp = self.head
        while(temp is not None):
            cnt+=1
            temp = temp.next
        print(cnt)

if __name__ == '__main__':
    s=Stack()
    ch = 100
    while(ch != 0):
        print("1. push")
        print("2. pop")
        print("3. top")
        print("4. size")
        print("5. display")
        print("Enter your choice:")
        ch=int(input())
        if(ch==1):
            val= int(input())
            s.push(val)
        elif(ch==2):
            s.pop()
        elif(ch==3):
            s.top()
        elif(ch==4):
            s.size()
        elif(ch==5):
            s.display()
