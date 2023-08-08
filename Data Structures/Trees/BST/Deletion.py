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

def search(root,key):
    if root is None:
        return False
    if root.val == key:
        return True
    elif key<root.val:
        return search(root.left,key)
    else:
        return search(root.right,key)

def getMinValue(root):
    current  = root

    while(current.left is not None):
        current = current.left
    
    return current

def delete(root,key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete(root.left,key)
    elif key > root.val:
        root.right = delete(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        if root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp = getMinValue(root.right)

        root.val = temp.val

        root.right = delete(root.right,temp.val)
    return root

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
    print()
    print(search(r,100))
    print(search(r,20))
    print(search(r,70))
    print(search(r,80))

    r = delete(r,20)
    r = delete(r,30)
    r = delete(r,50)

    printLevelOrder(r)
