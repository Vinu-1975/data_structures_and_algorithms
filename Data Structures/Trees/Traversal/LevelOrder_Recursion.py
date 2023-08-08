class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

def printLevelOrder(root):
    h = height(root)
    for i in range(1,h+1):
        printCurrentLevel(root,i)

def printCurrentLevel(root,level):
    if root is None:
        return
    if level == 1:
        print(root.val,end=' ')
    else:
        printCurrentLevel(root.left,level - 1)
        printCurrentLevel(root.right,level - 1)

def height(N):
    if N is None:
        return 0
    else:
        lh = height(N.left)
        rh = height(N.right)

        if lh > rh :
            return lh + 1
        else:
            return rh + 1


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    printLevelOrder(root)
