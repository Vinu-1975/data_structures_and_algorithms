from collections import Counter
from heapq import heappush, heappop

class Node:
    def __init__(self,symbol,freq,left=None,right=None):
        self.symbol = symbol
        self.freq = freq

        self.left = left
        self.right = right

        self.huff = ''
    def __str__(self) -> str:
        return f"({self.symbol},{self.freq})"
    def __repr__(self) -> str:
        return self.__str__()
    
    def __lt__(self,other):
        return self.freq < other.freq

def printNodes(node,val=''):
    newVal = val + str(node.huff)

    if node.left:
        printNodes(node.left,newVal)
    if node.right:
        printNodes(node.right,newVal)

    if not node.left and not node.right:
        print(f"{node.symbol} => {newVal}")

string = "vinayakan v s"
freq_table = Counter(string)
nodes = []
for k,v in freq_table.items():
    heappush(nodes,Node(k,v))
print(nodes)

while len(nodes) > 1:
    left = heappop(nodes)
    right = heappop(nodes)

    left.huff = 0
    right.huff = 1

    newNode = Node(left.symbol+right.symbol,left.freq+right.freq,left,right)

    heappush(nodes,newNode)
printNodes(nodes[0])