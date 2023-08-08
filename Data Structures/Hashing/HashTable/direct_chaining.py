class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.hashTable = [None] * size
        self.size = size

    def hashFunction(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hashFunction(key)
        if self.hashTable[index] is None:
            self.hashTable[index] = Node(key, value)
        else:
            temp = self.hashTable[index]
            while temp is not None:
                if temp.key == key:
                    temp.value = value
                    return
                temp = temp.next
            temp.next = Node(key, value)

    def displayHashTable(self):
        for i, j in enumerate(self.hashTable):
            temp = j
            while temp is not None:
                print(f"{i}---key {temp.key}----value--{temp.value}")

                temp = temp.next

    def delete(self, key):
        index = self.hashFunction(key)
        if self.hashTable[index] is None:
            print("Item doesn't exist")
            return
        if self.hashTable[index] == key:
            self.hashTable[index] = self.hashTable[index].next
        else:
            temp = self.hashTable[index]
            while temp.next is not None:
                if temp.next.key == key:
                    temp.next = temp.next.next
                    break
                temp = temp.next


if __name__ == "__main__":
    table = HashTable(13)
    table.insert(1, "vinayak")
    table.insert(2, "vaibhav")
    table.insert(2, "aswin")
    table.insert(3, "sidharth")
    # table.displayHashTable()
    # table.delete(2)
    table.displayHashTable()
