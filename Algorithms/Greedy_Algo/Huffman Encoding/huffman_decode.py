from collections import Counter
from heapq import heappush, heappop

class Node:
    def __init__(self,symbol,freq,left=None,right=None) -> None:
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

def storeCode(codes,root,val):
    if root is None:
        return
    if root.symbol != '$':
        codes[root.symbol] = val
    storeCode(codes,root.left,val+'0')
    storeCode(codes,root.right,val+'1')

def decode_file(root,s):
    curr = root
    n = len(s)
    ans = ''
    for i in range(n):
        if s[i] == '0':
            curr = curr.left
        elif s[i] == '1':
            curr = curr.right

        if curr.left is None and curr.right is None:
            ans+=curr.symbol
            curr = root
    return ans

if __name__ == "__main__":
    s = "geeksforgeeks"
    freq_table = Counter(s)
    encodedVal, decodedVal = "",""
    heap = []
    for k,v in freq_table.items():
        heappush(heap,Node(k,v))
    # print(heap)
    codes = {}
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        
        newNode = Node('$',left.freq+right.freq,left,right)

        heappush(heap,newNode)
    
    storeCode(codes,heap[0],"")
    print(codes)
    encodedVal = ''.join(codes[char] for char in s)
    print(encodedVal)
    decodedVal = decode_file(heap[0],encodedVal)
    print(decodedVal)
    

