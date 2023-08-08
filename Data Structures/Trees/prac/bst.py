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
    elif val > root.val:
        root.right = insert(root.right,val)
    else:
        root.left = insert(root.left,val)
    return root

def getHeight(root):
    if root is None:
        return 0
    else:
        return 1 + max(getHeight(root.left),getHeight(root.right))
    
def getTreeSum(root):
    if root is None:
        return 0
    else:
        return root.val +getTreeSum(root.left)+getTreeSum(root.right)
    
def getTreeLeafSum(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:  # Check if the node is a leaf node
        return root.val
    else:
        return getTreeLeafSum(root.left) + getTreeLeafSum(root.right)

def levelOrderTrav(root):
    if root is None:
        return
    q=[root]
    while q:
        node = q.pop(0)
        print(node.val,end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

root = Node(0)
root = insert(root,-1)
root = insert(root,1)
root = insert(root,2)
root = insert(root,3)
root = insert(root,4)
root = insert(root,5)
levelOrderTrav(root)
print()
print(getHeight(root))
print(getTreeSum(root))
print(getTreeLeafSum(root))