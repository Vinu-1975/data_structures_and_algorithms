class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class CLL:
    def __init__(self):
        self.head = None
    
    def addEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            newNode.next = newNode
            self.head = newNode
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = newNode
        newNode.next = self.head
    
    def addBegin(self,data):
        newNode = Node(data)
        if self.head is None:
            newNode.next = newNode
            self.head = newNode
            return
        
        temp = self.head
        while(temp.next != self.head):
            temp = temp.next
        temp.next = newNode
        newNode.next = self.head
        self.head = newNode

    def display(self):
        temp = self.head
        while(temp.next != self.head):
            print(temp.data,end=" ")
            temp= temp.next
        print(temp.data,end=" ")
        print()

if __name__ == "__main__":
    l = CLL()
    l.addBegin(4)
    l.addEnd(5)
    l.display()
        

