class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.tail = None

    def addEnd(self, data):
        newNode = Node(data)
        if self.tail is None:
            newNode.next = newNode
            self.tail = newNode
            return
        newNode.next = self.tail.next
        self.tail.next = newNode
        self.tail = newNode

    def addBegin(self, data):
        newNode = Node(data)
        if self.tail is None:
            newNode.next = newNode
            self.tail = newNode
            return
        newNode.next = self.tail.next
        self.tail.next = newNode
        

    def display(self):
        if(self.tail == None):
            print("LL is empty")
            return
        temp = self.tail.next
        while True:
            print(temp.data,end=" ")
            temp = temp.next
            if self.tail.next == temp:
                break


if __name__ == "__main__":
    l = CLL()
    l.addBegin(4)
    l.addEnd(5)
    l.addEnd(6)
    l.addEnd(7)
    l.addEnd(8)
    l.addEnd(9)
    l.addBegin(10)
    l.display()
