class Node:
    def __init__(self,value,priority):
        self.data=value
        self.priority=priority
        self.next = None

class PriorityQ:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def push(self,value,priority):
        newNode = Node(value,priority)
        if(self.isEmpty()):
            self.head = newNode
            return
        if self.head.priority < priority:
            newNode.next = self.head
            self.head = newNode

        else:
            temp = self.head
            while temp.next:
                if priority >= temp.next.priority:
                    break
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode
            return
    
    def pop(self):
        if self.isEmpty():
            return
        self.head = self.head.next
        return
    def peek(self):
        if self.isEmpty():
            return
        return self.head.data
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp= temp.next
        print()