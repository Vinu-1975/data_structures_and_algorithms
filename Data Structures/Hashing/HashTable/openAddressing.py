class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

    def delete(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size

    def display(self):
        for index, item in enumerate(self.table):
            if item is not None:
                print(f"Index {index}: {item[0]} => {item[1]}")
            else:
                print(f"Index {index}: None")


# Example usage:
hash_table = HashTable(10)
hash_table.insert(5, "Apple")
hash_table.insert(15, "Banana")
hash_table.insert(25, "Orange")

print("HashTable:")
hash_table.display()

print("Search 15:", hash_table.search(15))
print("Search 25:", hash_table.search(25))

hash_table.delete(15)

print(hash_table.search(25))
print("HashTable after deletion:")
hash_table.display()
