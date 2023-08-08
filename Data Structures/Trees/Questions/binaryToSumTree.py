    #      1
    #     /\
    #    /  \     
    #   /    \       
    #  2      3
    #   \    / \
    #    4  5   6
    #      / \
    #     7   8

# to

    #     35
    #     /\
    #    /  \     
    #   /    \       
    #  4      26
    #   \    / \
    #    0  15  0
    #      / \
    #     0   0

class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

def printPreOrder(root):
    if root:
        print(root.val,end=" ")
        printPreOrder(root.left)
        printPreOrder(root.right)
    

def transform(root):
    if root is None:
        return 0
    else:
        left = transform(root.left)
        right = transform(root.right)

        old = root.val
        root.val = left + right
        
        return old + root.val

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left=Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    printPreOrder(root)
    print()
    transform(root)
    printPreOrder(root)