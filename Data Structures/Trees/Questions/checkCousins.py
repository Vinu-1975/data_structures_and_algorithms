class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

class NodeInfo:
    def __init__(self,node,level,parent):
        self.node = node
        self.level = level
        self.parent = parent

def updateLevelAndParent(root,x,y,parent = None,level = 1):
    if root is None:
        return
    
    updateLevelAndParent(root.left,x,y,root,level+1)

    if root == x.node:
        x.level = level
        x.parent = parent
    
    if root == y.node:
        y.level = level
        y.parent = parent

    updateLevelAndParent(root.right,x,y,root,level+1)


def isCousin(root,Node1,Node2):
    if root is None:
        return False
    
    level = 1
    parent = None

    x = NodeInfo(Node1,level,parent)
    y = NodeInfo(Node2,level,parent)

    updateLevelAndParent(root,x,y)

    return x.level == y.level and x.parent != y.parent

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    if isCousin(root,root.left.right,root.right.left):
        print("Cousin")
    else:
        print("Not a Cousin")