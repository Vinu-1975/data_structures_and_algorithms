class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self,size):
        self.maxSize = size
        self.top = None
        self.size = 0

    def push(self,val):
        newNode = Node(val)
        if self.top == None:
            self.top = newNode
            self.size = 1
            return
        if self.size == self.maxSize:
            print("Stack is Full")
            return
        newNode.next = self.top
        self.top = newNode
        self.size += 1

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return
        deleted_node = self.top
        self.top = self.top.next
        self.size -= 1
        return deleted_node.val
    
    def printStack(self):
        temp = self.top
        while temp:
            print(temp.val,end = " ")
            temp = temp.next
        print()
    
if __name__ == "__main__":
    s = Stack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.printStack()
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())


        