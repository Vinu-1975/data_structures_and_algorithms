class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
    
    # def deleteN(head,position):
    #     temp = head
    #     prev = head
    
    def deleteList(self):
        self.head = None
        #since garbage collection happens automatically 
        #only this step is required

if __name__ == '__main__':
    l = LinkedList()
    l.push(1)
    l.push(2)
    l.push(5)