class HashTable:
    def __init__(self, size):
        self.maxSize = size
        self.hashTable = [None] * size
        self.currentSize = 0

    def hashFunction(self, key):
        return key % self.maxSize

    def insert(self, key, value):
        index = self.hashFunction(key)
        while self.hashTable[index] is not None:
            if self.hashTable[index][0] == key or self.hashTable[index][0] == "!":
                self.hashTable[index][1] = value
                return
            index = (index + 1) % self.maxSize
        self.hashTable[index] = [key, value]
        self.currentSize += 1

    def delete(self, key):
        index = self.hashFunction(key)
        while self.hashTable[index] is not None:
            if self.hashTable[index][0] == key:
                self.hashTable[index] = ["!", "!"]
                self.currentSize -= 1
                return
            index = (index + 1) % self.maxSize

    def search(self, key):
        index = self.hashFunction(key)
        intial_index = index
        while self.hashTable[index] is not None:
            if self.hashTable[index][0] == key:
                return self.hashTable[index][1]

            index = (index + 1) % self.maxSize
            if index == intial_index:
                break

        return "Item not found"

    def displayHashTable(self):
        for index, value in enumerate(self.hashTable):
            if value is None:
                print("NONE")
            else:
                print(f"{index} => ({value[0]},{value[1]})")


if __name__ == "__main__":
    h = HashTable(10)
    h.insert(4, "Vinayak")
    # h.insert(7,"Vaibhav")
    h.insert(14, "Charlie")
    h.insert(24, "Nidhi")
    h.insert(34, "Cheruvu")
    # h.insert(13,"Sahithee")
    h.delete(24)
    h.displayHashTable()
    print(h.search(24))
