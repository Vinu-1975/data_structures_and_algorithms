class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

def identical(x,y):
    if x is None and y is None:
        return True
    else:
        if x is not None and y is not None:
            checkLeft = identical(x.left,y.left)
            checkRight = identical(x.right,y.right)
            return x.val == y.val and checkLeft and checkRight

if __name__ == "__main__":
    x = Node(1)
    x.left = Node(2)
    x.right = Node(3)
    x.left = Node(4)
    
    y = Node(1)
    y.left = Node(2)
    y.right = Node(3)
    y.right = Node(4)

    print(identical(x,y))