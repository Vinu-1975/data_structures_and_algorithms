class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def insert(root,val):
    if root is None:
        return Node(val)
    if val == root.val:
        return root
    elif root.val < val:
        root.right = insert(root.right,val)
    else:
        root.left = insert(root.left,val)
    return root
    

def printLevelOrder(root):
    if root is None:
        return
    
    q = []

    q.append(root)
    while len(q) > 0:
        temp = q.pop(0)
        print(temp.val,end=" ")

        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.val,end=" ")
        printInOrder(root.right)

if __name__ == "__main__":
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)

    # printLevelOrder(root)
    printInOrder(r)