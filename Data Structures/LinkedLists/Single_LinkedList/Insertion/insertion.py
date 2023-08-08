class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push_back(self, val):
        newNode = Node(val)
        if (self.head == None):
            self.head = newNode
            return
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = newNode

    def push_front(self, val):
        newNode = Node(val)
        if (self.head is None):
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode

    def insert_after(self,key,val):
        newNode = Node(val)
        if(self.head.data == key):
            newNode.next = self.head.next
            self.head.next = newNode
            return
        temp = self.head
        while(temp.data != key):
            temp = temp.next
            if temp is None:
                return
        newNode.next = temp.next
        temp.next = newNode
    
    def print_list(self):
        temp = self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp = temp.next
        print("")


if __name__ == '__main__':
    list = LinkedList()
    ch = None
    while(ch!=0):
        print("1.pushback")
        print("2.pushfront")
        print("3.insertafter")
        print("4.print_list")
        ch=int(input())
        if ch == 1:
            print("enter value to add: ")
            val = int(input())
            list.push_back(val)
        elif ch == 2:
            print("enter value to add: ")
            val = int(input())
            list.push_front(val)
        elif ch == 3:
            print("enter value to add: ")
            val = int(input())
            print("enter key: ")
            key = int(input())
            list.insert_after(key,val)
        elif ch == 4:
            list.print_list()

