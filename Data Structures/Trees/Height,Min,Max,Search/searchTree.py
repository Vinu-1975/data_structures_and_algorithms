class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def existInTree(root,val):
    if root is None:
        return False
    else:
        inLeft = existInTree(root.left,val)
        inRight = existInTree(root.right,val)
        return root.val == val or inLeft or inRight

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(existInTree(root,3))
    print(existInTree(root,7))