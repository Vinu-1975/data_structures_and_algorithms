class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def Preorder(root):
    if root:
        print(root.val, end=' ')
        Preorder(root.left)
        Preorder(root.right)


if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    Preorder(root)