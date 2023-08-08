class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def insert(root,val):
    if root is None:
        return Node(val)
    
    if root.val == val:
        return root
    elif val > root.val:
        root.right = insert(root.right,val)
    else:
        root.left = insert(root.left,val)

    return root

def getMinNode(root):
    if root.left is None and root.right is None:
        return root
    return getMinNode(root.left)

def delete(root,val):
    if root is None:
        return None
    if val < root.val:
        root.left = delete(root.left,val)
    elif val > root.val:
        root.right = delete(root.right,val)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        if root.right is None:
            temp = root.right
            root = None
            return temp
        temp = getMinNode(root.right)
        root.val = temp.val
        root.right = delete(root.right,temp.val)

def search(root,val):
    if root is None:
        return False
    if root.val == val:

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