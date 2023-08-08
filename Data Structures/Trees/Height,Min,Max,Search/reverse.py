class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def reverse(root):
    if root is None:
        return 
    else:
        reverse(root.left)
        reverse(root.right)
        root.left,root.right = root.right, root.left

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

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    printLevelOrder(root)
    reverse(root)
    print()
    printLevelOrder(root)