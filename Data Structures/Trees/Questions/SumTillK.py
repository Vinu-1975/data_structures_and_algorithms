
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def isLeaf(root):
    if root.left is None and root.right is None:
        return True
    return False

def truncate(root,k,target = 0):

    if root is None:
        return None
    
    target = target + root.val

    root.left = truncate(root.left,k,target)
    root.right = truncate(root.right,k,target)

    if target < k and isLeaf(root):
        return None
    
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

if __name__ == "__main__":
    """ Construct the following tree
              6
            /   \
           /     \
          3       8
                /   \
               /     \
              4       2
            /   \      \
           /     \      \
          1       7      3
    """

    root = Node(6)
    root.left = Node(3)
    root.right = Node(8)
    root.right.left = Node(4)
    root.right.right = Node(2)
    root.right.left.left = Node(1)
    root.right.left.right = Node(7)
    root.right.right.right = Node(3)

    k = 20
    root = truncate(root, k)
    inorder(root)
